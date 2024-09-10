from django import forms
from .models import Foodhouse, Foodhub

class FoodhouseCraeteForm(forms.ModelForm):
    class Meta:
        model = Foodhouse
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'city' : forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
            'postcode' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'social_media' : forms.TextInput(attrs={'class': 'form-control'}),
            'apps' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class FoodhubCraeteForm(forms.ModelForm):
    class Meta:
        model = Foodhub
        fields = '__all__'
