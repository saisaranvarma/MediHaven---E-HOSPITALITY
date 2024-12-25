from . import views
from django.urls import path

urlpatterns = [
    path('adminuser/',views.adminuser,name='adminuser'),
    path('register-doctor/', views.register_doctor, name='register-doctor'),
    path('patientview2/',views.patientview2,name='patient-view'),
    path('doctorupdate/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('doctordelete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('update_patient/<int:pk>/', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('announcements/', views.announcements_view, name='announcements'),



]