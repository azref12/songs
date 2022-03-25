from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import MySongSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import datetime
from rest_framework import generics

if __name__ == "__main__": 
    print(song.objects.all())
    
class SongList (generics.ListCreateAPIView) :
        queryset = root.objects.all()
        serializer_class = MySongSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
        filterset_fields = ['id_songs','code_song'] 
        ordering_fields = ['id_songs','code_song']
        search_fields = ['id_songs','code_song','title_song','alias1','alias2','alias3'] 
        
class SongDetail (generics.RetrieveUpdateDestroyAPIView) :
        queryset = root.objects.all() 
        serializer_class = MySongSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
        filterset_fields = ['id_songs','code_song'] 
        ordering_fields = ['id_songs','code_song']
        search_fields = ['id_songs','code_song','title_song','alias1','alias2','alias3']

