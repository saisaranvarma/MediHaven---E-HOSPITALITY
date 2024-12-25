from django.contrib import admin

from .models import Patientregister
from .models import Appointment

admin.site.register(Patientregister)
admin.site.register(Appointment)
