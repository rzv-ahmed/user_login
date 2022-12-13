from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from login_app.models import User,User_Info

class User_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        
        model=User
        fields=('username','password','email')

class User_info_form(forms.ModelForm):
    class Meta():
        model=User_Info
        fields=('fb_id','image')