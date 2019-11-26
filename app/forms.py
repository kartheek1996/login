from django import forms
from .models import Register

import time

YEARS = [x for x in range(1940, int(time.strftime("%Y")) + 1)]


class Registerform(forms.Form):
    fname = forms.CharField(max_length=30, label="First Name")
    lname = forms.CharField(max_length=30, label="Last Name")
    password = forms.CharField(widget=forms.PasswordInput)
    Cpassword = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    email = forms.EmailField()
    D_O_B = forms.DateField(label="Enter date of birth", widget=forms.SelectDateWidget(years=YEARS))
