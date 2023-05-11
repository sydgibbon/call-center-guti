
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import ItemsOperatingsystems, ItemsSoftwarelicenses, ItemsSoftwareversions, Manufacturers, Operatingsystems, Softwarecategories, Softwarelicenses, Softwares, Softwareversions
from assets.serializers import EntitiesSerializer, OperatingsystemsSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetSoftwarecategoriesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarecategories
        fields = ['id', 'name']

class SoftwarecategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarecategories
        fields = '__all__'

class SoftwarelicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarelicenses
        fields = '__all__'

class SoftwaresSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    softwarecategories = SoftwarecategoriesSerializer(required=False)

    class Meta:
        model = Softwares
        fields = '__all__'

class SoftwareversionsSerializer(serializers.ModelSerializer):

    entities = EntitiesSerializer(required=False)
    softwares = SoftwaresSerializer(required=False)
    states = StatesSerializer(required=False)
    operatingsystems = OperatingsystemsSerializer(required=False)
    class Meta:
        model = Softwareversions
        fields = '__all__'

# tables
class GetSoftwaresSerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()
    softwareversions = serializers.SerializerMethodField()
    operatingsystems = serializers.SerializerMethodField()
    softwarelicenses = serializers.SerializerMethodField()
    installations  = serializers.SerializerMethodField()


    def get_manufacturers(self, obj):
        manufacturers = Manufacturers.objects.filter(id=obj.manufacturers_id)
        if (manufacturers.count() > 0):
            return Manufacturers.objects.filter(id=obj.manufacturers_id)[0].name
        return None
    
    def get_softwareversions(self, obj):
        items_softwareversions = ItemsSoftwareversions.objects.filter(items_id=obj.id, itemtype='Software')
        if (items_softwareversions.count() > 0):
            return Softwareversions.objects.filter(id=items_softwareversions[0].softwareversions_id)[0].name
        return None
    
    def get_operatingsystems(self, obj):
        items_operatingsystems = ItemsOperatingsystems.objects.filter(items_id=obj.id, itemtype='Software')
        if (items_operatingsystems.count() > 0):
            return Operatingsystems.objects.filter(id=items_operatingsystems[0].operatingsystems_id)[0].name
        return None
    
    def get_softwarelicenses(self, obj):
        items_softwarelicenses = ItemsSoftwarelicenses.objects.filter(items_id=obj.id, itemtype='Software')
        if (items_softwarelicenses.count() > 0):
            return Softwarelicenses.objects.filter(id=items_softwarelicenses[0].softwarelicenses_id)[0].name
        return None
    
    def get_installations(self, obj):
        items_softwareversions = ItemsSoftwareversions.objects.filter(items_id=obj.id, itemtype='Software')
        if (items_softwareversions.count() > 0):
            return items_softwareversions.count()
        return None
    
    class Meta:
        model = Softwares
        fields = ['id', 'name', 'manufacturers', 'softwareversions', 'operatingsystems', 'installations', 'softwarelicenses']