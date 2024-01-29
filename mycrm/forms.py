from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import NewFile
from django.contrib.admin import widgets

class SignUpForm(UserCreationForm):
    Name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model= User
        fields=('Name', 'email', 'username', 'password1', 'password2')

class addRecord(forms.ModelForm):

    class Meta:
        model = NewFile
        fields = ['name', 'upload', 'description']
        labels = {'Name of file': '', 'Select a file (max. 42 MB)': ''}
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}

class searchRecord(forms.ModelForm):
    class Meta:
        model = NewFile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = NewFile.objects.all()
