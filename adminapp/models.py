from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    password = models.CharField(max_length=128)  # Use 128 for compatibility with hashed passwords

    def __str__(self):
        return self.name

class Announcement(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]  # Display first 50 characters in admin panel
