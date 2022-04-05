from django import forms
from base.models import Geoinfo

class GeoinfoForm(forms.ModelForm):
    class Meta:
        model=Geoinfo
        fields = ['list_size']