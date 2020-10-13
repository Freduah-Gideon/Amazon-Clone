from django import forms
from .models import Checkout
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
class CheckoutForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name *', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder':'Enter Your Full Name'
    }))
    address_1 = forms.CharField(label='Address *', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder':'Enter Address To Be Shipped To'
    }))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder':'Enter An Optional Delivery Address'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input',
        'placeholder':'Phone Number May Be Used To Assist Deliveries (Optional)'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }))
    region = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input'
    }))
     
    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input'
    }))
    
    additional_info = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-input additional-info',
        'placeholder':'Optional'
    }))
    country = CountryField().formfield(attrs={
        'class':'form-input'
    })
    is_saved = forms.BooleanField(widget=forms.CheckboxInput(),label='Save For Next Time ',)
    

    class Meta: 
        model = Checkout
        fields = ['full_name','region', 'country','city','address_1', 'address_2',
                   'zip_code', 'phone', 'additional_info', 'payment_option','is_saved']
        # widgets = {'country':CountrySelectWidget()} 