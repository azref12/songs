from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from artist import views
from .views import *
from .customejwt import LogoutView, MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path ('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path ('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path ('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path ('logout/', LogoutView.as_view(), name='auth_logout'),
    path ('artist/', ArtistList.as_view(queryset=artist.objects.all(), serializer_class=MyArtistSerializer), name='ArtistList'),
    # path ('artist/search/', ArtistList.as_view(queryset=artist.objects.all(), serializer_class=MyArtistSerializer), name='ArtistList'),
    path ('artist/<int:pk>/', ArtistDetail.as_view(queryset=artist.objects.all(), serializer_class=MyArtistSerializer), name='ArtistDetail')
]
 
urlpatterns += router.urls