from rest_framework import serializers
from .models import *
from rest_framework import routers
router=routers.DefaultRouter

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields= '__all__'