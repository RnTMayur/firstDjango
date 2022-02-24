from attr import field
from django import forms
from .models import comapny

class sampleform(forms.ModelForm):
    class meta:
        model=comapny
        fields="__all__"
        