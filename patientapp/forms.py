from django import forms
from .models import Patientregister

class PatientForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Birth")

    class Meta:
        model = Patientregister
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
