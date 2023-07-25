
from django import forms
from django.contrib.auth.models import User
from product.models import Products

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','date_joined']

class ProductForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())


class DoctorForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())
    month = forms.ChoiceField(choices=[(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),
    (7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')])  

class DealsForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())
    month = forms.ChoiceField(choices=[(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),
    (7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')])  

