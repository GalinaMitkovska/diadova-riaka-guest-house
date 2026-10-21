from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

  class Meta:
    model = Booking
    fields = [
        'guest_name',
        'email',
        'phone',
        'number_of_guests',
        'check_in',
        'check_out',
        'room',
        'services',
    ]
    widgets = {
        'guest_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Вашето име'}
        ),
        'email': forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'example@domain.com',
            }
        ),
        'phone': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '+359...'}
        ),
        'number_of_guests': forms.NumberInput(
            attrs={'class': 'form-control'}
        ),
        'check_in': forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
        'check_out': forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
        'room': forms.Select(attrs={'class': 'form-control'}),
        'services': forms.CheckboxSelectMultiple(),
    }



class BookingEditForm(forms.ModelForm):

  class Meta:
    model = Booking
    fields = [
        'guest_name',
        'email',
        'phone',
        'number_of_guests',
        'check_in',
        'check_out',
        'services',
    ]
    widgets = {
        'guest_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'phone': forms.TextInput(attrs={'class': 'form-control'}),
        'number_of_guests': forms.NumberInput(attrs={'class': 'form-control'}),
        'check_in': forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
        'check_out': forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
        'services': forms.CheckboxSelectMultiple(),
    }


