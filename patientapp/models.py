from django.db import models

class Patientregister(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Store plain password

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    department = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return f"{self.name} - {self.department} - {self.date}"
