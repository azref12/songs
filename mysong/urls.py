from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artist.urls')),
    path('', include('category.urls')),
    path('', include('genre.urls')),
    path('', include('root.urls')),
    path('', include('songs.urls')),
    path('', include('youtube.urls'))
]