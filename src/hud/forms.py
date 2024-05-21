from django import forms
from src.hud.models import PosOrderItem


class PosOrderItemForm(forms.ModelForm):

    class Meta:
        model = PosOrderItem
        fields = ['order', 'product', 'quantity', 'discount', 'discount_type']
