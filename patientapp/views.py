from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from adminapp.models import Doctor
from .forms import PatientForm, LoginForm
from django.contrib import messages

from .models import Patientregister, Appointment


def patientview(request):
    doctors = Doctor.objects.all()
    doctor_count = doctors.count()

    patient_name = request.session.get('patient_name', 'Guest')
    context = {
        'doctors': doctors,
        'patient_name': patient_name,
        'doctor_count':doctor_count,
    }


    return render(request,'patient/index.html',context)

def patientview2(request):
    patient_name = request.session.get('patient_name', 'Guest')
    doctors = Doctor.objects.all()  # Get all doctors
    doctor_count = doctors.count()
    departments = doctors.values_list('specialization', flat=True).distinct()

    context = {
        'patient_name': patient_name,
        'departments': departments,
        'doctors': doctors,
        'doctor_count':doctor_count,
    }

    return render(request,'patient/index2.html',context)

def patientregister(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # Save the form data temporarily without committing to the database
            patient = form.save(commit=False)
            # Store the plain text password (no hashing)
            patient.password = form.cleaned_data['password']
            # Save the patient instance to the database
            patient.save()
            messages.success(request, 'Patient registered successfully!')
            return render(request, 'patient/registration.html', {'form': PatientForm()})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PatientForm()

    return render(request, 'patient/registration.html', {'form': form})


def patient_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            print(f"Form is valid. Email: {email}, Password: {password}")  # Debugging output

            try:
                # Look for the patient with the given email
                patient = Patientregister.objects.get(email=email)

                # Compare the plain text passwords
                if password == patient.password:
                    # Save patient details in the session
                    request.session['patient_name'] = patient.first_name
                    request.session['patient_email'] = patient.email  # Save email in session

                    messages.success(request, "Login successful!")
                    return redirect('patientview2')  # Redirect to a dashboard or another page
                else:
                    print(f"Invalid password entered for {email}")  # Debugging output
                    messages.error(request, "Invalid password.")
            except Patientregister.DoesNotExist:
                print(f"No patient found with email {email}")  # Debugging output
                messages.error(request, "Patient with this email does not exist.")
        else:
            print(f"Form is invalid: {form.errors}")  # Debugging output
    else:
        form = LoginForm()

    return render(request, 'patient/login.html', {'form': form})



def appointment_view(request):
    if request.method == "POST":
        # Extracting data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        message = request.POST.get("message", "")  # Default to empty string if not provided

        # Save data to the database
        appointment = Appointment(
            name=name,
            email=email,
            phone=phone,
            date=date,
            department=department,
            doctor=doctor,
            message=message,
        )
        appointment.save()

        # Handle success response
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"message": "Your appointment request has been sent successfully. Thank you!!"}, status=200)
        return redirect('patientview2')  # Adjust the redirection as needed

    # Render the appointment form page (GET request)
    return render(request, 'index2.html')




def calculate_bmi(request):
    if request.method == "POST":
        try:
            # Extract height and weight from POST request
            height = float(request.POST.get("height", 0))
            weight = float(request.POST.get("weight", 0))

            if height <= 0 or weight <= 0:
                return JsonResponse({"error": "Height and weight must be positive numbers."}, status=400)

            # BMI calculation
            height_meters = height / 100  # Convert height to meters
            bmi = weight / (height_meters ** 2)

            # BMI category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"

            return JsonResponse({"bmi": round(bmi, 2), "category": category})
        except ValueError:
            return JsonResponse({"error": "Invalid input. Please provide numbers only."}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405)


def treatment_history(request):
    # Assuming the patient is logged in and their ID or email is in the session
    patient_email = request.session.get('patient_email')

    # Fetch the patient information
    try:
        patient = Patientregister.objects.get(email=patient_email)
    except Patientregister.DoesNotExist:
        patient = None

    # Fetch the appointments of the patient
    appointments = Appointment.objects.filter(email=patient_email)

    context = {
        'patient': patient,
        'appointments': appointments,
    }
    return render(request, 'patient/treatmenthistory.html', context)