from rest_framework import serializers  # import de serializers
from assets.models import Manufacturers

class GetManufacturersNameSerializer(serializers.ModelSerializer):
    model = Manufacturers
    fields = ('id', 'name')