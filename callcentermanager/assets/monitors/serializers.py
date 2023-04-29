
from rest_framework import serializers  # import de serializers
from assets.models import Monitormodels, Monitortypes
class GetMonitortypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitortypes
        fields = ['id', 'name']

class GetMonitormodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitormodels
        fields = ['id', 'name']