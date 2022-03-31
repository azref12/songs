from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from genre import views
from genre import view_genre
from .views import *
 
router = routers.DefaultRouter()

urlpatterns = [
    path ('genre/genre_list/', views.genre_list, name='genre_list'),
    path ('genre/genre_detail/<int:pk>/', views.genre_detail, name='genre_detail'),
    path ('genre/', view_genre.GenreList.as_view(queryset=genre.objects.all(), serializer_class=MyGenreSerializer), name='GenreList')
]
 
urlpatterns += router.urls 