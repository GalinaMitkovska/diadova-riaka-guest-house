from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):

  class Meta:
    model = Service
    fields = ['service_type', 'name', 'description']
    widgets = {
        'service_type': forms.Select(attrs={'class': 'form-control'}),
        'name': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'напр. Разходка с коне',
            }
        ),
        'description': forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Описание...',
            }
        ),
        'price': forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': '0.00'}
        ),
        
    }