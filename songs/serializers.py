from numpy import roots
from rest_framework import serializers
from .models import song
from artist.serializers import *
from category.serializers import *
from genre.serializers import *
from root.serializers import *
from songs.serializers import *
from youtube.serializers import *

class MySongSerializer(serializers.ModelSerializer):
    ytb = MyYoutubeSerializer(read_only=True, many=True)
    artists = MyArtistSerializer(read_only=True, many=True)
    categories = MyCategorySerializer(read_only=True, many=True)
    genres = MyGenreSerializer(read_only=True, many=True)
    roots = MyRootSerializer(read_only=True, many=True)
    
    class Meta:
        model = song  
        fields = "__all__"