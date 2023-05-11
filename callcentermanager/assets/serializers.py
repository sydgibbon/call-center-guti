from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
# import de todos los callcenterdata, proximamente se mueve a assets
from assets.models import *
from django.contrib.auth import authenticate
from assets.networks.serializers import NetworksSerializer
from assets.printers.serializers import PrintersSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer
from assistance import models as assistanceModels, serializers as assistanceSerializers

#Login Auth


class OperatingsystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operatingsystems
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs

#Model serializers
#         

class DevicemotherboardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicemotherboards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicenetworkcardmodelsSerializer(serializers.ModelSerializer):
    class Meta:  # Clase meta para configurar el serializer
        model = Devicenetworkcardmodels  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicenetworkcardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicenetworkcards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicepcimodelsSerializer(serializers.ModelSerializer):   
    class Meta:  # Clase meta para configurar el serializer
        model = Devicepcimodels  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicepcisSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicepcis  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicepowersuppliesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicepowersupplies  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicepowersupplymodelsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicepowersupplymodels  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DeviceprocessormodelsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Deviceprocessormodels  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DeviceprocessorsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Deviceprocessors  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicesensormodelsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicesensormodels  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicesensorsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicesensors  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicesensortypesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicesensortypes  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicesoundcardmodelsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicesoundcardmodels  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicesoundcardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicesoundcards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicebatteriesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicebatteries  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicecamerasSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicecameras  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicecamerasImageformatsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicecamerasImageformats  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicecamerasImageresolutionsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicecamerasImageresolutions  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicecasesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicecases  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicecontrolsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicecontrols  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicedrivesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicedrives  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicefirmwaresSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicefirmwares  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicegenericsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicegenerics  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicegraphiccardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicegraphiccards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDeviceharddrivesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDeviceharddrives  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicememoriesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicememories  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicemotherboardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicemotherboards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicenetworkcardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicenetworkcards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicepcisSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicepcis  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicepowersuppliesSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicepowersupplies  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDeviceprocessorsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDeviceprocessors  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicesensorsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicesensors  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicesimcardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicesimcards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class ItemsDevicesoundcardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = ItemsDevicesoundcards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model

# Nata (PhoneTypes hasta DeviceMotherboardModels)

# Este tiene problemitas (no se le puede agregar con add)
class RackmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rackmodels
        fields = '__all__'


class RacktypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racktypes
        fields = '__all__'


class ItemsRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsRacks
        fields = '__all__'


# Este también tiene problemitas (no se le puede agregar con add)

class DevicesimcardtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcardtypes
        fields = '__all__'

class DevicebatteriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicebatteries
        fields = '__all__'


class DevicebatterymodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicebatterymodels
        fields = '__all__'


class DevicebatterytypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicebatterytypes
        fields = '__all__'


class DevicecameramodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicecameramodels
        fields = '__all__'


class DevicecamerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicecameras
        fields = '__all__'


class DevicecasemodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicecasemodels
        fields = '__all__'


class DevicecasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicecases
        fields = '__all__'


class DevicecasetypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicecasetypes
        fields = '__all__'


class DevicecontrolmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicecontrolmodels
        fields = '__all__'


class DevicecontrolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicecontrols
        fields = '__all__'


class DevicedrivemodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicedrivemodels
        fields = '__all__'


class DevicedrivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicedrives
        fields = '__all__'


class DevicefirmwaremodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicefirmwaremodels
        fields = '__all__'


class DevicefirmwaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicefirmwares
        fields = '__all__'


class DevicefirmwaretypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicefirmwaretypes
        fields = '__all__'


class DevicegenericmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicegenericmodels
        fields = '__all__'


class DevicegenericsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicegenerics
        fields = '__all__'


class DevicegenerictypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicegenerictypes
        fields = '__all__'


class DevicegraphiccardmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicegraphiccardmodels
        fields = '__all__'


class DevicegraphiccardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicegraphiccards
        fields = '__all__'


class DeviceharddrivemodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deviceharddrivemodels
        fields = '__all__'


class DeviceharddrivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deviceharddrives
        fields = '__all__'


class DevicememoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicememories
        fields = '__all__'


class DevicememorymodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicememorymodels
        fields = '__all__'


class DevicememorytypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicememorytypes
        fields = '__all__'


class DevicemotherboardmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicemotherboardmodels
        fields = '__all__'
# ---------------------------

class UnmanagedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unmanageds
        fields = '__all__'

class DevicesimcardtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcardtypes
        fields = '__all__'

class SoftwarecategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarecategories
        fields = '__all__'

class SoftwarelicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarelicenses
        fields = '__all__'

class EntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        fields = '__all__'

class SnmpcredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snmpcredentials
        fields = '__all__'


class DcroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcrooms
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

class RacksSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    racktypes = RacktypesSerializer(required=False)
    rackmodels = RackmodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    dcrooms = DcroomsSerializer(required=False)

    class Meta:
        model = Racks
        fields = '__all__'

class UnmanagedsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    networks = NetworksSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Unmanageds
        fields = '__all__'

class DevicesimcardsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    devicesimcardtypes = DevicesimcardtypesSerializer(required=False)

    class Meta:
        model = Devicesimcards
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
class GetDevicesimcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcards
        fields = ['id']


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

class GetRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racks
        fields = ['id', 'name']
