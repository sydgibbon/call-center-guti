
from rest_framework import serializers  # import de serializers
from assets.models import Networks, Networkequipments

class GetNetworksSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networks
        fields = ['id', 'name']

class GetNetworkequipmentsCountSerializer(serializers.ModelSerializer):
    networkequipmentsCount = serializers.SerializerMethodField()
    
    def get_networkequipmentsCount(self,obj):
        return Networkequipments.objects.count()
    
    class Meta:
        model = Networkequipments
        fields = ['networkequipmentsCount']

class GetNetworkequipmentsCountByManufacturersSerializer(serializers.Serializer):
    manufacturers = serializers.CharField(source='manufacturers_id__name')
    count = serializers.IntegerField()
class NetworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networks
        fields = '__all__'
