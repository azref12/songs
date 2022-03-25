from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from genre import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('genre/', GenreList.as_view(queryset=genre.objects.all(), serializer_class=MyGenreSerializer), name='GenreList'),
    path ('genre/<int:pk>/', GenreDetail.as_view(queryset=genre.objects.all(), serializer_class=MyGenreSerializer), name='GenreDetail')
]
 
urlpatterns += router.urls 