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

class DevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset= Devicemotherboards.objects.all()
    serializer_class = DevicemotherboardsSerializer

class DevicenetworkcardmodelsViewSet(viewsets.ModelViewSet):
    queryset= Devicenetworkcardmodels.objects.all()
    serializer_class = DevicenetworkcardmodelsSerializer 

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