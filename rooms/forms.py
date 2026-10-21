from django import forms
from .models import Room


class RoomForm(forms.ModelForm):

  class Meta:
    model = Room
    fields = ['room_type', 'capacity', 'description']
    widgets = {
        'room_type': forms.Select(attrs={'class': 'form-control'}),
        'capacity': forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Брой гости'}
        ),

        'description': forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Описание...',
            }
        ),
    }
