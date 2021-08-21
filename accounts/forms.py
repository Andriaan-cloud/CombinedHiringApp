# File: forms.py
from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import *

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
            'end_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }