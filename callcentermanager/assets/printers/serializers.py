from rest_framework import serializers  # import de serializers
from assets.models import Printers, Printermodels, Printertypes

class GetPrintersSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printers
        fields = ['id', 'name']

class GetPrintermodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printermodels
        fields = ['id', 'name']
class GetPrintertypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printertypes
        fields = ['id', 'name']