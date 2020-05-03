from django.contrib import admin
from django.urls import path, include
from tweets.views import Home, Tweet_details_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('tweet/<int:tweet_id>',Tweet_details_view),
]
