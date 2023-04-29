from rest_framework import serializers  # import de serializers
from assets.models import Printers, Printermodels, Printertypes

class GetPrintersSerializer(serializers.ModelSerializer):
    model = Printers
    fields = ('id', 'name')

class GetPrintermodelsSerializer(serializers.ModelSerializer):
    model = Printermodels
    fields = ('id', 'name')

class GetPrintertypesSerializer(serializers.ModelSerializer):
    model = Printertypes
    fields = ('id', 'name')