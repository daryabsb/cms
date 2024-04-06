from django import forms
from src.contactus.models import ContactUs


class ContactusForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ( 
            'name',
            'email',
            'phone',
            'message',
        )