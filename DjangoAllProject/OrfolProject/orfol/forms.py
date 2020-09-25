from django import forms
from django.contrib.auth.models import User
from .models import Report ,SubCategory,ReportImage
from django.utils import  timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe
# from datetimepicker.widgets import DateTimePicker
# from django.utils.datetimepicker.widgets import DateTimePicker


# label='username',widget=forms.TextInput(attrs={'placeholder': 'username'})
CHOICES = [('L','Lost'),('F','Found')]
class createpost(forms.ModelForm):
    type = forms.ChoiceField(label='Select report type', required=True, initial='Lost',
                             widget=forms.RadioSelect(attrs={'class': 'radio_class', 'id': 'radio_id'}),
                             choices=(('L', 'Lost'), ('F', 'Found'),))
    #user_id = forms.CharField()
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter Title'}))
    reward = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter Reward'}))
    location = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter Location'}))
    date_occurrence = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_created = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    status = forms.CharField(max_length=50)
    description = forms.Textarea()
    class Meta:
        model = Report
        fields = ['title','category','subcategory_id','type','reward','location','date_occurrence','date_created','status','description']
        # fields = ['user_id','type','title','reward','location','date_occurrence','date_created','status','description']




class ImageForm(forms.ModelForm):
    imagepath = forms.ImageField(label='Image')
    class Meta:
        model = ReportImage
        fields = ['imagepath']