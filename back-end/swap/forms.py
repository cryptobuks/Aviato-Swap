from attr import fields
from django import forms
from matplotlib import widgets
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from email.mime.multipart import MIMEMultipart as main
from email.mime import text
from random import randint
import smtplib
import re

    

class SignUp(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class' : 'username', 'name' : 'username',
            'type' : 'text', 'required' : '', 'placeholder' : 'Your username',
            'onkeydown' : 'usernameValidation()'
        })
        self.fields['email'].widget.attrs.update({
            'class' : 'email', 'name' : 'email',
            'type' : 'text', 'required' : '' , 'placeholder' : 'Your email',
            'onkeydown' : 'emailValidation()'
        })
        self.fields['password1'].widget.attrs.update({
            'class' : 'password1', 'name':'password1',
            'type':'password', 'required' : '' , 'placeholder' : 'password',
            'onkeydown' : 'passwod1Validation()'
        })
        self.fields['password2'].widget.attrs.update({
            'class' : 'password2', 'name' : 'password2',
            'type' : 'password' , 'required' : '' , 'placeholder' : 'password confirmation',
            'onkeydown' : 'password2Validation()'
        })

    class Meta:
        model = User
        fields = ('username' ,'email', 'password1', 'password2')

    def clean_email(self):
        # pattern = r'^[a-z]+(?:(?:\.[a-z]+)+\d*|(?:_[a-z]+)+(?:\.\d+)?)?@(?!.*\.\.)[^\W_][a-z\d.]+[a-z\d]{2}$'
        pattern = r'\w*'
        result = re.match(pattern, self.cleaned_data.get('email'))
        if not bool(result):
            raise forms.ValidationError('email is invalid')
        return self.cleaned_data.get('email')


class login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={                                                                                                                                                                                                                                                                                                                                     
            'class' : 'username_login',
            'placeholder' : 'Your Username'
        }
    ))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'password',
            'placeholder' : 'Password'
        }
    ))


class UploadProfilePic(forms.Form):
    picture = forms.ImageField(widget=forms.FileInput(
        attrs={
            'id' : 'upload', 'name' : 'upload', 'type' : 'file'
        }
    ))

    def clean_picture(self):
        pic = self.cleaned_data.get('picture',0)
        try:
            val = pic.split('.')[-1]
        except AttributeError:
            raise forms.ValidationError('Firest off, please insert your picture')

        if val not in ['jpeg','jpg','jfif','pic']:
            raise forms.ValidationError(f'{val} is NOT good forms')

        return self.cleaned_data.get('picture')


