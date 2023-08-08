from django import forms
from .models import*


class regform(forms.ModelForm):
    class Meta:
        model=registermodel
        fields=('name1','addr','dob','age','phone1','email1','pass1')
        widigets={
                'name1':forms.TextInput(attrs={'class':'form-control'}),
                'addr':forms.TextInput(attrs={'class':'form-control'}),
                'dob':forms.TextInput(attrs={'class':'form-control'}),
                'age':forms.TextInput(attrs={'class':'form-control'}),
                'phone1':forms.TextInput(attrs={'class':'form-control'}),
                'email1':forms.TextInput(attrs={'class':'form-control'}),
                'pass1':forms.TextInput(attrs={'class':'form-control'}),
        }