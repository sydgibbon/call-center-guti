
from rest_framework import serializers
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Devicesimcards, Devicesimcardtypes, ItemsDevicesimcards, Lines
from assets.generics.serializers import EntitiesSerializer

class GetDevicesimcardsSelectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='designation')
    class Meta:
        model = Devicesimcards
        fields = ['id', 'name']

class GetLinesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lines
        fields = ['id', 'name']

class ItemsDevicesimcardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicesimcards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model

class DevicesimcardtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcardtypes
        fields = '__all__'

class GetDevicesimcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcards
        fields = ['id']

class DevicesimcardtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcardtypes
        fields = '__all__'

class DevicesimcardsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    devicesimcardtypes = DevicesimcardtypesSerializer(required=False)

    class Meta:
        model = Devicesimcards
        fields = '__all__'

class GetDevicesimcardsListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='designation')
    class Meta:
        model = Devicesimcards
        fields = ['id', 'name']