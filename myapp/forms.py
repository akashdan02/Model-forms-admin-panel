from django import forms
from django.forms import fields
from .models import Application_settings

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application_settings
        fields = "__all__"