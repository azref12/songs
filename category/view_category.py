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
from .serializers import MyCategorySerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import datetime
from rest_framework import generics

t = datetime.datetime.now()

if __name__ == "__main__":
    print(category.objects.all())
    
class CategoryList (generics.ListCreateAPIView) :
        queryset = category.objects.all()
        serializer_class = MyCategorySerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
        filterset_fields = ['id_category','category_name'] 
        ordering_fields = ['id_category','category_name']
        search_fields = ['id_category','category_name']

        

