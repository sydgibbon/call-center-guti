import queue
from winreg import QueryInfoKey
from rest_framework import viewsets #import de ViewSets
from assets.serializers import * #import de todos los serializers,

#ViewSets para cada Serializer
class ComputersViewSet(viewsets.ModelViewSet):
    queryset= Computers.objects.all()
    serializer_class = ComputersSerializer

class MonitorsViewSet(viewsets.ModelViewSet):
    queryset= Monitors.objects.all()
    serializer_class = MonitorsSerializer

class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset= Softwares.objects.all()
    serializer_class = SoftwaresSerializer

#Desde aca empezo fran
class NetworkequipmentsViewSet(viewsets.ModelViewSet):
    queryset= Networkequipments.objects.all()
    serializer_class = NetworkequipmentsSerializer

class PrintersViewSet(viewsets.ModelViewSet):
    queryset= Printers.objects.all()
    serializer_class = PrintersSerializer

class CartridgesViewSet(viewsets.ModelViewSet):
    queryset= Cartridges.objects.all()
    serializer_class = CartridgesSerializer

class ConsumablesViewSet(viewsets.ModelViewSet):
    queryset= Consumables.objects.all()
    serializer_class = ConsumablesSerializer

class PhonesViewSet(viewsets.ModelViewSet):
    queryset= Phones.objects.all()
    serializer_class = PhonesSerializer

class RacksViewSet(viewsets.ModelViewSet):
    queryset= Racks.objects.all()
    serializer_class = RacksSerializer

class EnclosuresViewSet(viewsets.ModelViewSet):
    queryset= Enclosures.objects.all()
    serializer_class = EnclosuresSerializer

class PdusViewSet(viewsets.ModelViewSet):
    queryset= Pdus.objects.all()
    serializer_class = PdusSerializer

class UnmanagedsViewSet(viewsets.ModelViewSet):
    queryset= Unmanageds.objects.all()
    serializer_class = UnmanagedsSerializer

class CablesViewSet(viewsets.ModelViewSet):
    queryset= Cables.objects.all()
    serializer_class = CablesSerializer

class DevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset= Devicesimcards.objects.all()
    serializer_class = DevicesimcardsSerializer

class ComputermodelsViewSet(viewsets.ModelViewSet):
    queryset= Computermodels.objects.all()
    serializer_class = ComputermodelsSerializer

class ComputersItemsViewSet(viewsets.ModelViewSet):
    queryset= ComputersItems.objects.all()
    serializer_class = ComputersItemsSerializer

class ComputertypesViewSet(viewsets.ModelViewSet):
    queryset= Computertypes.objects.all()
    serializer_class = ComputertypesSerializer

class MonitormodelsViewSet(viewsets.ModelViewSet):
    queryset= Monitormodels.objects.all()
    serializer_class = MonitormodelsSerializer

class MonitortypesViewSet(viewsets.ModelViewSet):
    queryset= Monitortypes.objects.all()
    serializer_class = MonitortypesSerializer

class SoftwarecategoriesViewSet(viewsets.ModelViewSet):
    queryset= Softwarecategories.objects.all()
    serializer_class = SoftwarecategoriesSerializer

class SoftwarelicensesViewSet(viewsets.ModelViewSet):
    queryset= Softwarelicenses.objects.all()
    serializer_class = SoftwarelicensesSerializer

class SoftwareversionsViewSet(viewsets.ModelViewSet):
    queryset= Softwareversions.objects.all()
    serializer_class = SoftwareversionsSerializer

class NetworkequipmentmodelsViewSet(viewsets.ModelViewSet):
    queryset= Networkequipmentmodels.objects.all()
    serializer_class = NetworkequipmentmodelsSerializer

class NetworkequipmenttypesViewSet(viewsets.ModelViewSet):
    queryset= Networkequipmenttypes.objects.all()
    serializer_class = NetworkequipmenttypesSerializer

class PrintermodelsViewSet(viewsets.ModelViewSet):
    queryset= Printermodels.objects.all()
    serializer_class = PrintermodelsSerializer

class PrintertypesViewSet(viewsets.ModelViewSet):
    queryset= Printertypes.objects.all()
    serializer_class = PrintertypesSerializer

class PrintersCartridgeinfosViewSet(viewsets.ModelViewSet):
    queryset= PrintersCartridgeinfos.objects.all()
    serializer_class = PrintersCartridgeinfosSerializer

class CartridgeitemsViewSet(viewsets.ModelViewSet):
    queryset= Cartridgeitems.objects.all()
    serializer_class = CartridgeitemsSerializer

class CartridgeitemsPrintermodelsViewSet(viewsets.ModelViewSet):
    queryset= CartridgeitemsPrintermodels.objects.all()
    serializer_class = CartridgeitemsPrintermodelsSerializer

class CartridgeitemtypesViewSet(viewsets.ModelViewSet):
    queryset= Cartridgeitemtypes.objects.all()
    serializer_class = CartridgeitemtypesSerializer

class ConsumableitemsViewSet(viewsets.ModelViewSet):
    queryset= Consumableitems.objects.all()
    serializer_class = ConsumableitemsSerializer

class ConsumableitemtypesViewSet(viewsets.ModelViewSet):
    queryset= Consumableitemtypes.objects.all()
    serializer_class = ConsumableitemtypesSerializer

class PhonemodelsViewSet(viewsets.ModelViewSet):
    queryset= Phonemodels.objects.all()
    serializer_class = PhonemodelsSerializer

class PhonepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset= Phonepowersupplies.objects.all()
    serializer_class = PhonepowersuppliesSerializer

class PhonetypesViewSet(viewsets.ModelViewSet):
    queryset= Phonetypes.objects.all()
    serializer_class = PhonetypesSerializer

class ItemsRacksViewSet(viewsets.ModelViewSet):
    queryset= ItemsRacks.objects.all()
    serializer_class = ItemsRacksSerializer

class ItemsEnclosuresViewSet(viewsets.ModelViewSet):
    queryset= ItemsEnclosures.objects.all()
    serializer_class = ItemsEnclosuresSerializer

class PdusPlugsViewSet(viewsets.ModelViewSet):
    queryset= PdusPlugs.objects.all()
    serializer_class = PdusPlugsSerializer

class PdusRacksViewSet(viewsets.ModelViewSet):
    queryset= PdusRacks.objects.all()
    serializer_class = PdusRacksSerializer

class CablestrandsViewSet(viewsets.ModelViewSet):
    queryset= Cablestrands.objects.all()
    serializer_class = CablestrandsSerializer

class CabletypesViewSet(viewsets.ModelViewSet):
    queryset= Cabletypes.objects.all()
    serializer_class = CabletypesSerializer

class DevicesimcardtypesViewSet(viewsets.ModelViewSet):
    queryset= Devicesimcardtypes.objects.all()
    serializer_class = DevicesimcardtypesSerializer

class DevicebatteriesViewSet(viewsets.ModelViewSet):
    queryset= Devicebatteries.objects.all()
    serializer_class = DevicebatteriesSerializer

class DevicebatterymodelsViewSet(viewsets.ModelViewSet):
    queryset= Devicebatterymodels.objects.all()
    serializer_class = DevicebatterymodelsSerializer

class DevicebatterytypesViewSet(viewsets.ModelViewSet):
    queryset= Devicebatterytypes.objects.all()
    serializer_class = DevicebatterytypesSerializer

class DevicecameramodelsViewSet(viewsets.ModelViewSet):
    queryset= Devicecameramodels.objects.all()
    serializer_class = DevicecameramodelsSerializer

class DevicecamerasViewSet(viewsets.ModelViewSet):
    queryset= Devicecameras.objects.all()
    serializer_class = DevicecamerasSerializer

class DevicecasemodelsViewSet(viewsets.ModelViewSet):
    queryset= Devicecasemodels.objects.all()
    serializer_class = DevicecasemodelsSerializer

class DevicecasesViewSet(viewsets.ModelViewSet):
    queryset= Devicecases.objects.all()
    serializer_class = DevicecasesSerializer

class DevicecasetypesViewSet(viewsets.ModelViewSet):
    queryset= Devicecasetypes.objects.all()
    serializer_class = DevicecasetypesSerializer

class DevicecontrolmodelsViewSet(viewsets.ModelViewSet):
    queryset= Devicecontrolmodels.objects.all()
    serializer_class = DevicecontrolmodelsSerializer

# Arranca Nata
class DevicecontrolsViewSet(viewsets.ModelViewSet):
    queryset = Devicecontrols.objects.all()
    serializer_class = DevicecontrolsSerializer

class DevicedrivemodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicedrivemodels.objects.all()
    serializer_class = DevicedrivemodelsSerializer

class DevicedrivesViewSet(viewsets.ModelViewSet):
    queryset = Devicedrives.objects.all()
    serializer_class = DevicedrivesSerializer

class DevicefirmwaremodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwaremodels.objects.all()
    serializer_class = DevicefirmwaremodelsSerializer

class DevicefirmwaresViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwares.objects.all()
    serializer_class = DevicefirmwaresSerializer

class DevicefirmwaretypesViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwaretypes.objects.all()
    serializer_class = DevicefirmwaretypesSerializer

class DevicegenericmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicegenericmodels.objects.all()
    serializer_class = DevicegenericmodelsSerializer

class DevicegenericsViewSet(viewsets.ModelViewSet):
    queryset = Devicegenerics.objects.all()
    serializer_class = DevicegenericsSerializer

class DevicegenerictypesViewSet(viewsets.ModelViewSet):
    queryset = Devicegenerictypes.objects.all()
    serializer_class = DevicegenerictypesSerializer

class DevicegraphiccardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicegraphiccardmodels.objects.all()
    serializer_class = DevicegraphiccardmodelsSerializer

class DevicegraphiccardsViewSet(viewsets.ModelViewSet):
    queryset = Devicegraphiccards.objects.all()
    serializer_class = DevicegraphiccardsSerializer

class DeviceharddrivemodelsViewSet(viewsets.ModelViewSet):
    queryset = Deviceharddrivemodels.objects.all()
    serializer_class = DeviceharddrivemodelsSerializer

class DeviceharddrivesViewSet(viewsets.ModelViewSet):
    queryset = Deviceharddrivemodels.objects.all()
    serializer_class = DeviceharddrivemodelsSerializer

class DevicememoriesViewSet(viewsets.ModelViewSet):
    queryset = Devicememories.objects.all()
    serializer_class = DevicememoriesSerializer

class DevicememorymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicememorymodels.objects.all()
    serializer_class = DevicememorymodelsSerializer

class DevicememorytypesViewSet(viewsets.ModelViewSet):
    queryset = Devicememorytypes.objects.all()
    serializer_class = DevicememorytypesSerializer

class DevicemotherboardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicemotherboardmodels.objects.all()
    serializer_class = DevicemotherboardmodelsSerializer

class DevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset = Devicemotherboards.objects.all()
    serializer_class = DevicemotherboardsSerializer

class DevicenetworkcardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicenetworkcardmodels.objects.all()
    serializer_class = DevicenetworkcardmodelsSerializer

class DevicenetworkcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicenetworkcards.objects.all()
    serializer_class = DevicenetworkcardsSerializer

class DevicepcimodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicepcimodels.objects.all()
    serializer_class = DevicepcimodelsSerializer

class DevicepcisViewSet(viewsets.ModelViewSet):
    queryset = Devicepcis.objects.all()
    serializer_class = DevicepcisSerializer

class DevicepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = Devicepowersupplies.objects.all()
    serializer_class = DevicepowersuppliesSerializer

class DevicepowersupplymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicepowersupplymodels.objects.all()
    serializer_class = DevicepowersupplymodelsSerializer

class DeviceprocessormodelsViewSet(viewsets.ModelViewSet):
    queryset = Deviceprocessormodels.objects.all()
    serializer_class = DeviceprocessormodelsSerializer

class DeviceprocessorsViewSet(viewsets.ModelViewSet):
    queryset = Deviceprocessors.objects.all()
    serializer_class = DeviceprocessorsSerializer

class DevicesensormodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicesensormodels.objects.all()
    serializer_class = DevicesensormodelsSerializer

class DevicesensorsViewSet(viewsets.ModelViewSet):
    queryset = Devicesensors.objects.all()
    serializer_class = DevicesensorsSerializer

class DevicesensortypesViewSet(viewsets.ModelViewSet):
    queryset = Devicesensortypes.objects.all()
    serializer_class = DevicesensortypesSerializer

class DevicesoundcardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicesoundcardmodels.objects.all()
    serializer_class = DevicesoundcardmodelsSerializer

class DevicesoundcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesoundcards.objects.all()
    serializer_class = DevicesoundcardsSerializer

class ItemsDevicebatteriesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicebatteries.objects.all()
    serializer_class = ItemsDevicebatteriesSerializer

class ItemsDevicecamerasViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecameras.objects.all()
    serializer_class = ItemsDevicecamerasSerializer

class ItemsDevicecamerasImageformatsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecamerasImageformats.objects.all()
    serializer_class = ItemsDevicecamerasImageformatsSerializer

class ItemsDevicecamerasImageresolutionsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecamerasImageresolutions.objects.all()
    serializer_class = ItemsDevicecamerasImageresolutionsSerializer

class ItemsDevicecasesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecases.objects.all()
    serializer_class = ItemsDevicecasesSerializer

class ItemsDevicecontrolsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecontrols.objects.all()
    serializer_class = ItemsDevicecontrolsSerializer

class ItemsDevicedrivesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicedrives.objects.all()
    serializer_class = ItemsDevicedrivesSerializer

class ItemsDevicefirmwaresViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicefirmwares.objects.all()
    serializer_class = ItemsDevicefirmwaresSerializer

class ItemsDevicegenericsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicegenerics.objects.all()
    serializer_class = ItemsDevicegenericsSerializer

class ItemsDevicegraphiccardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicegraphiccards.objects.all()
    serializer_class = ItemsDevicegraphiccardsSerializer

class ItemsDeviceharddrivesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDeviceharddrives.objects.all()
    serializer_class = ItemsDeviceharddrivesSerializer

class ItemsDevicememoriesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicememories.objects.all()
    serializer_class = ItemsDevicememoriesSerializer

class ItemsDevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicemotherboards.objects.all()
    serializer_class = ItemsDevicemotherboardsSerializer

class ItemsDevicenetworkcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicenetworkcards.objects.all()
    serializer_class = ItemsDevicenetworkcardsSerializer

class ItemsDevicepcisViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicepcis.objects.all()
    serializer_class = ItemsDevicepcisSerializer

class ItemsDevicepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicepowersupplies.objects.all()
    serializer_class = ItemsDevicepowersuppliesSerializer

class ItemsDeviceprocessorsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDeviceprocessors.objects.all()
    serializer_class = ItemsDeviceprocessorsSerializer

class ItemsDevicesensorsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesensors.objects.all()
    serializer_class = ItemsDevicesensorsSerializer

class ItemsDevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesimcards.objects.all()
    serializer_class = ItemsDevicesimcardsSerializer

class ItemsDevicesoundcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesoundcards.objects.all()
    serializer_class = ItemsDevicesoundcardsSerializer



