from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from songs import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('song/', SongList.as_view(queryset=song.objects.all(), 
                                    serializer_class=MySongSerializer), name='SongList'),
    path ('song/<int:pk>/', SongDetail.as_view(queryset=song.objects.all(), 
                                               serializer_class=MySongSerializer), name='SongDetail')
]
 
urlpatterns += router.urls 