from django.contrib import admin



from .models import Doctor, Announcement

admin.site.register(Doctor)
admin.site.register(Announcement)