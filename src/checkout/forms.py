from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(
        label='Credit card number', 
        required=False)
    cvv = forms.CharField(
        label='Security code (CVV)',
        required=False)
    expiry_month = forms.ChoiceField(
        label='Month',
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={'class':'checkout-form-control'}),
        required=False)
    expiry_year = forms.ChoiceField(
        label='Year', 
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class':'checkout-form-control'}),
        required=False)
    stripe_id = forms.CharField(
        widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'street_address',
            'town_or_city','postcode', 'country'
        )