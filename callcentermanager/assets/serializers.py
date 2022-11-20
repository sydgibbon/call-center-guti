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
    computertypes = ComputertypesSerializer()
    computermodels = ComputermodelsSerializer()
    entities = EntitiesSerializer()
    networks = NetworksSerializer()
    locations = LocationsSerializer()
    autoupdatesystems = AutoupdatesystemsSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    manufacturers = ManufacturersSerializer()
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)

    class Meta:  # Clase meta para configurar el serializer
        model = Computers  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model


class MonitorsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    locations = LocationsSerializer()
    monitortypes = MonitortypesSerializer()
    monitormodels = MonitormodelsSerializer()
    manufacturers = ManufacturersSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()
    autoupdatesystems = AutoupdatesystemsSerializer()

    class Meta:
        model = Monitors
        fields = '__all__'


class SoftwaresSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    manufacturers = ManufacturersSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    softwarecategories = SoftwarecategoriesSerializer()

    class Meta:
        model = Softwares
        fields = '__all__'


class NetworkequipmentsSerializer(serializers.ModelSerializer):
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    locations = LocationsSerializer()
    networks = NetworksSerializer()
    networkequipmenttypes = NetworkequipmenttypesSerializer()
    networkequipmentmodels = NetworkequipmentmodelsSerializer()
    manufacturers = ManufacturersSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()
    autoupdatesystems = AutoupdatesystemsSerializer()
    snmpcredentials = SnmpcredentialsSerializer()
    entities = EntitiesSerializer()

    class Meta:
        model = Networkequipments
        fields = '__all__'


class PeripheralsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    locations = LocationsSerializer()
    peripheraltypes = PeripheraltypesSerializer()
    peripheralmodels = PeripheralmodelsSerializer()
    manufacturers = ManufacturersSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()
    autoupdatesystems = AutoupdatesystemsSerializer()

    class Meta:
        model = Peripherals
        fields = '__all__'


class PrintersSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    locations = LocationsSerializer()
    networks = NetworksSerializer()
    printermodels = PrintermodelsSerializer
    printertypes = PrintertypesSerializer()
    manufacturers = ManufacturersSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()
    snmpcredentials = SnmpcredentialsSerializer()
    autoupdatesystems = AutoupdatesystemsSerializer()

    class Meta:
        model = Printers
        fields = '__all__'


class CartridgeitemsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    cartridgeitemtypes = CartridgeitemtypesSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()

    class Meta:
        model = Cartridgeitems
        fields = '__all__'


class CartridgesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    cartridgeitems = CartridgeitemsSerializer()
    printers = PrintersSerializer()

    class Meta:
        model = Cartridges
        fields = '__all__'


class ConsumableitemsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    consumableitemtypes = ConsumableitemtypesSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()

    class Meta:
        model = Consumableitems
        fields = '__all__'


class PhonesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    phonetypes = PhonetypesSerializer()
    phonemodels = PhonemodelsSerializer()
    phonepowersupplies = PhonepowersuppliesSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    autoupdatesystems = AutoupdatesystemsSerializer()
    states = StatesSerializer()

    class Meta:
        model = Phones
        fields = '__all__'


class RacksSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    racktypes = RacktypesSerializer()
    rackmodels = RackmodelsSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()
    dcrooms = DcroomsSerializer()

    class Meta:
        model = Racks
        fields = '__all__'


class EnclosuresSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    enclosuremodels = EnclosuremodelsSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()

    class Meta:
        model = Enclosures
        fields = '__all__'


class PdusSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    pdumodels = PdumodelsSerializer()
    pdutypes = PdutypesSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()

    class Meta:
        model = Pdus
        fields = '__all__'


class PassivedcequipmentsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    passivedcequipmentmodels = PassivedcequipmentmodelsSerializer()
    passivedcequipmenttypes = PassivedcequipmenttypesSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    states = StatesSerializer()

    class Meta:
        model = Passivedcequipments
        fields = '__all__'


class UnmanagedsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    locations = LocationsSerializer()
    networks = NetworksSerializer()
    manufacturers = ManufacturersSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    groups_tech = assistanceSerializers.GroupsSerializer()
    users = assistanceSerializers.UsersSerializer()
    groups = assistanceSerializers.GroupsSerializer()
    autoupdatesystems = AutoupdatesystemsSerializer()
    states = StatesSerializer()

    class Meta:
        model = Unmanageds
        fields = '__all__'


class CablesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    users_tech = assistanceSerializers.UsersSerializer()
    cablestrands = CablestrandsSerializer()
    cabletypes = CabletypesSerializer()
    states = StatesSerializer()

    class Meta:
        model = Cables
        fields = '__all__'


class DevicesimcardsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer()
    manufacturers = ManufacturersSerializer()
    devicesimcardtypes = DevicesimcardtypesSerializer()

    class Meta:
        model = Devicesimcards
        fields = '__all__'
