from django.db import models
from datetime import datetime
from django import forms
# Create your models here.

class detail(models.Model):

    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    #password = forms.CharField(max_length=32, widget=forms.PasswordInput)


    login_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username
