
from rest_framework import serializers  # import de serializers
from assets.models import Pdutypes, Pdumodels, Pdus

class GetPdutypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdutypes
        fields = ['id', 'name']

class GetPdumodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdumodels
        fields = ['id', 'name']

class GetPdusCountSerializer(serializers.ModelSerializer):
    pdusCount = serializers.SerializerMethodField()
    
    def get_pdusCount(self,obj):
        return Pdus.objects.count()
    
    class Meta:
        model = Pdus
        fields = ['pdusCount']