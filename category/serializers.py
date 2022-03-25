from rest_framework import serializers
from .models import category

class MyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category  
        fields = [
                    'id_category',
                    'category_name', 
                ]