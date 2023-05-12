
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

class CountByManufacturerSerializer(serializers.Serializer):

    manufacturers_id = serializers.CharField()
    count = serializers.IntegerField()

class CountByStateSerializer(serializers.Serializer):

    states_id = serializers.CharField()
    count = serializers.IntegerField()

class CountByComputertypeSerializer(serializers.Serializer):

    computertypes_id = serializers.CharField()
    count = serializers.IntegerField()