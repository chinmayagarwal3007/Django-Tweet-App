from django import forms
from .models import Tweet


class TweetForm(forms.ModeelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']