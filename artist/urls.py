from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from artist import views
from artist import view_artist
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
    path ('artist/artist_list/', views.artist_list, name='artist_list'),
    path ('artist/artist_detail/<int:pk>/', views.artist_detail, name='artist_detail'),
    path ('artist/', view_artist.ArtistList.as_view(queryset=artist.objects.all(), serializer_class=MyArtistSerializer), name='ArtistList')
]
 
# urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)