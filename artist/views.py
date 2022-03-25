from functools import reduce
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import MyArtistSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import datetime
from rest_framework import generics
from functools import reduce
import operator
from django.db.models import Q

t = datetime.datetime.now()

if __name__ == "__main__":
    print(artist.objects.all())
    
class ArtistList (generics.ListCreateAPIView) :
        queryset = artist.objects.all() 
        serializer_class = MyArtistSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['id_artist','code_artist','artist_name','aliasname1','aliasname2','aliasname3'] 
        ordering_fields = ['id_artist','code_artist']
        search_fields = ['id_artist','code_artist','artist_name','aliasname1','aliasname2','aliasname3']
        
        # def get_queryset(self) :
        #     name = self.request.query_params.get('query', None)
        #     if not name : 
        #             return self.queryset
        #     name_seq = name.split(' ')
        #     name_qs = reduce(operator.and_,
        #                      (Q(artist_name__icontains=x) | Q (aliasname1__icontains=x) | Q (aliasname2__icontains=x) | Q (aliasname3__icontains=x)
        #                       for x in name_seq))
        #     return self.queryset.filter(name_qs)
               
class ArtistDetail (generics.RetrieveUpdateDestroyAPIView) :
        queryset = artist.objects.all() 
        serializer_class = MyArtistSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['id_artist','code_artist','artist_name','aliasname1','aliasname2','aliasname3'] 
        ordering_fields = ['id_artist','code_artist']
        search_fields = ['id_artist','code_artist','artist_name','aliasname1','aliasname2','aliasname3']
        

