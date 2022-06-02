from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import comment, product

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        Email = forms.EmailField()
        fields = ['username', 'email', 'password1', 'password2']

class productInfo(forms.ModelForm):
    class Meta:
        models = product
        fields = ['title', 'image', 'image_1', 'image_2' 'ptype', 'pname', 'price', 'pdetails']

class userComment(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['uname', 'email', 'review']
        