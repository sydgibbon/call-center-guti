
from rest_framework import serializers  # import de serializers
from assets.models import Enclosuremodels, Enclosures

class GetEnclosuremodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosuremodels
        fields = ['id', 'name']

class GetEnclosuresCountSerializer(serializers.ModelSerializer):
    enclosuresCount = serializers.SerializerMethodField()
    
    def get_enclosuresCount(self,obj):
        return Enclosures.objects.count()
    
    class Meta:
        model = Enclosures
        fields = ['enclosuresCount']