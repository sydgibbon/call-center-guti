from rest_framework import serializers  # import de serializers
from assets.models import Peripherals, Peripheraltypes, Peripheralmodels

class GetPeripheralsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripherals
        fields = ['id', 'name']
        
class GetPeripheraltypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheraltypes
        fields = ['id', 'name']
class GetPeripheralmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheralmodels
        fields = ['id', 'name']

class GetPeripheralsCountSerializer(serializers.ModelSerializer):
    peripheralsCount = serializers.SerializerMethodField()
    
    def get_peripheralsCount(self,obj):
        return Peripherals.objects.count()
    
    class Meta:
        model = Peripherals
        fields = ['peripheralsCount']