from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Cartridgeitems, CartridgeitemsPrintermodels, Cartridgeitemtypes, Cartridges, Locations, Manufacturers
from assets.printers.serializers import PrintersSerializer
from assets.generics.serializers import EntitiesSerializer
from assets.users.serializers import UsersSerializer

class GetCartridgeitemtypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartridgeitemtypes
        fields = ['id', 'name']

class GetCartridgeItemsSerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    cartridgeitemtypes = serializers.SerializerMethodField()

    def get_manufacturers(self, obj):
        manufacturers = Manufacturers.objects.filter(id=obj.manufacturers_id)
        if (manufacturers.count() > 0):
            return Manufacturers.objects.filter(id=obj.manufacturers_id)[0].name
        return None
                
    def get_locations(self, obj):
        locations = Locations.objects.filter(id=obj.locations_id)
        if (locations.count() > 0):
            return Locations.objects.filter(id=obj.locations_id)[0].name
        return None
    
    def get_cartridgeitemtypes(self, obj):
        cartridgeitemtypes = Cartridgeitemtypes.objects.filter(id=obj.cartridgeitemtypes_id)
        if (cartridgeitemtypes.count() > 0):
            return Cartridgeitemtypes.objects.filter(id=obj.cartridgeitemtypes_id)[0].name
        return None
    class Meta:
        model = Cartridgeitems
        fields = ['id', 'name' , 'ref', 'manufacturers' , 'locations', 'cartridgeitemtypes']

class CartridgeitemsPrintermodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartridgeitemsPrintermodels
        fields = '__all__'

class CartridgeitemtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartridgeitemtypes
        fields = '__all__'

class CartridgeitemsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    cartridgeitemtypes = CartridgeitemtypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)

    class Meta:
        model = Cartridgeitems
        fields = '__all__'

class CartridgesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    cartridgeitems = CartridgeitemsSerializer(required=False)
    printers = PrintersSerializer(required=False)

    class Meta:
        model = Cartridges
        fields = '__all__'