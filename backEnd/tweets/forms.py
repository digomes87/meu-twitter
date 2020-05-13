from django import forms

from tweets.models import Tweet

MAX_TWEET_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
    
    def cleanContent():
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("Much Long !!!!")
        return content
