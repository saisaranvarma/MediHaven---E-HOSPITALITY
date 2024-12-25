from django import forms
from .models import PatientDetails

class DoctorLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")





class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ['patient_name', 'age', 'issue', 'diagnosis', 'medicines']
        widgets = {
            'issue': forms.Textarea(attrs={'rows': 4}),
            'diagnosis': forms.Textarea(attrs={'rows': 4}),
            'medicines': forms.Textarea(attrs={'rows': 3}),
        }

