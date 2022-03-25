from django.shortcuts import render

# Create your views here.
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
from .serializers import MyGenreSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import datetime
from rest_framework import generics

t = datetime.datetime.now()

if __name__ == "__main__":
    print(genre.objects.all())
    
class GenreList (generics.ListCreateAPIView) :
        queryset = genre.objects.all()
        serializer_class = MyGenreSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
        filterset_fields = ['id_genre','genre'] 
        ordering_fields = ['id_genre','genre']
        search_fields = ['id_genre','genre'] 
        
class GenreDetail (generics.RetrieveUpdateDestroyAPIView) :
        queryset = genre.objects.all() 
        serializer_class = MyGenreSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
        filterset_fields = ['id_genre','genre'] 
        ordering_fields = ['id_genre','genre']
        search_fields = ['id_genre','genre']
        

