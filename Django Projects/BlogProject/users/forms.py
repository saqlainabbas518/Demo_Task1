from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
       email = forms.EmailField()
       fullname = forms.CharField()

       class Meta:
           model = User
           fields = ['fullname' , 'username' , 'email' , 'password1','password2']


class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()
        fullname = forms.CharField()

        class Meta:
            model = User
            fields = ['fullname', 'username' , 'email']


class ProfileUpdateForm(forms.ModelForm):
        city = forms.CharField()
        class Meta:
            model = Profile
            fields =['city' , 'image']