from django import forms
from django.forms import ModelForm
from todo.models import *


class ContactForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Title'}))
    description = forms.CharField(widget=forms.Textarea)


class FeedbackForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Your name'}))
