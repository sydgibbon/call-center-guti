
from rest_framework import serializers  # import de serializers
from assets.models import Enclosuremodels

class GetEnclosuremodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosuremodels
        fields = ['id', 'name']