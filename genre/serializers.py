from rest_framework import serializers
from .models import genre

class MyGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = genre  
        fields = [ 
                    'id_genre',
                    'genre',     
                ]