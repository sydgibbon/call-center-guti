
from rest_framework import serializers  # import de serializers
from assets.models import Manufacturers

class GetManufacturersSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields = ['id', 'name']

class ManufacturersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields = '__all__'