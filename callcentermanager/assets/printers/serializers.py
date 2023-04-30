from rest_framework import serializers  # import de serializers
from assets.models import Printermodels, Printertypes

class GetPrintermodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printermodels
        fields = ['id', 'name']
class GetPrintertypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printertypes
        fields = ['id', 'name']