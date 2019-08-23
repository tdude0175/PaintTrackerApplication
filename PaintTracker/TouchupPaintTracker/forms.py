from django import forms
from .models import TouchUpPaint

class TouchUpForm(forms.ModelForm):
    class Meta:
        model = TouchUpPaint
        exclude = ['in_use','is_in_possession']