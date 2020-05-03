from django.shortcuts import render
from django.http import HttpResponse
from tweets.models import Tweet

def Home(requests, *args, **kwargs):
    return HttpResponse('oi')

def Tweet_details_view(requests, tweet_id, *args, **kwargs):
    obj = Tweet.objects.get(id=tweet_id)
    return HttpResponse(f'Id {tweet_id}- {obj.content}')
