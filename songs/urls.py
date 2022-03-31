from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from songs import views
from songs import view_songs
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('song/song_list/', views.song_list, name='song_list'),
    path ('song/song_detail/<int:pk>/', views.song_detail, name='song_detail'),
    path ('song/', view_songs.SongList.as_view(queryset=song.objects.all(), 
                                    serializer_class=MySongSerializer), name='SongList')
]
 
urlpatterns += router.urls 