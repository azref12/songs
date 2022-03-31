from logging import root
from rest_framework import serializers
from .models import root

class MyRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = root  
        fields = [
                    'id_root',
                    'paths',    
                ]