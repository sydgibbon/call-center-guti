
from rest_framework import serializers  # import de serializers
from assets.models import Cabletypes, Cablestrands, Sockets, Socketmodels

class GetCabletypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabletypes
        fields = ['id', 'name']
        
class GetCablestrandsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cablestrands
        fields = ['id', 'name']
                      
class GetSocketsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sockets
        fields = ['id', 'name']

class GetSocketmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socketmodels
        fields = ['id', 'name']
