from django import forms
from django.forms import ModelForm, PasswordInput, EmailInput

from .models import *


class RegisterCustomerForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    address = forms.CharField(max_length=500)

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "address"]


class RegisterRestaurantForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    image = forms.ImageField()

    class Meta:
        model = Restaurant
        fields = ["username", "password", "email", 'image']


class AddProduct(ModelForm):
    class Meta:
        model = Product
        fields = []