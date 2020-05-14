import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from tweets.models import Tweet
from .forms import TweetForm


def Home(requests, *args, **kwargs):
    return render(requests, "pages/home.html", context={}, status=200)

def tweet_create_view(requests, *args, **kwargs):
    form = TweetForm(requests.POST or None)
    next_url = requests.POST.get("next") or None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = TweetForm()
    return render(requests, 'components/forms.html', context={"form": form})

def tweet_list_view(requests, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list =[{"id": x.id, "content": x.content, "likes": random.randint(0, 1200)} for x in qs]
    data = {
        "isUser": False,
        "response": tweet_list
    }
    return JsonResponse(data)

def Tweet_details_view(requests, tweet_id, *args, **kwargs):
    """
        REST API VIEW  return json data
    """
    data = {
        "id":tweet_id,
    }
    status =200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
    

    return JsonResponse(data, status=status)
