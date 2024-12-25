from django.shortcuts import render,get_object_or_404, redirect

from adminapp.forms import DoctorRegistrationForm, AnnouncementForm
from adminapp.models import Doctor, Announcement
from patientapp.forms import PatientForm
from patientapp.models import Patientregister


def adminuser(request):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()
    context = {
        'doctors': doctors,
        'doctor_count': doctor_count,
        'patients': patients,
        'patient_count': patient_count,

    }

    return render(request,'admin/index.html',context)


def register_doctor(request):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()

    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register-doctor')  # Replace with the desired redirect URL
    else:
        form = DoctorRegistrationForm()

    context = {
        'doctors': doctors,
        'doctor_count': doctor_count,
        'patients': patients,
        'patient_count': patient_count,
        'form': form

    }
    return render(request, 'admin/register_doctor.html', context)

def patientview2(request):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    context={
        'patients': patients,
        'patient_count': patient_count,
        'doctors': doctors,
        'doctor_count': doctor_count,
        'patients': patients,
        'patient_count': patient_count,


    }
    return render(request, 'admin/patients.html', context)

def update_doctor(request, pk):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()




    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('adminuser')  # Replace 'doctor_list' with your list view name
    else:
        form = DoctorRegistrationForm(instance=doctor)

    context = {
        'doctors': doctors,
        'doctor_count': doctor_count,
        'patients': patients,
        'patient_count': patient_count,
        'form': form,

    }
    return render(request, 'admin/update_doctor.html', context)

def delete_doctor(request, pk):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('adminuser')  # Replace 'doctor_list' with your list view name

    context = {
        'doctors': doctors,
        'doctor_count': doctor_count,
        'patients': patients,
        'patient_count': patient_count,
        'doctor': doctor,


    }
    return render(request, 'admin/confirm_delete.html', context)


def update_patient(request, pk):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()


    patient = get_object_or_404(Patientregister, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('adminuser')  # Redirect to the admin dashboard or patient list
    else:
        form = PatientForm(instance=patient)

    context = {
        'doctors': doctors,
        'doctor_count': doctor_count,
        'patients': patients,
        'patient_count': patient_count,
        'form': form,
        'patient': patient

    }

    return render(request, 'admin/update_patient.html', context)

def delete_patient(request, pk):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()


    patient = get_object_or_404(Patientregister, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('adminuser')  # Redirect to the admin dashboard or patient list

    context = {
        'doctors': doctors,
        'doctor_count': doctor_count,
        'patients': patients,
        'patient_count': patient_count,
        'patient': patient

    }

    return render(request, 'admin/confirm_delete_patient.html', context)


def announcements_view(request):
    doctors = Doctor.objects.all()
    patients = Patientregister.objects.all()
    patient_count = patients.count()

    doctor_count = doctors.count()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminuser')  # Redirect to the same page or another
    else:
        form = AnnouncementForm()
    context = {
            'doctors': doctors,
            'doctor_count': doctor_count,
            'patients': patients,
            'patient_count': patient_count,
            'form': form

        }

    return render(request, 'admin/announcements.html', context)



