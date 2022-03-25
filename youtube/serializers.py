from rest_framework import serializers
from .models import youtube

class MyYoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = youtube  
        fields = [
                    'id_ytb',
                    'id_song',
                    'url',     
                ]