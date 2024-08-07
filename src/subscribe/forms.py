from django import forms
from src.subscribe.models import Subscribes

class SubscribeForm(forms.ModelForm):
  class Meta:
    model = Subscribes
    fields = (
        'user_id',
        'name',
        'email',
        'phone',
        'status',
        'unsubscribe'
      )