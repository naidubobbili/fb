from django import forms

from .models import detail

class detailform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=detail
        fields=['username','password']
