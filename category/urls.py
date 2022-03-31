from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from category import views
from category import view_category
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path ('category/category_list/', views.category_list, name='category_list'),
    path ('category/category_detail/<int:pk>/', views.category_detail, name='category_detail'),
    path ('category/', view_category.CategoryList.as_view(queryset=category.objects.all(), 
                                                          serializer_class=MyCategorySerializer), 
                                                          name='CategoryList') 
]
 
urlpatterns += router.urls