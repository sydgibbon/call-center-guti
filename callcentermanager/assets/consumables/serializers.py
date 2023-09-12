from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Consumableitems, Consumableitemtypes, Consumables, Locations, Manufacturers
from assets.generics.serializers import EntitiesSerializer
from assets.users.serializers import UsersSerializer

class GetConsumableitemtypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumableitemtypes
        fields = ['id', 'name']

class ConsumablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumables
        fields = '__all__'

class ConsumableitemtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumableitemtypes
        fields = '__all__'

class ConsumableitemsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    consumableitemtypes = ConsumableitemtypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)

    class Meta:
        model = Consumableitems
        fields = '__all__'

class GetConsumableitemsSerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    consumableitemtypes = serializers.SerializerMethodField()

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
    
    def get_consumableitemtypes(self, obj):  
        consumableitemtypes = Consumableitemtypes.objects.filter(id=obj.consumableitemtypes_id)
        if (consumableitemtypes.count() > 0):
            return Consumableitemtypes.objects.filter(id=obj.consumableitemtypes_id)[0].name
        return None
    class Meta:
        model = Consumableitems
        fields = ['id', 'name' , 'ref', 'manufacturers', 'locations', 'consumableitemtypes']

class GetConsumableitemsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumableitems
        fields = ['id', 'name']

class GetConsumableitemsByIdSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Consumableitems
        fields = ['id', 'name', 'locations', 'consumableitemtypes', 'ref', 'users_tech', 'manufacturers', 'groups_tech', 'otherserial', 'comment', 'alarm_threshold', 'pictures', 'stock_target']

    def __init__(self, *args, **kwargs):
        item_id = kwargs.pop('item_id', None)
        super().__init__(*args, **kwargs)

        if item_id is not None:
            try:
                instance = Consumableitems.objects.get(id=item_id)
                self.instance = instance
            except Consumableitems.DoesNotExist:
                pass

class CreateConsumableItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumableitems
        fields = '__all__'