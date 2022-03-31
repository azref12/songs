#from rest_framework.response import Response
#from rest_framework.authtoken.views import ObtainAuthToken
#from django.shortcuts import render
#from rest_framework.renderers import JSONRenderer
#from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from inspect import isfunction
from msilib.schema import AppId
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import MySongSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
import datetime
from pathlib import Path
from decouple import Config ,RepositoryEnv, Csv
import os
from re import X
from django.db import DatabaseError, transaction
from django.db.utils import IntegrityError

t = datetime.datetime.now() 

if __name__ == "__main__":
    print(song.objects.all())

mastermodel = isfunction
masterserialzer = isfunction

@csrf_exempt
@api_view(["GET","POST"])
@permission_classes([AllowAny])

def song_list (request):    
        try:
                cek = request.GET['return_url']
                if  cek == '/song_list':
                        mastermodel = song
                        masterserialzer = MySongSerializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)

        if request.method == 'GET':
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer(localmodel, many=True)
                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201)

        if request.method == 'POST':
                localrequest = JSONParser().parse(request)
                localserializer = masterserialzer(data=localrequest)
                if localserializer.is_valid():
                        try:
                                res = song.objects.filter(id_songs__contains=y).last()
                                x = int (res.id_songs)+1
                                print(x)
                        except :
                                x=1
                                
                        y = t. x
                        with transaction.atomic():
                                sid = transaction.savepoint()
                                try:

                                        if localserializer.is_valid():
                                                songs = song.objects.filter(id_songs = localrequest['id_songs']).first()
                                                artists = song.objects.filter(id_artist = localrequest['id_artist']).first()
                                                categories = song.objects.filter(id_category = localrequest['id_category']).first()
                                                genres = song.objects.filter(id_genre = localrequest['id_genre']).first()
                                                roots = song.objects.filter(id_root = localrequest['id_root']).first()
                                                ytb = song.objects.filter(id_ytb = localrequest['id_ytb']).first()

                                                songSave = song ( 
                                                                id_songs = songs,
                                                                code_song=localserializer.data.get("code_song"),
                                                                title_song=localserializer.data.get("title_song"),
                                                                alias1=localserializer.data.get("alias1"),
                                                                alias2=localserializer.data.get("alias2"),
                                                                alias3=localserializer.data.get("alias3"),
                                                                paths=localserializer.data.get("paths"),
                                                                xvoc=localserializer.data.get("xvoc"),
                                                                voc=localserializer.data.get("voc"),
                                                                vol=localserializer.data.get("vol"),
                                                                foto=localserializer.data.get("foto"),
                                                                id_artist = artists,
                                                                id_category = categories,
                                                                id_genre = genres,
                                                                id_root = roots,
                                                                id_ytb = ytb
                                                        )
                                                songSave.save()
                                        transaction.savepoint_commit(sid)
                                except IntegrityError:
                                        transaction.savepoint_rollback(sid)

                                ModelMaster = song.objects.filter(id)
                                MasterSerializer = MySongSerializer(ModelMaster, many=True)
                                
                                formater = {
                                        "master": MasterSerializer.data

                                }
                            
                                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater},
                                    status=201)  

@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny]) 
def song_detail(request, pk):
        try:
                cek = request.GET['return_url']
                if  cek == '/song_detail':
                        mastermodel = song
                        masterserialzer = MySongSerializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)
        
        try:
                localmodel = mastermodel.objects.get(pk=pk)
        except mastermodel.DoesNotExist:
                return HttpResponse(status=404)

        if request.method == 'GET':
        
                localserializer = masterserialzer(localmodel)
                return JsonResponse(localserializer.data)
    
        elif request.method == 'PUT': 
                localrequest = JSONParser().parse(request) 
                localserializer = masterserialzer(localmodel, data=localrequest) 

                if localserializer.is_valid(): 
                
                        localserializer.save()  
                
                        localmodel = mastermodel.objects.all()
                        localserializer = masterserialzer(localmodel, many=True)

                        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                        status=201)
                return JsonResponse(localserializer.errors, status=400) 

        elif request.method == 'PATCH':
                localserializer = masterserialzer(localmodel, data={'status':0}, partial=True)
                if localserializer.is_valid():
                        localserializer.save()
                        return JsonResponse({'message': 'Success'}, status=200)
                else:
                        return JsonResponse(localserializer.errors, status=400)

        elif request.method == 'DELETE': 
                localmodel.delete() 
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer(localmodel, many=True)

        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201)        
