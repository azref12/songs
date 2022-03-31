from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from youtube import views
from youtube import view_ytb
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('youtube/youtube_list/', views.youtube_list, name='youtube_list'),
    path ('youtube/youtube_detail/<int:pk>/', views.youtube_detail, name='youtube_detail'),
    path ('youtube/', view_ytb.YoutubeList.as_view(queryset=youtube.objects.all(), serializer_class=MyYoutubeSerializer), name='YoutubeList')
]
 
urlpatterns += router.urls 