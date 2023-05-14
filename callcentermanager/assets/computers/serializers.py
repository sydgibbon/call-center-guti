
from rest_framework import serializers  # import de serializers
from assets.models import Computers, Computermodels, Computertypes

class GetComputersSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = ['id', 'name']

class GetComputertypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computertypes
        fields = ['id', 'name']

class GetComputermodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computermodels
        fields = ['id', 'name']

class GetComputersCountSerializer(serializers.ModelSerializer):
    computersCount = serializers.SerializerMethodField()
    
    def get_computersCount(self,obj):
        return Computers.objects.count()
    
    class Meta:
        model = Computers
        fields = ['computersCount']

class GetComputersCountByManufacturersSerializer(serializers.Serializer):
    manufacturers = serializers.CharField(source='manufacturers_id__name')
    count = serializers.IntegerField()

class GetComputersCountByStatesSerializer(serializers.Serializer):

    states = serializers.CharField(source='states_id__name')
    count = serializers.IntegerField()

class GetComputersCountByComputertypesSerializer(serializers.Serializer):

    computertypes = serializers.CharField(source='computertypes_id__name')
    count = serializers.IntegerField()