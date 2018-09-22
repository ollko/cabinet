from django import forms
from .models import Product

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name',)
