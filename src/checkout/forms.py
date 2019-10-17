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
        required=False)
    expiry_year = forms.ChoiceField(
        label='Year', 
        choices=YEAR_CHOICES, 
        required=False)
    stripe_id = forms.CharField(
        widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Full Name',
        required=True)
    phone_number = forms.CharField(
        label='Phone Number',
        required=True)
    street_address1 = forms.CharField(
        label='Street Address 1',
        required=True)
    street_address2 = forms.CharField(
        label='Street Address 2 (optional)',
        required=False)
    town_or_city = forms.CharField(
        label='Town or city',
        required=True)
    postcode = forms.CharField(
        label='Postcode', 
        required=False)
    county = forms.CharField(
        label='County', 
        required=False)
    country = forms.CharField(
        label='Country',
        required=True)
    

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'street_address1' , 'street_address2' ,
            'town_or_city','postcode', 'county', 'country'
        )