from django import forms
from .models import Doctors

class DoctorRegistration(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['Doctor_Name','Doctor_Specialisation','Doctor_Contact_Number','Doctor_Location','EnteredBy']

    
    Doctor_Name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'})
    )

    Doctor_Specialisation = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Specialisation'})
    )

    Doctor_Contact_Number = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact_Number'})
    )

    Doctor_Location = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'})
    )

    EnteredBy = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

