from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from root import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('root/',RootList.as_view(queryset=root.objects.all(), serializer_class=MyRootSerializer), name='RootList'),
    path ('root/<int:pk>/',RootDetail.as_view(queryset=root.objects.all(), serializer_class=MyRootSerializer), name='RootDetail')
]
 
urlpatterns += router.urls 