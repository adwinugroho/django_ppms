from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    macAddress = forms.CharField()
    port = forms.NumberInput()