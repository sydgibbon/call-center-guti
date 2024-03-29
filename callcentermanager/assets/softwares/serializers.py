
from rest_framework import serializers  # import de serializers
from assets.models import Softwarecategories, Softwares, Softwarelicenses
from rest_framework import serializers
from assets.computers.serializers import OperatingsystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import ItemsOperatingsystems, ItemsSoftwarelicenses, ItemsSoftwareversions, Manufacturers, Operatingsystems, Softwarecategories, Softwarelicenses, Softwares, Softwareversions
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetSoftwarecategoriesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarecategories
        fields = ['id', 'name']

class GetSoftwaresCountSerializer(serializers.ModelSerializer):
    softwaresCount = serializers.SerializerMethodField()
    
    def get_softwaresCount(self,obj):
        return obj.count()
    
    class Meta:
        model = Softwares
        fields = ['softwaresCount']

class GetSoftwarelicensesCountSerializer(serializers.ModelSerializer):
    softwarelicensesCount = serializers.SerializerMethodField()
    
    def get_softwarelicensesCount(self,obj):
        return obj.count()
    
    class Meta:
        model = Softwarelicenses
        fields = ['softwarelicensesCount']
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

class GetSoftwaresListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwares
        fields = ['id', 'name']

class CreateSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwares
        fields = '__all__'

class GetSoftwaresByIdSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Softwares
        fields = ['id', 'name', 'is_helpdesk_visible', 'locations', 'manufacturers', 'users_tech', 'groups_tech', 'groups', 'users', 'comment','is_update', 'softwares', 'pictures', 'softwarecategories']

    def __init__(self, *args, **kwargs):
        item_id = kwargs.pop('item_id', None)
        super().__init__(*args, **kwargs)

        if item_id is not None:
            try:
                instance = Softwares.objects.get(id=item_id)
                self.instance = instance
            except Softwares.DoesNotExist:
                pass