from rest_framework import serializers  # import de serializers
# import de todos los callcenterdata, proximamente se mueve a assets
from assets.models import *
from assistance import models as assistanceModels, serializers as assistanceSerializers


class AutoupdatesystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autoupdatesystems
        fields = '__all__'


class DevicemotherboardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicemotherboards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicenetworkcardmodelsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicenetworkcardmodels  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicenetworkcardsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta:  # Clase meta para configurar el serializer
        model = Devicenetworkcards  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class DevicepcimodelsSerializer(serializers.ModelSerializer):
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
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


class SoftwareversionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwareversions
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
    computertypes_id = serializers.SerializerMethodField()
    computermodels_id = serializers.SerializerMethodField()
    entities_id = serializers.SerializerMethodField()
    networks_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)

    class Meta:  # Clase meta para configurar el serializer
        model = Computers  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model

    def get_computermodels_id(self, obj):
        computermodels_id_query = Computermodels.objects.filter(
            id=obj.computermodels_id)
        serializer = ComputermodelsSerializer(
            computermodels_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_computertypes_id(self, obj):
        computertypes_id_query = Computertypes.objects.filter(
            id=obj.computertypes_id)
        serializer = ComputertypesSerializer(computertypes_id_query, many=True)
        return serializer.data

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(id=obj.entities_id)
        serializer = EntitiesSerializer(entities_id_query, many=True)
        return serializer.data

    def get_networks_id(self, obj):
        networks_id_query = Networks.objects.filter(id=obj.networks_id)
        serializer = NetworksSerializer(networks_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(id=obj.locations_id)
        serializer = LocationsSerializer(locations_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data


class MonitorsSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    monitortypes_id = serializers.SerializerMethodField()
    monitormodels_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()

    class Meta:
        model = Monitors
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(id=obj.entities_id)
        serializer = EntitiesSerializer(entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(id=obj.locations_id)
        serializer = LocationsSerializer(locations_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_monitortypes_id(self, obj):
        monitortypes_id_query = Monitortypes.objects.filter(
            id=obj.monitortypes_id)
        serializer = MonitortypesSerializer(
            monitortypes_id_query, many=True)
        return serializer.data

    def get_monitormodels_id(self, obj):
        monitormodels_id_query = Monitormodels.objects.filter(
            id=obj.monitormodels_id)
        serializer = MonitormodelsSerializer(
            monitormodels_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data


class SoftwaresSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    softwarecategories_id = serializers.SerializerMethodField()

    class Meta:
        model = Softwares
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(id=obj.entities_id)
        serializer = EntitiesSerializer(entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(id=obj.locations_id)
        serializer = LocationsSerializer(locations_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_softwarecategories_id(self, obj):
        softwarecategories_id_query = Softwarecategories.objects.filter(
            id=obj.softwarecategories_id)
        serializer = SoftwarecategoriesSerializer(
            softwarecategories_id_query, many=True)
        return serializer.data


class NetworkequipmentsSerializer(serializers.ModelSerializer):
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    networks_id = serializers.SerializerMethodField()
    networkequipmenttypes_id = serializers.SerializerMethodField()
    networkequipmentmodels_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()
    snmpcredentials_id = serializers.SerializerMethodField()
    entities_id = serializers.SerializerMethodField()

    class Meta:
        model = Networkequipments
        fields = '__all__'

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(id=obj.locations_id)
        serializer = LocationsSerializer(locations_id_query, many=True)
        return serializer.data

    def get_networks_id(self, obj):
        networks_id_query = Networks.objects.filter(id=obj.networks_id)
        serializer = NetworksSerializer(networks_id_query, many=True)
        return serializer.data

    def get_networkequipmenttypes_id(self, obj):
        networks_id_query = Networkequipmenttypes.objects.filter(
            id=obj.networkequipmenttypes_id)
        serializer = NetworkequipmenttypesSerializer(
            networks_id_query, many=True)
        return serializer.data

    def get_networkequipmentmodels_id(self, obj):
        networks_id_query = Networkequipmentmodels.objects.filter(
            id=obj.networkequipmentmodels_id)
        serializer = NetworksSerializer(networks_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data

    def get_snmpcredentials_id(self, obj):
        snmpcredentials_id_query = Snmpcredentials.objects.filter(
            id=obj.snmpcredentials_id)
        serializer = SnmpcredentialsSerializer(
            snmpcredentials_id_query, many=True)
        return serializer.data

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data


class PeripheralsSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    peripheraltypes_id = serializers.SerializerMethodField()
    peripheralmodels_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()

    class Meta:
        model = Peripherals
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(id=obj.locations_id)
        serializer = LocationsSerializer(locations_id_query, many=True)
        return serializer.data

    def get_peripheraltypes_id(self, obj):
        peripheraltypes_id_query = Peripheraltypes.objects.filter(
            id=obj.peripheraltypes_id)
        serializer = PeripheraltypesSerializer(
            peripheraltypes_id_query, many=True)
        return serializer.data

    def get_peripheralmodels_id(self, obj):
        peripheralmodels_id_query = Peripheralmodels.objects.filter(
            id=obj.peripheralmodels_id)
        serializer = PeripheralmodelsSerializer(
            peripheralmodels_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(id=obj.states_id)
        serializer = StatesSerializer(states_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data


class PrintersSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    networks_id = serializers.SerializerMethodField()
    printermodels_id = serializers.SerializerMethodField()
    printertypes_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()
    snmpcredentials_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()

    class Meta:
        model = Printers
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(id=obj.locations_id)
        serializer = LocationsSerializer(locations_id_query, many=True)
        return serializer.data

    def get_networks_id(self, obj):
        networks_id_query = Networks.objects.filter(id=obj.networks_id)
        serializer = NetworksSerializer(networks_id_query, many=True)
        return serializer.data

    def get_printermodels_id(self, obj):
        printermodels_id_query = Printermodels.objects.filter(
            id=obj.printermodels_id)
        serializer = PrintermodelsSerializer(printermodels_id_query, many=True)
        return serializer.data

    def get_printertypes_id(self, obj):
        printertypes_id_query = Printertypes.objects.filter(
            id=obj.printertypes_id)
        serializer = PrintertypesSerializer(printertypes_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(id=obj.states_id)
        serializer = StatesSerializer(states_id_query, many=True)
        return serializer.data

    def get_snmpcredentials_id(self, obj):
        snmpcredentials_id_query = Snmpcredentials.objects.filter(
            id=obj.snmpcredentials_id)
        serializer = SnmpcredentialsSerializer(
            snmpcredentials_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data


class CartridgeitemsSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    cartridgeitemtypes_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()

    class Meta:
        model = Cartridgeitems
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_cartridgeitemtypes_id(self, obj):
        cartridgeitemtypes_id_query = Cartridgeitemtypes.objects.filter(
            id=obj.cartridgeitemtypes_id)
        serializer = CartridgeitemtypesSerializer(
            cartridgeitemtypes_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data


class CartridgesSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    cartridgeitems_id = serializers.SerializerMethodField()
    printers_id = serializers.SerializerMethodField()

    class Meta:
        model = Cartridges
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_cartridgeitems_id(self, obj):
        cartridgeitems_id_query = Cartridgeitems.objects.filter(
            id=obj.cartridgeitems_id)
        serializer = CartridgeitemsSerializer(
            cartridgeitems_id_query, many=True)
        return serializer.data

    def get_printers_id(self, obj):
        printers_id_query = Printers.objects.filter(id=obj.printers_id)
        serializer = PrintersSerializer(printers_id_query, many=True)
        return serializer.data


class ConsumableitemsSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    consumableitemtypes_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()

    class Meta:
        model = Consumableitems
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_consumableitemtypes_id(self, obj):
        consumableitemtypes_id_query = Consumableitemtypes.objects.filter(
            id=obj.consumableitemtypes_id)
        serializer = ConsumableitemtypesSerializer(
            consumableitemtypes_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data


class PhonesSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    phonetypes_id = serializers.SerializerMethodField()
    phonemodels_id = serializers.SerializerMethodField()
    phonepowersupplies_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()

    class Meta:
        model = Phones
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_phonetypes_id(self, obj):
        phonetypes_id_query = Phonetypes.objects.filter(
            id=obj.phonetypes_id)
        serializer = PhonetypesSerializer(
            phonetypes_id_query, many=True)
        return serializer.data

    def get_phonemodels_id(self, obj):
        phonemodels_id_query = Phonemodels.objects.filter(
            id=obj.phonemodels_id)
        serializer = PhonemodelsSerializer(
            phonemodels_id_query, many=True)
        return serializer.data

    def get_phonepowersupplies_id(self, obj):
        phonepowersupplies_id_query = Phonepowersupplies.objects.filter(
            id=obj.phonepowersupplies_id)
        serializer = PhonepowersuppliesSerializer(
            phonepowersupplies_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data


class RacksSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    racktypes_id = serializers.SerializerMethodField()
    rackmodels_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()
    dcrooms_id = serializers.SerializerMethodField()

    class Meta:
        model = Racks
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_racktypes_id(self, obj):
        racktypes_id_query = Racktypes.objects.filter(
            id=obj.racktypes_id)
        serializer = RacktypesSerializer(
            racktypes_id_query, many=True)
        return serializer.data

    def get_rackmodels_id(self, obj):
        rackmodels_id_query = Rackmodels.objects.filter(
            id=obj.rackmodels_id)
        serializer = RackmodelsSerializer(
            rackmodels_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data

    def get_dcrooms_id(self, obj):
        dcrooms_id_query = Dcrooms.objects.filter(
            id=obj.dcrooms_id)
        serializer = DcroomsSerializer(
            dcrooms_id_query, many=True)
        return serializer.data


class EnclosuresSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    enclosuremodels_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()

    class Meta:
        model = Enclosures
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_enclosuremodels_id(self, obj):
        enclosuremodels_id_query = Enclosuremodels.objects.filter(
            id=obj.enclosuremodels_id)
        serializer = EnclosuremodelsSerializer(
            enclosuremodels_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data


class PdusSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    pdumodels_id = serializers.SerializerMethodField()
    pdutypes_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()

    class Meta:
        model = Pdus
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_pdumodels_id(self, obj):
        pdumodels_id_query = Pdumodels.objects.filter(
            id=obj.pdumodels_id)
        serializer = PdumodelsSerializer(
            pdumodels_id_query, many=True)
        return serializer.data

    def get_pdutypes_id(self, obj):
        pdutypes_id_query = Pdutypes.objects.filter(
            id=obj.pdutypes_id)
        serializer = PdutypesSerializer(
            pdutypes_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data


class PassivedcequipmentsSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    passivedcequipmentmodels_id = serializers.SerializerMethodField()
    passivedcequipmenttypes_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()

    class Meta:
        model = Passivedcequipments
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_passivedcequipmentmodels_id(self, obj):
        passivedcequipmentmodels_id_query = Passivedcequipmentmodels.objects.filter(
            id=obj.passivedcequipmentmodels_id)
        serializer = PassivedcequipmentmodelsSerializer(
            passivedcequipmentmodels_id_query, many=True)
        return serializer.data

    def get_passivedcequipmenttypes_id(self, obj):
        passivedcequipmenttypes_id_query = Passivedcequipmenttypes.objects.filter(
            id=obj.passivedcequipmenttypes_id)
        serializer = PassivedcequipmenttypesSerializer(
            passivedcequipmenttypes_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data


class UnmanagedsSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    locations_id = serializers.SerializerMethodField()
    networks_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    groups_id_tech = serializers.SerializerMethodField()
    users_id = serializers.SerializerMethodField()
    groups_id = serializers.SerializerMethodField()
    autoupdatesystems_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()

    class Meta:
        model = Unmanageds
        fields = '__all__'

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_groups_id_tech(self, obj):
        groups_id_tech_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id_tech)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_tech_query, many=True)
        return serializer.data

    def get_users_id(self, obj):
        users_id_query = assistanceModels.Users.objects.filter(
            id=obj.users_id)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_query, many=True)
        return serializer.data

    def get_groups_id(self, obj):
        groups_id_query = assistanceModels.Groups.objects.filter(
            id=obj.groups_id)
        serializer = assistanceSerializers.GroupsSerializer(
            groups_id_query, many=True)
        return serializer.data

    def get_autoupdatesystems_id(self, obj):
        autoupdatesystems_id_query = Autoupdatesystems.objects.filter(
            id=obj.autoupdatesystems_id)
        serializer = AutoupdatesystemsSerializer(
            autoupdatesystems_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_locations_id(self, obj):
        locations_id_query = Locations.objects.filter(
            id=obj.locations_id)
        serializer = LocationsSerializer(
            locations_id_query, many=True)
        return serializer.data

    def get_networks_id(self, obj):
        networks_id_query = Networks.objects.filter(
            id=obj.networks_id)
        serializer = NetworksSerializer(
            networks_id_query, many=True)
        return serializer.data


class CablesSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    users_id_tech = serializers.SerializerMethodField()
    cablestrands_id = serializers.SerializerMethodField()
    cabletypes_id = serializers.SerializerMethodField()
    states_id = serializers.SerializerMethodField()

    class Meta:
        model = Cables
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_cablestrands_id(self, obj):
        cablestrands_id_query = Cablestrands.objects.filter(
            id=obj.cablestrands_id)
        serializer = CablestrandsSerializer(
            cablestrands_id_query, many=True)
        return serializer.data

    def get_users_id_tech(self, obj):
        users_id_tech_query = assistanceModels.Users.objects.filter(
            id=obj.users_id_tech)
        serializer = assistanceSerializers.UsersSerializer(
            users_id_tech_query, many=True)
        return serializer.data

    def get_cabletypes_id(self, obj):
        cabletypes_id_query = Cabletypes.objects.filter(
            id=obj.cabletypes_id)
        serializer = CabletypesSerializer(
            cabletypes_id_query, many=True)
        return serializer.data

    def get_states_id(self, obj):
        states_id_query = States.objects.filter(
            id=obj.states_id)
        serializer = StatesSerializer(
            states_id_query, many=True)
        return serializer.data


class DevicesimcardsSerializer(serializers.ModelSerializer):
    entities_id = serializers.SerializerMethodField()
    manufacturers_id = serializers.SerializerMethodField()
    devicesimcardtypes_id = serializers.SerializerMethodField()

    class Meta:
        model = Devicesimcards
        fields = '__all__'

    def get_entities_id(self, obj):
        entities_id_query = Entities.objects.filter(
            id=obj.entities_id)
        serializer = EntitiesSerializer(
            entities_id_query, many=True)
        return serializer.data

    def get_manufacturers_id(self, obj):
        manufacturers_id_query = Manufacturers.objects.filter(
            id=obj.manufacturers_id)
        serializer = ManufacturersSerializer(
            manufacturers_id_query, many=True)
        return serializer.data

    def get_devicesimcardtypes_id(self, obj):
        devicesimcardtypes_id_query = Devicesimcardtypes.objects.filter(
            id=obj.devicesimcardtypes_id)
        serializer = DevicesimcardtypesSerializer(
            devicesimcardtypes_id_query, many=True)
        return serializer.data
