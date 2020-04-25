from django.contrib.auth.models import User
from django import forms
from django.forms import CharField, Form, PasswordInput ,TextInput
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import Profile


class UserRegisterationForm(UserCreationForm):
    username = forms.CharField(max_length=30 , widget= forms.TextInput(attrs={'style': 'border:black', 'placeholder': 'username'}))
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'style': 'border:none', 'placeholder': 'email'}))
    contact_no = forms.IntegerField(widget = forms.TextInput(attrs={'style':'border:none', 'placeholder' :'+923330110001'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'style': 'border:none;', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'conifrm Password'}))


    class Meta:
        model = User
        fields = ['username' ,'email' ,'contact_no' ,  'password1' , 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2' : None,
        }


class newpost(forms.Form):
    title = forms.CharField(max_length=30 , widget= forms.TextInput(attrs={'style': 'border:blue', 'placeholder': 'Title'}))

    class Meta:
        fields = ['title' , 'content']


class UserUpdateForm(forms.ModelForm):
    contact_no = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'email','contact_no']


class UpdateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']