from django import forms
from .models import Client, Status

class ClientForm(forms.ModelForm):
    client_registered = forms.DateField()
    class Meta:
        model       = Client
        fields      = ['client_no', 'client_name', 'client_address', 'client_email', 'client_registered', 'client_ip']

        widgets = {
            'client_registered' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control', 'placeholder':'Select a date'})
        }

class StatusForm(forms.ModelForm):
    #status_date = forms.DateField()
    class Meta:
        model       = Status
        fields      = ['client', 'status_type', 'status_note']