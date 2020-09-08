from rest_framework import serializers
from .models import Collage

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Collage
        fields = ('name','image','upload_date')