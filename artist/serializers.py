from rest_framework import serializers
from .models import artist

class MyArtistSerializer(serializers.ModelSerializer):
    foto_artist = serializers.SerializerMethodField()
    
    class Meta:
        model = artist  
        fields = [
                    'id_artist',
                    'code_artist', 
                    'artist_name', 
                    'aliasname1', 
                    'aliasname2', 
                    'aliasname3',
                    'foto_artist',
                ]