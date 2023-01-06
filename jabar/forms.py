from django import forms
from .models import *

class KotaForm(forms.ModelForm):

    class Meta:
        model = Kota
        fields = '__all__'

class PetaForm(forms.ModelForm):

    class Meta:
        model = Peta
        fields = '__all__'

