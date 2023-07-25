from django import forms
from .models import Products

class ProductRegistration(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['Product_name','company_name','Product_image','Product_price','EnteredBy']

    
    Product_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'})
    )

    company_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'company_name'})
    )

    Product_image = forms.ImageField(
        widget = forms.FileInput(attrs={'class':'form-control'})
    )

    Product_price = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'price'})
    )

    EnteredBy = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

