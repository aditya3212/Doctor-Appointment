from datetime import date

from django import forms
#from datetimewidget.widgets import DateTimeWidget

from .models import Appointment
from .models import Doctor

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = "__all__"
        

class DoctorForm(forms.ModelForm):

    class Meta:
        model=Doctor
        fields="__all__"
    
    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)', code='invalid')
        if day.isoweekday() in (0, 6):
            raise forms.ValidationError('Date should be a workday', code='invalid')

        return day
        