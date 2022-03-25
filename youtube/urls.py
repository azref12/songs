from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from youtube import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('youtube/',YoutubeList.as_view(queryset=youtube.objects.all(), serializer_class=MyYoutubeSerializer), name='YoutubeList'),
    path ('youtube/<int:pk>/',YoutubeDetail.as_view(queryset=youtube.objects.all(), serializer_class=MyYoutubeSerializer), name='YoutubeDetail')
]
 
urlpatterns += router.urls 