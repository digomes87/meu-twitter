from django.contrib import admin
from django.urls import path, include
from tweets.views import Home, Tweet_details_view, tweet_list_view, tweet_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('create-tweet', tweet_create_view),
    path('tweets/<int:tweet_id>',Tweet_details_view),
    path('tweets/', tweet_list_view),
]
