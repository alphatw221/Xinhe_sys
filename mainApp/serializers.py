from rest_framework import serializers
from .models import *


class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class  WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Worker
        fields='__all__'

class  SquadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Squad
        fields='__all__'

class  WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Warehouse
        fields='__all__'
        
