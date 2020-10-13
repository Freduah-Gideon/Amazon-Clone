from .models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'placeholder': 'First Name Is Required'
    }),required=True)
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={
        'placeholder':'Email Address Is Required'
    }),required=True)
    phone = forms.CharField(label='Phone Number', widget=forms.NumberInput(attrs={
        'placeholder': 'Phone Number Is Required'
    }),required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter A Secure Password'
    }),required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Your Password'
    }),required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'phone', 'password', 'password2']
