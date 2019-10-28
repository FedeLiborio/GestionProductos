from django import forms

FRUIT_CHOICES= []

class CheckoutForm(forms.Form):
    metodoDePago = forms.ChoiceField(choices=FRUIT_CHOICES)
    nombre = forms.CharField(label='algo', required=True)