from rest_framework import viewsets  # import de ViewSets
from assets.serializers import *  # import de todos los serializers,
from rest_framework.permissions import IsAuthenticated

# ViewSets para cada Serializer


class ComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer
    permission_classes = (IsAuthenticated,)


class MonitorsViewSet(viewsets.ModelViewSet):
    queryset = Monitors.objects.all()
    serializer_class = MonitorsSerializer
    permission_classes = (IsAuthenticated,)


class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = SoftwaresSerializer
    permission_classes = (IsAuthenticated,)
# Desde aca empezo fran


class NetworkequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipments.objects.all()
    serializer_class = NetworkequipmentsSerializer
    permission_classes = (IsAuthenticated,)


class PrintersViewSet(viewsets.ModelViewSet):
    queryset = Printers.objects.all()
    serializer_class = PrintersSerializer
    permission_classes = (IsAuthenticated,)


class CartridgesViewSet(viewsets.ModelViewSet):
    queryset = Cartridges.objects.all()
    serializer_class = CartridgesSerializer
    permission_classes = (IsAuthenticated,)


class ConsumablesViewSet(viewsets.ModelViewSet):
    queryset = Consumables.objects.all()
    serializer_class = ConsumablesSerializer
    permission_classes = (IsAuthenticated,)


class PhonesViewSet(viewsets.ModelViewSet):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated,)


class RacksViewSet(viewsets.ModelViewSet):
    queryset = Racks.objects.all()
    serializer_class = RacksSerializer
    permission_classes = (IsAuthenticated,)


class EnclosuresViewSet(viewsets.ModelViewSet):
    queryset = Enclosures.objects.all()
    serializer_class = EnclosuresSerializer
    permission_classes = (IsAuthenticated,)


class PdusViewSet(viewsets.ModelViewSet):
    queryset = Pdus.objects.all()
    serializer_class = PdusSerializer
    permission_classes = (IsAuthenticated,)


class UnmanagedsViewSet(viewsets.ModelViewSet):
    queryset = Unmanageds.objects.all()
    serializer_class = UnmanagedsSerializer
    permission_classes = (IsAuthenticated,)


class CablesViewSet(viewsets.ModelViewSet):
    queryset = Cables.objects.all()
    serializer_class = CablesSerializer
    permission_classes = (IsAuthenticated,)


class DevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcards.objects.all()
    serializer_class = DevicesimcardsSerializer
    permission_classes = (IsAuthenticated,)


class ComputermodelsViewSet(viewsets.ModelViewSet):
    queryset = Computermodels.objects.all()
    serializer_class = ComputermodelsSerializer
    permission_classes = (IsAuthenticated,)


class ComputersItemsViewSet(viewsets.ModelViewSet):
    queryset = ComputersItems.objects.all()
    serializer_class = ComputersItemsSerializer
    permission_classes = (IsAuthenticated,)


class ComputertypesViewSet(viewsets.ModelViewSet):
    queryset = Computertypes.objects.all()
    serializer_class = ComputertypesSerializer
    permission_classes = (IsAuthenticated,)


class MonitormodelsViewSet(viewsets.ModelViewSet):
    queryset = Monitormodels.objects.all()
    serializer_class = MonitormodelsSerializer
    permission_classes = (IsAuthenticated,)


class MonitortypesViewSet(viewsets.ModelViewSet):
    queryset = Monitortypes.objects.all()
    serializer_class = MonitortypesSerializer
    permission_classes = (IsAuthenticated,)


class SoftwarecategoriesViewSet(viewsets.ModelViewSet):
    queryset = Softwarecategories.objects.all()
    serializer_class = SoftwarecategoriesSerializer
    permission_classes = (IsAuthenticated,)


class SoftwarelicensesViewSet(viewsets.ModelViewSet):
    queryset = Softwarelicenses.objects.all()
    serializer_class = SoftwarelicensesSerializer
    permission_classes = (IsAuthenticated,)


class SoftwareversionsViewSet(viewsets.ModelViewSet):
    queryset = Softwareversions.objects.all()
    serializer_class = SoftwareversionsSerializer
    permission_classes = (IsAuthenticated,)


class NetworkequipmentmodelsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipmentmodels.objects.all()
    serializer_class = NetworkequipmentmodelsSerializer
    permission_classes = (IsAuthenticated,)


class NetworkequipmenttypesViewSet(viewsets.ModelViewSet):
    queryset = Networkequipmenttypes.objects.all()
    serializer_class = NetworkequipmenttypesSerializer
    permission_classes = (IsAuthenticated,)


class PrintermodelsViewSet(viewsets.ModelViewSet):
    queryset = Printermodels.objects.all()
    serializer_class = PrintermodelsSerializer
    permission_classes = (IsAuthenticated,)


class PrintertypesViewSet(viewsets.ModelViewSet):
    queryset = Printertypes.objects.all()
    serializer_class = PrintertypesSerializer
    permission_classes = (IsAuthenticated,)


class PrintersCartridgeinfosViewSet(viewsets.ModelViewSet):
    queryset = PrintersCartridgeinfos.objects.all()
    serializer_class = PrintersCartridgeinfosSerializer
    permission_classes = (IsAuthenticated,)


class CartridgeitemsViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitems.objects.all()
    serializer_class = CartridgeitemsSerializer
    permission_classes = (IsAuthenticated,)


class CartridgeitemsPrintermodelsViewSet(viewsets.ModelViewSet):
    queryset = CartridgeitemsPrintermodels.objects.all()
    serializer_class = CartridgeitemsPrintermodelsSerializer
    permission_classes = (IsAuthenticated,)


class CartridgeitemtypesViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitemtypes.objects.all()
    serializer_class = CartridgeitemtypesSerializer
    permission_classes = (IsAuthenticated,)


class ConsumableitemsViewSet(viewsets.ModelViewSet):
    queryset = Consumableitems.objects.all()
    serializer_class = ConsumableitemsSerializer
    permission_classes = (IsAuthenticated,)


class ConsumableitemtypesViewSet(viewsets.ModelViewSet):
    queryset = Consumableitemtypes.objects.all()
    serializer_class = ConsumableitemtypesSerializer
    permission_classes = (IsAuthenticated,)


class PhonemodelsViewSet(viewsets.ModelViewSet):
    queryset = Phonemodels.objects.all()
    serializer_class = PhonemodelsSerializer
    permission_classes = (IsAuthenticated,)


class PhonepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = Phonepowersupplies.objects.all()
    serializer_class = PhonepowersuppliesSerializer
    permission_classes = (IsAuthenticated,)


class PhonetypesViewSet(viewsets.ModelViewSet):
    queryset = Phonetypes.objects.all()
    serializer_class = PhonetypesSerializer
    permission_classes = (IsAuthenticated,)


class ItemsRacksViewSet(viewsets.ModelViewSet):
    queryset = ItemsRacks.objects.all()
    serializer_class = ItemsRacksSerializer
    permission_classes = (IsAuthenticated,)


class ItemsEnclosuresViewSet(viewsets.ModelViewSet):
    queryset = ItemsEnclosures.objects.all()
    serializer_class = ItemsEnclosuresSerializer
    permission_classes = (IsAuthenticated,)


class PdusPlugsViewSet(viewsets.ModelViewSet):
    queryset = PdusPlugs.objects.all()
    serializer_class = PdusPlugsSerializer
    permission_classes = (IsAuthenticated,)


class PdusRacksViewSet(viewsets.ModelViewSet):
    queryset = PdusRacks.objects.all()
    serializer_class = PdusRacksSerializer
    permission_classes = (IsAuthenticated,)


class CablestrandsViewSet(viewsets.ModelViewSet):
    queryset = Cablestrands.objects.all()
    serializer_class = CablestrandsSerializer
    permission_classes = (IsAuthenticated,)


class CabletypesViewSet(viewsets.ModelViewSet):
    queryset = Cabletypes.objects.all()
    serializer_class = CabletypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicesimcardtypesViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcardtypes.objects.all()
    serializer_class = DevicesimcardtypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicebatteriesViewSet(viewsets.ModelViewSet):
    queryset = Devicebatteries.objects.all()
    serializer_class = DevicebatteriesSerializer
    permission_classes = (IsAuthenticated,)


class DevicebatterymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicebatterymodels.objects.all()
    serializer_class = DevicebatterymodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicebatterytypesViewSet(viewsets.ModelViewSet):
    queryset = Devicebatterytypes.objects.all()
    serializer_class = DevicebatterytypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicecameramodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicecameramodels.objects.all()
    serializer_class = DevicecameramodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicecamerasViewSet(viewsets.ModelViewSet):
    queryset = Devicecameras.objects.all()
    serializer_class = DevicecamerasSerializer
    permission_classes = (IsAuthenticated,)


class DevicecasemodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicecasemodels.objects.all()
    serializer_class = DevicecasemodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicecasesViewSet(viewsets.ModelViewSet):
    queryset = Devicecases.objects.all()
    serializer_class = DevicecasesSerializer
    permission_classes = (IsAuthenticated,)


class DevicecasetypesViewSet(viewsets.ModelViewSet):
    queryset = Devicecasetypes.objects.all()
    serializer_class = DevicecasetypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicecontrolmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicecontrolmodels.objects.all()
    serializer_class = DevicecontrolmodelsSerializer
    permission_classes = (IsAuthenticated,)
# Arranca Nata


class DevicecontrolsViewSet(viewsets.ModelViewSet):
    queryset = Devicecontrols.objects.all()
    serializer_class = DevicecontrolsSerializer
    permission_classes = (IsAuthenticated,)


class DevicedrivemodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicedrivemodels.objects.all()
    serializer_class = DevicedrivemodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicedrivesViewSet(viewsets.ModelViewSet):
    queryset = Devicedrives.objects.all()
    serializer_class = DevicedrivesSerializer
    permission_classes = (IsAuthenticated,)


class DevicefirmwaremodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwaremodels.objects.all()
    serializer_class = DevicefirmwaremodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicefirmwaresViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwares.objects.all()
    serializer_class = DevicefirmwaresSerializer
    permission_classes = (IsAuthenticated,)


class DevicefirmwaretypesViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwaretypes.objects.all()
    serializer_class = DevicefirmwaretypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicegenericmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicegenericmodels.objects.all()
    serializer_class = DevicegenericmodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicegenericsViewSet(viewsets.ModelViewSet):
    queryset = Devicegenerics.objects.all()
    serializer_class = DevicegenericsSerializer
    permission_classes = (IsAuthenticated,)


class DevicegenerictypesViewSet(viewsets.ModelViewSet):
    queryset = Devicegenerictypes.objects.all()
    serializer_class = DevicegenerictypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicegraphiccardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicegraphiccardmodels.objects.all()
    serializer_class = DevicegraphiccardmodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicegraphiccardsViewSet(viewsets.ModelViewSet):
    queryset = Devicegraphiccards.objects.all()
    serializer_class = DevicegraphiccardsSerializer
    permission_classes = (IsAuthenticated,)


class DeviceharddrivemodelsViewSet(viewsets.ModelViewSet):
    queryset = Deviceharddrivemodels.objects.all()
    serializer_class = DeviceharddrivemodelsSerializer
    permission_classes = (IsAuthenticated,)


class DeviceharddrivesViewSet(viewsets.ModelViewSet):
    queryset = Deviceharddrivemodels.objects.all()
    serializer_class = DeviceharddrivemodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicememoriesViewSet(viewsets.ModelViewSet):
    queryset = Devicememories.objects.all()
    serializer_class = DevicememoriesSerializer
    permission_classes = (IsAuthenticated,)


class DevicememorymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicememorymodels.objects.all()
    serializer_class = DevicememorymodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicememorytypesViewSet(viewsets.ModelViewSet):
    queryset = Devicememorytypes.objects.all()
    serializer_class = DevicememorytypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicemotherboardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicemotherboardmodels.objects.all()
    serializer_class = DevicemotherboardmodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset = Devicemotherboards.objects.all()
    serializer_class = DevicemotherboardsSerializer
    permission_classes = (IsAuthenticated,)


class DevicenetworkcardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicenetworkcardmodels.objects.all()
    serializer_class = DevicenetworkcardmodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicenetworkcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicenetworkcards.objects.all()
    serializer_class = DevicenetworkcardsSerializer
    permission_classes = (IsAuthenticated,)


class DevicepcimodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicepcimodels.objects.all()
    serializer_class = DevicepcimodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicepcisViewSet(viewsets.ModelViewSet):
    queryset = Devicepcis.objects.all()
    serializer_class = DevicepcisSerializer
    permission_classes = (IsAuthenticated,)


class DevicepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = Devicepowersupplies.objects.all()
    serializer_class = DevicepowersuppliesSerializer
    permission_classes = (IsAuthenticated,)


class DevicepowersupplymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicepowersupplymodels.objects.all()
    serializer_class = DevicepowersupplymodelsSerializer
    permission_classes = (IsAuthenticated,)


class DeviceprocessormodelsViewSet(viewsets.ModelViewSet):
    queryset = Deviceprocessormodels.objects.all()
    serializer_class = DeviceprocessormodelsSerializer
    permission_classes = (IsAuthenticated,)


class DeviceprocessorsViewSet(viewsets.ModelViewSet):
    queryset = Deviceprocessors.objects.all()
    serializer_class = DeviceprocessorsSerializer
    permission_classes = (IsAuthenticated,)


class DevicesensormodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicesensormodels.objects.all()
    serializer_class = DevicesensormodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicesensorsViewSet(viewsets.ModelViewSet):
    queryset = Devicesensors.objects.all()
    serializer_class = DevicesensorsSerializer
    permission_classes = (IsAuthenticated,)


class DevicesensortypesViewSet(viewsets.ModelViewSet):
    queryset = Devicesensortypes.objects.all()
    serializer_class = DevicesensortypesSerializer
    permission_classes = (IsAuthenticated,)


class DevicesoundcardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicesoundcardmodels.objects.all()
    serializer_class = DevicesoundcardmodelsSerializer
    permission_classes = (IsAuthenticated,)


class DevicesoundcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesoundcards.objects.all()
    serializer_class = DevicesoundcardsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicebatteriesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicebatteries.objects.all()
    serializer_class = ItemsDevicebatteriesSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicecamerasViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecameras.objects.all()
    serializer_class = ItemsDevicecamerasSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicecamerasImageformatsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecamerasImageformats.objects.all()
    serializer_class = ItemsDevicecamerasImageformatsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicecamerasImageresolutionsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecamerasImageresolutions.objects.all()
    serializer_class = ItemsDevicecamerasImageresolutionsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicecasesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecases.objects.all()
    serializer_class = ItemsDevicecasesSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicecontrolsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecontrols.objects.all()
    serializer_class = ItemsDevicecontrolsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicedrivesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicedrives.objects.all()
    serializer_class = ItemsDevicedrivesSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicefirmwaresViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicefirmwares.objects.all()
    serializer_class = ItemsDevicefirmwaresSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicegenericsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicegenerics.objects.all()
    serializer_class = ItemsDevicegenericsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicegraphiccardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicegraphiccards.objects.all()
    serializer_class = ItemsDevicegraphiccardsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDeviceharddrivesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDeviceharddrives.objects.all()
    serializer_class = ItemsDeviceharddrivesSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicememoriesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicememories.objects.all()
    serializer_class = ItemsDevicememoriesSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicemotherboards.objects.all()
    serializer_class = ItemsDevicemotherboardsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicenetworkcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicenetworkcards.objects.all()
    serializer_class = ItemsDevicenetworkcardsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicepcisViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicepcis.objects.all()
    serializer_class = ItemsDevicepcisSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicepowersupplies.objects.all()
    serializer_class = ItemsDevicepowersuppliesSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDeviceprocessorsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDeviceprocessors.objects.all()
    serializer_class = ItemsDeviceprocessorsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicesensorsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesensors.objects.all()
    serializer_class = ItemsDevicesensorsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesimcards.objects.all()
    serializer_class = ItemsDevicesimcardsSerializer
    permission_classes = (IsAuthenticated,)


class ItemsDevicesoundcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesoundcards.objects.all()
    serializer_class = ItemsDevicesoundcardsSerializer
    permission_classes = (IsAuthenticated,)
