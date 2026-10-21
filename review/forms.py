from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

  class Meta:
    model = Review
    fields = ['name', 'rating', 'comment']
    widgets = {
        'name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Вашето име'}
        ),
        'rating': forms.Select(attrs={'class': 'form-control'}),
        'comment': forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Напишете отзив...',
            }
        ),
    }