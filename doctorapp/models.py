from django.db import models


class PatientDetails(models.Model):
    patient_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    issue = models.TextField()
    diagnosis = models.TextField()
    medicines = models.TextField()
    added_by = models.ForeignKey('adminapp.Doctor', on_delete=models.CASCADE)  # Reference to the logged-in doctor

    def __str__(self):
        return f"{self.patient_name} ({self.age} years) - {self.issue[:30]}"
