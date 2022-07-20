from django import forms
from django.db.models import fields 
from .models import signupform,userform

class signup(forms.ModelForm):
    class Meta:
        model=signupform
        fields='__all__'

class userformdata(forms.ModelForm):
    class Meta:
        model=userform
        fields='__all__'
