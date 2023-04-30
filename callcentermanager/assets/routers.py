from rest_framework.routers import DefaultRouter
from .views import *
from assets.computers import views as computers
from assets.locations import views as locations
from assets.states import views as states
from assets.manufacturers import views as manufacturers
from assets.autoupdatesystems import views as autoupdatesystems
from assets.networks import views as networks
from assets.snmpcredentials import views as snmpcredentials
from assets.users import views as users
from assets.groups import views as groups
from assets.networkequipments import views as networkequipments
from assets.simcards import views as simcards

router=DefaultRouter()
router.register(r'computers', ComputersViewSet, basename='computers')
router.register(r'monitors', MonitorsViewSet, basename='monitors')
router.register(r'softwares', SoftwaresViewSet, basename='softwares')
router.register(r'networkequipments', NetworkequipmentsViewSet, basename='networkequipments')
router.register(r'printers', PrintersViewSet, basename='printers')
router.register(r'cartridges', CartridgesViewSet, basename='cartridges')
router.register(r'consumables', ConsumablesViewSet, basename='consumables')
router.register(r'phones', PhonesViewSet, basename='phones')
router.register(r'racks', RacksViewSet, basename='racks')
router.register(r'enclosures', EnclosuresViewSet, basename='enclosures')
router.register(r'pdus', PdusViewSet, basename='pdus')
router.register(r'pdutypes', PdusViewSet, basename='pdutypes')
router.register(r'pdumodels', PdusViewSet, basename='pdumodels')
router.register(r'passivedcequipments', PassivedcequipmentsViewSet, basename='passivedcequipments')
router.register(r'passivedcequipmentmodels', PassivedcequipmentmodelsViewSet, basename='passivedcequipmentmodels')
router.register(r'passivedcequipmenttypes', PassivedcequipmenttypesViewSet, basename='passivedcequipmenttypes')
router.register(r'unmanageds', UnmanagedsViewSet, basename='unmanageds')
router.register(r'cables', CablesViewSet, basename='cables')
router.register(r'devicesimcards', DevicesimcardsViewSet, basename='devicesimcards')
router.register(r'computermodels', ComputermodelsViewSet, basename='computermodels')
router.register(r'computersitems', ComputersItemsViewSet, basename='computersitems')
router.register(r'computertypes', ComputertypesViewSet, basename='computertypes')
router.register(r'monitormodels', MonitormodelsViewSet, basename='monitormodels')
router.register(r'monitortypes', MonitortypesViewSet, basename='monitortypes')
router.register(r'softwarecategories', SoftwarecategoriesViewSet, basename='softwarecategories')
router.register(r'softwarelicenses', SoftwarelicensesViewSet, basename='softwarelicenses')
router.register(r'softwareversions', SoftwareversionsViewSet, basename='softwareversions')
router.register(r'networkequipmentmodels', NetworkequipmentmodelsViewSet, basename='networkequipmentmodels')
router.register(r'networkequipmenttypes', NetworkequipmenttypesViewSet, basename='networkequipmenttypes')
router.register(r'printermodels', PrintermodelsViewSet, basename='printermodels')
router.register(r'printertypes', PrintertypesViewSet, basename='printertypes')
router.register(r'printerscartridgeinfos', PrintersCartridgeinfosViewSet, basename='printerscartridgeinfos')
router.register(r'cartridgeitems', CartridgeitemsViewSet, basename='cartridgeitems')
router.register(r'cartridgeitemsprintermodels', CartridgeitemsPrintermodelsViewSet, basename='cartridgeitemsprintermodels')
router.register(r'cartridgeitemtypes', CartridgeitemtypesViewSet, basename='cartridgeitemtypes')
router.register(r'consumableitems', ConsumableitemsViewSet, basename='consumableitems')
router.register(r'consumableitemtypes', ConsumableitemtypesViewSet, basename='consumableitemtypes')
router.register(r'phonemodels', PhonemodelsViewSet, basename='phonemodels')
router.register(r'phonepowersupplies', PhonepowersuppliesViewSet, basename='phonepowersupplies')
router.register(r'phonetypes', PhonetypesViewSet, basename='phonetypes')
router.register(r'itemsracks', ItemsRacksViewSet, basename='itemsracks')
router.register(r'itemsenclosures', ItemsEnclosuresViewSet, basename='itemsenclosures')
router.register(r'pdusplugs', PdusPlugsViewSet, basename='pdusplugs')
router.register(r'pdusracks', PdusRacksViewSet, basename='pdusracks')
router.register(r'cablestrands', CablestrandsViewSet, basename='cablestrands')
router.register(r'cabletypes', CabletypesViewSet, basename='cabletypes')
router.register(r'devicesimcardtypes', DevicesimcardtypesViewSet, basename='devicesimcardtypes')
router.register(r'devicebatteries', DevicebatteriesViewSet, basename='devicebatteries')
router.register(r'devicebatterymodels', DevicebatterymodelsViewSet, basename='devicebatterymodels')
router.register(r'devicebatterytypes', DevicebatterytypesViewSet, basename='devicebatterytypes')
router.register(r'devicecameramodels', DevicecameramodelsViewSet, basename='devicecameramodels')
router.register(r'devicecameras', DevicecamerasViewSet, basename='devicecameras')
router.register(r'devicecasemodels', DevicecasemodelsViewSet, basename='devicecasemodels')
router.register(r'devicecases', DevicecasesViewSet, basename='devicecases')
router.register(r'devicecasetypes', DevicecasetypesViewSet, basename='devicecasetypes')
router.register(r'devicecontrolmodels', DevicecontrolmodelsViewSet, basename='devicecontrolmodels')
router.register(r'devicecontrols', DevicecontrolsViewSet, basename='devicecontrols')
router.register(r'devicedrivemodels', DevicedrivemodelsViewSet, basename='devicedrivemodels')
router.register(r'devicedrives', DevicedrivesViewSet, basename='devicedrives')
router.register(r'devicefirmwaremodels', DevicefirmwaremodelsViewSet, basename='devicefirmwaremodels')
router.register(r'devicefirmwares', DevicefirmwaresViewSet, basename='devicefirmwares')
router.register(r'devicefirmwaretypes', DevicefirmwaretypesViewSet, basename='devicefirmwaretypes')
router.register(r'devicegenericmodels', DevicegenericmodelsViewSet, basename='devicegenericmodels')
router.register(r'devicegenerics', DevicegenericsViewSet, basename='devicegenerics')
router.register(r'devicegenerictypes', DevicegenerictypesViewSet, basename='devicegenerictypes')
router.register(r'devicegraphiccardmodels', DevicegraphiccardmodelsViewSet, basename='devicegraphiccardmodels')
router.register(r'devicegraphiccards', DevicegraphiccardsViewSet, basename='devicegraphiccards')
router.register(r'deviceharddrivemodels', DeviceharddrivemodelsViewSet, basename='deviceharddrivemodels')
router.register(r'deviceharddrives', DeviceharddrivesViewSet, basename='deviceharddrives')
router.register(r'devicememories',DevicememoriesViewSet, basename='devicememories')
router.register(r'devicememorymodels', DevicememorymodelsViewSet, basename='devicememorymodels')
router.register(r'devicememorytypes', DevicememorytypesViewSet, basename='devicememorytypes')
router.register(r'devicemotherboardmodels', DevicemotherboardmodelsViewSet, 'devicemotherboardmodels')
router.register(r'devicemotherboards', DevicemotherboardsViewSet, basename='devicemotherboards')
router.register(r'devicenetworkcardmodels', DevicenetworkcardmodelsViewSet, basename='devicenetworkcardmodels')
router.register(r'devicenetworkcards', DevicenetworkcardsViewSet, basename='devicenetworkcards')
router.register(r'devicepcimodels', DevicepcimodelsViewSet, basename='devicepcimodels')
router.register(r'devicepcis', DevicepcisViewSet, basename='devicepcis')
router.register(r'devicepowersupplies', DevicepowersuppliesViewSet, basename='devicepowersupplies')
router.register(r'devicepowersupplymodels', DevicepowersupplymodelsViewSet, basename='devicepowersupplymodels')
router.register(r'deviceprocessormodels', DeviceprocessormodelsViewSet, basename='deviceprocessormodels')
router.register(r'deviceprocessors', DeviceprocessorsViewSet, basename='deviceprocessors')
router.register(r'devicesensormodels', DevicesensormodelsViewSet , basename='devicesensormodels')
router.register(r'devicesensors', DevicesensorsViewSet, basename='devicesensors')
router.register(r'devicesensortypes', DevicesensortypesViewSet, basename='devicesensortypes')
router.register(r'devicesoundcardmodels', DevicesoundcardmodelsViewSet, basename='devicesoundcardmodels')
router.register(r'devicesoundcards', DevicesoundcardsViewSet, basename='devicesoundcards')
router.register(r'itemsdevicebatteries', ItemsDevicebatteriesViewSet, basename='itemsdevicebatteries')
router.register(r'itemsdevicecameras', ItemsDevicecamerasViewSet, basename='itemsdevicecameras')
router.register(r'itemsdevicecamerasimageformats', ItemsDevicecamerasImageformatsViewSet, basename='itemsdevicecamerasimageformats')
router.register(r'Itemsdevicecamerasimageresolutions', ItemsDevicecamerasImageresolutionsViewSet, 'Itemsdevicecamerasimageresolutions')
router.register(r'Itemsdevicecases', ItemsDevicecasesViewSet, basename='Itemsdevicecases')
router.register(r'Itemsdevicecontrols', ItemsDevicecontrolsViewSet, basename='Itemsdevicecontrols')
router.register(r'itemsdevicedrives', ItemsDevicedrivesViewSet, basename='itemsdevicedrives')
router.register(r'itemsdevicefirmwares', ItemsDevicefirmwaresViewSet, basename='itemsdevicefirmwares')
router.register(r'itemsdevicegenerics', ItemsDevicegenericsViewSet, basename='itemsdevicegenerics')
router.register(r'itemsdevicegraphiccards', ItemsDevicegraphiccardsViewSet, basename='itemsdevicegraphiccards')
router.register(r'itemsdeviceharddrives', ItemsDeviceharddrivesViewSet, basename='itemsdeviceharddrives')
router.register(r'itemsdevicememories', ItemsDevicememoriesViewSet, basename='itemsdevicememories')
router.register(r'itemsdevicemotherboards', ItemsDevicemotherboardsViewSet, basename='itemsdevicemotherboards')
router.register(r'itemsdevicenetworkcards', ItemsDevicenetworkcardsViewSet, basename='itemsdevicenetworkcards')
router.register(r'itemsdevicepcis', ItemsDevicepcisViewSet, basename='itemsdevicepcis')
router.register(r'itemsdevicepowersupplies', ItemsDevicepowersuppliesViewSet, basename='itemsdevicepowersupplies')
router.register(r'itemsdeviceprocessors', ItemsDeviceprocessorsViewSet, basename='itemsdeviceprocessors')
router.register(r'itemsdevicesensors', ItemsDevicesensorsViewSet, basename='itemsdevicesensors')
router.register(r'itemsdevicesimcards', ItemsDevicesimcardsViewSet, basename='itemsdevicesimcards')
router.register(r'itemsdevicesoundcards', ItemsDevicesoundcardsViewSet, basename='itemsdevicesoundcards')
router.register(r'peripherals', PeripheralsViewSet, basename='peripherals')
router.register(r'peripheralmodels', PeripheralmodelsViewSet, basename='peripheralmodels')
router.register(r'peripheraltypes', PeripheraltypesViewSet, basename='peripheraltypes')
router.register(r'autoupdatesystems', AutoupdatesystemsViewSet, basename='autoupdatesystems')
router.register(r'rackmodels', RackmodelsViewSet, basename='rackmodels')
router.register(r'racktypes', RacktypesViewSet, basename='racktypes')
router.register(r'enclosuremodels', EnclosuremodelsViewSet, basename='enclosuremodels')
router.register(r'entities', EntitiesViewSet, basename='entities')
router.register(r'networks', NetworksViewSet, basename='networks')
router.register(r'snmpcredentials', SnmpcredentialsViewSet, basename='snmpcredentials')
router.register(r'manufacturers', ManufacturersViewSet, basename='manufacturers')
router.register(r'dcrooms', DcroomsViewSet, basename='dcrooms')
router.register(r'locations', LocationsViewSet, basename='locations')
router.register(r'states', StatesViewSet, basename='states')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'operatingsystems', OperatingsystemsViewSet, basename='operatingsystems')

# tables
router.register(r'getComputers', GetComputersViewSet, basename='getComputers')
router.register(r'getMonitors', GetMonitorsViewSet, basename='getMonitors')
router.register(r'getDevicesimcards', GetDevicesimcardsViewSet, basename='getDevicesimcards')
router.register(r'getPeripherals', GetPeripheralsViewSet, basename='getPeripherals')
router.register(r'getPrinters', GetPrintersViewSet, basename='getPrinters')
router.register(r'getEnclosures', GetEnclosuresViewSet, basename='getEnclosures')
router.register(r'getPdus', GetPdusViewSet, basename='getPdus')
router.register(r'getSoftwares', GetSoftwaresViewSet, basename='getSoftwares')
router.register(r'getNetworkequipments', GetNetworkequipmentsViewSet, basename='getNetworkequipments')
router.register(r'getPhones', GetPhonesViewSet, basename='getPhones')
router.register(r'getRacks', GetRacksViewSet, basename='getRacks')
router.register(r'getCables', GetCablesViewSet, basename='getCables')
router.register(r'getPassivedcequipments', GetPassivedcequipmentsViewSet, basename='getPassivedcequipments')
router.register(r'getConsumableitems', GetConsumableitemsViewSet, basename='getConsumableitems')
router.register(r'getCartridgeitems', GetCartridgeItemsViewSet, basename='getCartridgeitems')

#selects
router.register(r'getComputertypesSelect', computers.GetComputertypesSelectViewSet, basename='getComputertypesSelect')
router.register(r'getComputermodelsSelect', computers.GetComputermodelsSelectViewSet, basename='getComputermodelsSelect')
router.register(r'getLocationsSelect', locations.GetLocationsSelectViewSet, basename='getLocationsSelect')
router.register(r'getStatesSelect', states.GetStatesSelectViewSet, basename='getStatesSelect')
router.register(r'getManufacturersSelect', manufacturers.GetManufacturersSelectViewSet, basename='getManufacturersSelect')
router.register(r'getAutoupdatesystemsSelect', autoupdatesystems.GetAutoupdatesystemsSelectViewSet, basename='getAutoupdatesystemsSelect')
router.register(r'getNetworksSelect', networks.GetNetworksSelectViewSet, basename='getNetworksSelect')
router.register(r'getSnmpcredentialsSelect', snmpcredentials.GetSnmpcredentialsSelectViewSet, basename='getSnmpcredentialsSelect')
router.register(r'getGroupsSelect', groups.GetGroupsSelectViewSet, basename='getGroupsSelect')
router.register(r'getGroupInChargeSelect', groups.GetGroupInChargeSelectViewSet, basename='getGroupInChargeSelect')
router.register(r'getUsersSelect', users.GetUsersSelectViewSet, basename='getUsersSelect')
router.register(r'getUserInChargeSelect', users.GetTechInChargeSelectViewSet, basename='getUserInChargeSelect')
router.register(r'getNetworkequipmenttypesSelect', networkequipments.GetNetworkequipmenttypesSelectViewSet, basename='getNetworkequipmenttypesSelect')
router.register(r'getNetworkequipmentmodelsSelect', networkequipments.GetNetworkequipmentmodelsSelectViewSet, basename='getNetworkequipmentmodelsSelect')
router.register(r'getDevicesimcardsSelect', simcards.GetDevicesimcardsSelectViewSet, basename='getDevicesimcardsSelect')
router.register(r'getLinesSelect', simcards.GetLinesSelectViewSet, basename='getLinesSelect')
