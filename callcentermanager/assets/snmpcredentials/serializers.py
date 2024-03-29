
from rest_framework import serializers  # import de serializers
from assets.models import Snmpcredentials

class GetSnmpcredentialsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snmpcredentials
        fields = ['id', 'name']

class SnmpcredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snmpcredentials
        fields = '__all__'
