from . import views
from django.urls import path

urlpatterns = [
    path('',views.patientview,name='patientview'),
    path('patient/',views.patientview2,name='patientview2'),
    path('register/',views.patientregister,name='patientregister'),
    path('login/', views.patient_login, name='patient_login'),
    path('appointment/',views.appointment_view,name='appointment'),
    path('bmi/', views.calculate_bmi, name='calculate_bmi'),
    path('treatmenthistory/',views.treatment_history,name='treatmenthistory')

]