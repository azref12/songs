from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from category import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('category/', CategoryList.as_view(queryset=category.objects.all(), serializer_class=MyCategorySerializer), name='CategoryList'),
    path ('category/<int:pk>/', CategoryDetail.as_view(queryset=category.objects.all(), serializer_class=MyCategorySerializer), name='CategoryDetail')
]
 
urlpatterns += router.urls