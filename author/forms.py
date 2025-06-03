from django import forms
from.models import employee

class SignupForm(forms.ModelForm):
    class Meta:
        model=employee
        fields=['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class LoginForm(forms.Form):
    identifier = forms.CharField(label='Name or Email')
    password = forms.CharField(widget=forms.PasswordInput)