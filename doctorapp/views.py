from django.shortcuts import render, redirect
from django.contrib import messages

from adminapp.models import Doctor, Announcement
from doctorapp.forms import DoctorLoginForm, PatientDetailsForm
from doctorapp.models import PatientDetails
from patientapp.models import Appointment


def doctorview(request):
    # Check if the doctor is logged in
    announcements=Announcement.objects.all()
    doctors = Doctor.objects.all()  # Get all doctors
    doctor_count = doctors.count()
    doctor_id = request.session.get('doctor_id')
    if not doctor_id:
        # Redirect to login if no session exists
        messages.error(request, "Please log in to view this page.")
        return redirect('doctorlogin')

    # Fetch the logged-in doctor's details
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        messages.error(request, "Doctor not found.")
        return redirect('doctorlogin')

    # Fetch appointments assigned to this doctor
    appointments = Appointment.objects.filter(doctor=doctor.name)

    # Pass the doctor details and appointments to the template
    context = {
        'doctor': doctor,
        'appointments': appointments,
        'doctor_count':doctor_count,
        'announcements':announcements,
    }
    return render(request, 'doctor/docindex.html', context)



def doctorlogin(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                # Check if a doctor exists with the given email and password
                doctor = Doctor.objects.get(email=email, password=password)
                # Store doctor ID and email in session for later use
                request.session['doctor_id'] = doctor.id
                request.session['doctor_email'] = doctor.email  # Add this line
                messages.success(request, 'Login successful!')
                return redirect('doctorview')  # Redirect to dashboard or desired page
            except Doctor.DoesNotExist:
                messages.error(request, 'Invalid email or password')
    else:
        form = DoctorLoginForm()
    return render(request, 'doctor/doclogin.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        # Fetch new password and confirmation
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('change_password')

        # Fetch the logged-in doctor's email from the session
        doctor_email = request.session.get('doctor_email')
        try:
            doctor = Doctor.objects.get(email=doctor_email)
        except Doctor.DoesNotExist:
            messages.error(request, "Doctor not found.")
            return redirect('doctorview')  # Redirect to login if no valid session

        # Save the new password as plain text
        doctor.password = new_password
        doctor.save()
        messages.success(request, "Password updated successfully.")
        return redirect('doctorview')  # Redirect to the dashboard or another page
    return render(request, 'doctor/change_password.html')



def add_patient_details(request):
    if request.method == 'POST':
        form = PatientDetailsForm(request.POST)
        if form.is_valid():
            patient_details = form.save(commit=False)
            # Set the doctor (logged-in user) as the one adding the details
            patient_details.added_by_id = request.session.get('doctor_id')
            patient_details.save()
            messages.success(request, "Patient details saved successfully!")
            return redirect('doctorview')  # Redirect to doctor dashboard or desired page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PatientDetailsForm()

    return render(request, 'doctor/add_patient_details.html', {'form': form})



def patient_list_view(request):
    # Fetch all patient details
    patients = PatientDetails.objects.all()
    return render(request, 'doctor/patient_list.html', {'patients': patients})