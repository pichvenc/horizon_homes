from django import forms

from horizon_main.models import RequestViewing


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15)


class ViewRequestForm(forms.Form):
    preferred_date = forms.DateField(widget=forms.SelectDateWidget)

