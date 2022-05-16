from django import forms

from .models import Rdv


#from .models import Participant

class Enregistrement(forms.Form):
    email=forms.EmailField(label='Ton email')

class AjoutRdv(forms.ModelForm):
    class Meta:
        model=Rdv
        fields=['titre','description','lieu','date']




"""
class Enregistrement(forms.ModelForm):
    class Meta:
        model=Participant 
        fields=['email']
#useless because we don't use form.save()
"""

