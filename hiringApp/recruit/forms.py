from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'surname': 'Surname',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'province': 'Province',
            'industry': 'Industry',
            'job_title': 'Job Title',
            'bio': 'Biography',
            'date_of_birth ':'Date of birth',
            'social': 'Where did you hear about us ?'

        }
        widgets = {
            'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'end_date': DatePickerInput(format='%Y-%m-%d'),# specify date-frmat
        }


