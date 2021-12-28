from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    macAddress = forms.CharField()
    port = forms.NumberInput()
    
class PatientForm(forms.Form):
    patient_name = forms.CharField()
    address = forms.CharField()
    dob = forms.DateField()
    gender = forms.CharField()
    license_number = forms.CharField()