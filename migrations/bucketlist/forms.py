from django import forms
from .models import User, Pray, Play

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'phone_number',
            'email',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'birthday',
        ]
class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = [
            'text',
        ]
        
class PrayForm(forms.ModelForm):
        class Meta:
        model = Pray
        fields = [
            'text',
        ]