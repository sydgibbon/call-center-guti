
from rest_framework import serializers  # import de serializers
from assets.models import Monitormodels, Monitortypes, Monitors
class GetMonitortypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitortypes
        fields = ['id', 'name']

class GetMonitormodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitormodels
        fields = ['id', 'name']

class GetMonitorsCountSerializer(serializers.ModelSerializer):
    monitorsCount = serializers.SerializerMethodField()
    
    def get_monitorsCount(self,obj):
        return Monitors.objects.count()
    
    class Meta:
        model = Monitors
        fields = ['monitorsCount']