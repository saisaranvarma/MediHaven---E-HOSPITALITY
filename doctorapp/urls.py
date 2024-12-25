from . import views
from django.urls import path

urlpatterns = [
    path('doctorview/',views.doctorview,name='doctorview'),
    path('doctorlogin/',views.doctorlogin,name='doctorlogin'),
    path('change-password/', views.change_password, name='change_password'),
    path('add-patient-details/', views.add_patient_details, name='add_patient_details'),
    path('patients/', views.patient_list_view, name='patient_list'),


]