from django import forms
from .modeld import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields =['text','photo']