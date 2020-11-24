from django import forms
from .models import PrayPlay

class PrayPlayForm(forms.ModelForm):
    class Meta:
        model = PrayPlay
        fields = [
            'text',
            'type',
        ]
