from django import forms
from crispy_forms.helper import FormHelper
from .models import Product

class PaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_show_labels = False
        print('self.helper.form_show_labels =', self.helper.form_show_labels)

    class Meta:
        model = Product
        fields = ('name',)
