from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from root import views
from root import view_root
from .views import *

router = routers.DefaultRouter()
 
urlpatterns = [
    path ('root/root_list/', views.root_list, name='root_list'),
    path ('root/root_detail/<int:pk>/', views.root_detail, name='root_detail'),
    path ('root/',view_root.RootList.as_view(queryset=root.objects.all(), serializer_class=MyRootSerializer), name='RootList')
    
]
 
urlpatterns += router.urls 