from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from .models import Participant

class Enregistrement(forms.Form):
    email=forms.EmailField(label='Ton email')

class InscriptionForm(UserCreationForm):
    email= forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        



"""
class Enregistrement(forms.ModelForm):
    class Meta:
        model=Participant 
        fields=['email']
#useless because we don't use form.save()
"""

