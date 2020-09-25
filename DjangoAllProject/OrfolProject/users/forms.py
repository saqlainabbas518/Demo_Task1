from django import forms
from django.contrib.auth.models import User
from django.utils import  timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'style': 'border:black', 'placeholder': 'username'}))
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'style': 'border:none', 'placeholder': 'email'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'border:none', 'placeholder': '+923330110001'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'border:none;', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'conifrm Password'}))

    def __init__(self, *args, **kwargs):
          super(UserRegisterForm, self).__init__(*args, **kwargs)

          for fieldname in ['username', 'password1', 'password2']:
              self.fields[fieldname].help_text = None
    class Meta:
          model = User
          fields = ['username' , 'email' ,'phone', 'password1' , 'password2']





class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['username'].label = 'Username'
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter password'})
        self.fields['password'].label = 'Password'


