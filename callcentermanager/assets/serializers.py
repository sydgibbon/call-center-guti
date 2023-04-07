from rest_framework import serializers  # import de serializers
# import de todos los callcenterdata, proximamente se mueve a assets
from assets.models import *
from django.contrib.auth import authenticate
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

class AutoupdatesystemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autoupdatesystems
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Groups #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

        
class UsersSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Users #Especificar el nombre del Model
        fields = ['id', 'name']

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


class PhonetypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetypes
        fields = '__all__'


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
class ItemsEnclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsEnclosures
        fields = '__all__'


class EnclosuremodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosuremodels
        fields = '__all__'


class PdusPlugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdusPlugs
        fields = '__all__'


class CablestrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cablestrands
        fields = '__all__'


class CabletypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabletypes
        fields = '__all__'


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


class ConsumablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumables
        fields = '__all__'


class PdusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdus
        fields = '__all__'


class PdutypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdutypes
        fields = '__all__'


class PdumodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdumodels
        fields = '__all__'


class PassivedcequipmentmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmentmodels
        fields = '__all__'


class PassivedcequipmenttypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmenttypes
        fields = '__all__'


class UnmanagedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unmanageds
        fields = '__all__'


class DevicesimcardtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcardtypes
        fields = '__all__'


class ComputermodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computermodels
        fields = '__all__'


class ComputersItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputersItems
        fields = '__all__'


class ComputertypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computertypes
        fields = '__all__'


class MonitormodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitormodels
        fields = '__all__'


class MonitortypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitortypes
        fields = '__all__'


class SoftwarecategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarecategories
        fields = '__all__'


class SoftwarelicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarelicenses
        fields = '__all__'




class NetworkequipmentmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmentmodels
        fields = '__all__'


class PrintermodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printermodels
        fields = '__all__'


class PrintertypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printertypes
        fields = '__all__'


class PrintersCartridgeinfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintersCartridgeinfos
        fields = '__all__'


class CartridgeitemsPrintermodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartridgeitemsPrintermodels
        fields = '__all__'


class CartridgeitemtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartridgeitemtypes
        fields = '__all__'


class ConsumableitemtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumableitemtypes
        fields = '__all__'


class PhonemodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonemodels
        fields = '__all__'


class PhonepowersuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonepowersupplies
        fields = '__all__'


class PdusRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdusRacks
        fields = '__all__'


class NetworkequipmenttypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmenttypes
        fields = '__all__'


class PeripheraltypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheraltypes
        fields = '__all__'


class PeripheralmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheralmodels
        fields = '__all__'


class EntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        fields = '__all__'


class NetworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networks
        fields = '__all__'


class SnmpcredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snmpcredentials
        fields = '__all__'


class ManufacturersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields = '__all__'


class DcroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcrooms
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'


class ComputersSerializer(serializers.ModelSerializer):
    computertypes = ComputertypesSerializer(required=False)
    computermodels = ComputermodelsSerializer(required=False)
    entities = EntitiesSerializer(required=False)
    networks = NetworksSerializer(required=False)
    locations = LocationsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)

    class Meta:  # Clase meta para configurar el serializer
        model = Computers  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class MonitorsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    monitortypes = MonitortypesSerializer(required=False)
    monitormodels = MonitormodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)

    class Meta:
        model = Monitors
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


class NetworkequipmentsSerializer(serializers.ModelSerializer):
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    networks = NetworksSerializer(required=False)
    networkequipmenttypes = NetworkequipmenttypesSerializer(required=False)
    networkequipmentmodels = NetworkequipmentmodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    snmpcredentials = SnmpcredentialsSerializer(required=False)
    entities = EntitiesSerializer(required=False)

    class Meta:
        model = Networkequipments
        fields = '__all__'


class PeripheralsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    peripheraltypes = PeripheraltypesSerializer(required=False)
    peripheralmodels = PeripheralmodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)

    class Meta:
        model = Peripherals
        fields = '__all__'


class PrintersSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    networks = NetworksSerializer(required=False)
    printermodels = PrintermodelsSerializer(required=False)
    printertypes = PrintertypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    snmpcredentials = SnmpcredentialsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)

    class Meta:
        model = Printers
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


class PhonesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    phonetypes = PhonetypesSerializer(required=False)
    phonemodels = PhonemodelsSerializer(required=False)
    phonepowersupplies = PhonepowersuppliesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Phones
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


class EnclosuresSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    enclosuremodels = EnclosuremodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Enclosures
        fields = '__all__'


class PdusSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    pdumodels = PdumodelsSerializer(required=False)
    pdutypes = PdutypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Pdus
        fields = '__all__'


class PassivedcequipmentsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    passivedcequipmentmodels = PassivedcequipmentmodelsSerializer(required=False)
    passivedcequipmenttypes = PassivedcequipmenttypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Passivedcequipments
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


class CablesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    cablestrands = CablestrandsSerializer(required=False)
    cabletypes = CabletypesSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Cables
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
class GetComputersSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    computertypes = serializers.SerializerMethodField()
    computermodels = serializers.SerializerMethodField()
    operatingsystems = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    date_mod = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    processors = serializers.SerializerMethodField()

    def get_states(self, obj):
        return States.objects.filter(id=obj.states_id)[0].name

    def get_manufacturers(self, obj):
        return Manufacturers.objects.filter(id=obj.manufacturers_id)[0].name

    def get_computertypes(self, obj):
        return Computertypes.objects.filter(id=obj.computertypes_id)[0].name
    
    def get_computermodels(self, obj):
        return Computermodels.objects.filter(id=obj.computermodels_id)[0].name
    
    def get_operatingsystems(self, obj):
        items_operatingsystems = ItemsOperatingsystems.objects.filter(items_id=obj.id, itemtype='Computer')
        if (items_operatingsystems.count() > 0):
            return Operatingsystems.objects.filter(id=items_operatingsystems[0].operatingsystems_id)[0].name
        return None
            
    
    def get_locations(self, obj):
        return Computermodels.objects.filter(id=obj.computermodels_id)[0].name
    
    def get_processors(self, obj):
        items_deviceprocessors = ItemsDeviceprocessors.objects.filter(items_id=obj.id, itemtype='Computer')
        print(items_deviceprocessors)
        if (items_deviceprocessors.count() > 0):
            return items_deviceprocessors.count()
        return None
    
    class Meta:
        model = Computers
        fields = ['id', 'name', 'states', 'manufacturers', 'serial', 'computertypes', 'computermodels',
                  'operatingsystems', 'locations', 'date_mod', 'processors']


class GetMonitorsSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    monitortypes = serializers.SerializerMethodField()
    monitormodels = serializers.SerializerMethodField()
    date_mod = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 

    def get_states(self, obj):
        return States.objects.filter(id=obj.states_id)[0].name

    def get_manufacturers(self, obj):
        return Manufacturers.objects.filter(id=obj.manufacturers_id)[0].name
                
    def get_locations(self, obj):
        return Locations.objects.filter(id=obj.locations_id)[0].name

    def get_monitortypes(self, obj):
        return Monitortypes.objects.filter(id=obj.monitortypes_id)[0].name
    
    def get_monitormodels(self, obj):
        return Monitormodels.objects.filter(id=obj.monitormodels_id)[0].name
    class Meta:
        model = Monitors
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'monitortypes', 'monitormodels', 
                  'date_mod', 'contact']
        
class GetDevicesimcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devicesimcards
        fields = ['id']

class GetPeripheralsSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    peripheraltypes = serializers.SerializerMethodField()
    peripheralmodels = serializers.SerializerMethodField()
    date_mod = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 

    def get_states(self, obj):
        return States.objects.filter(id=obj.states_id)[0].name

    def get_manufacturers(self, obj):
        return Manufacturers.objects.filter(id=obj.manufacturers_id)[0].name
                
    def get_locations(self, obj):
        return Locations.objects.filter(id=obj.locations_id)[0].name

    def get_peripheraltypes(self, obj):
        return Peripheraltypes.objects.filter(id=obj.peripheraltypes_id)[0].name
    
    def get_peripheralmodels(self, obj):
        return Peripheralmodels.objects.filter(id=obj.peripheralmodels_id)[0].name
    class Meta:
        model = Peripherals
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'peripheraltypes', 'peripheralmodels', 
                  'date_mod', 'contact']
class GetPrintersSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    printertypes = serializers.SerializerMethodField()
    printermodels = serializers.SerializerMethodField()
    date_mod = serializers.DateTimeField(format="%Y-%m-%d %H:%M") 

    def get_states(self, obj):
        return States.objects.filter(id=obj.states_id)[0].name

    def get_manufacturers(self, obj):
        return Manufacturers.objects.filter(id=obj.manufacturers_id)[0].name
                
    def get_locations(self, obj):
        return Locations.objects.filter(id=obj.locations_id)[0].name

    def get_printertypes(self, obj):
        return Printertypes.objects.filter(id=obj.printertypes_id)[0].name
    
    def get_printermodels(self, obj):
        return Printermodels.objects.filter(id=obj.printermodels_id)[0].name
    class Meta:
        model = Printers
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'printertypes', 'printermodels', 
                  'date_mod']
