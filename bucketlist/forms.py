from django import forms
from .models import User, PrayPlay

#class UserForm(forms.ModelForm):
    #class Meta:
        #model = User
        #fields = [
            #'name',
            #'username',
           # 'phone_number',
           # 'email',
           # 'address_1',
           # 'address_2',
            # 'city',
            # 'state',
            # 'zip_code',
            
       # ]
class PrayPlayForm(forms.ModelForm):
    class Meta:
        model = PrayPlay
        fields = [
            'text',
            'type',
        ]
