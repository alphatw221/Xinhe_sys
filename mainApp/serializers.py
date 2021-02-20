from rest_framework import serializers
from .models import *

class  WorkSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkSheet
        fields='__all__'
        
class WorkSheetProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkSheetProducts
        fields='__all__'


class  GetProductSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=GetProductSheet
        fields='__all__'
        
class GetProductSheetProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=GetProductSheetProducts
        fields='__all__'


class  UseProductSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=UseProductSheet
        fields='__all__'
        
class UseProductSheetProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UseProductSheetProducts
        fields='__all__'


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
        
