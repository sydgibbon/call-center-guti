from rest_framework.routers import DefaultRouter

from assets.generics.views import *
from assets.locations import views as locations
from assets.states import views as states
from assets.manufacturers import views as manufacturers
from assets.autoupdatesystems import views as autoupdatesystems
from assets.networks import views as networks
from assets.snmpcredentials import views as snmpcredentials
from assets.users import views as users
from assets.groups import views as groups
from assets.peripherals import views as peripherals
from assets.networkequipments import views as networkequipments
from assets.cables import views as cables
from assets.simcards import views as simcards
from assets.printers import views as printers
from assets.consumables import views as consumableitems
from assets.passivedcequipments import views as passivedcequipments
from assets.phones import views as phones
from assets.racks import views as racks
from assets.enclosures import views as enclosures
from assets.pdus import views as pdus
from assets.computers import views as computers
from assets.monitors import views as monitors
from assets.softwares import views as softwares
from assets.cartridges import views as cartridges
from assets.unmanageds import views as unmanageds

router=DefaultRouter()
router.register(r'computers', computers.ComputersViewSet, basename='computers')
router.register(r'monitors', monitors.MonitorsViewSet, basename='monitors')
router.register(r'softwares', softwares.SoftwaresViewSet, basename='softwares')
router.register(r'networkequipments', networkequipments.NetworkequipmentsViewSet, basename='networkequipments')
router.register(r'printers', printers.PrintersViewSet, basename='printers')
router.register(r'cartridges', cartridges.CartridgesViewSet, basename='cartridges')
router.register(r'consumables', consumableitems.ConsumablesViewSet, basename='consumables')
router.register(r'phones', phones.PhonesViewSet, basename='phones')
router.register(r'racks', racks.RacksViewSet, basename='racks')
router.register(r'enclosures', enclosures.EnclosuresViewSet, basename='enclosures')
router.register(r'pdus', pdus.PdusViewSet, basename='pdus')
router.register(r'pdutypes', pdus.PdusViewSet, basename='pdutypes')
router.register(r'pdumodels', pdus.PdusViewSet, basename='pdumodels')
router.register(r'passivedcequipments', passivedcequipments.PassivedcequipmentsViewSet, basename='passivedcequipments')
router.register(r'passivedcequipmentmodels', passivedcequipments.PassivedcequipmentmodelsViewSet, basename='passivedcequipmentmodels')
router.register(r'passivedcequipmenttypes', passivedcequipments.PassivedcequipmenttypesViewSet, basename='passivedcequipmenttypes')
router.register(r'unmanageds', unmanageds.UnmanagedsViewSet , basename='unmanageds')
router.register(r'cables', cables.CablesViewSet, basename='cables')
router.register(r'devicesimcards', simcards.DevicesimcardsViewSet, basename='devicesimcards')
router.register(r'computermodels', computers.ComputermodelsViewSet, basename='computermodels')
router.register(r'computersitems', computers.ComputersItemsViewSet, basename='computersitems')
router.register(r'computertypes', computers.ComputertypesViewSet, basename='computertypes')
router.register(r'monitormodels', monitors.MonitormodelsViewSet, basename='monitormodels')
router.register(r'monitortypes', monitors.MonitortypesViewSet, basename='monitortypes')
router.register(r'softwarecategories', softwares.SoftwarecategoriesViewSet, basename='softwarecategories')
router.register(r'softwarelicenses', softwares.SoftwarelicensesViewSet, basename='softwarelicenses')
router.register(r'softwareversions', softwares.SoftwareversionsViewSet, basename='softwareversions')
router.register(r'networkequipmentmodels', networkequipments.NetworkequipmentmodelsViewSet, basename='networkequipmentmodels')
router.register(r'networkequipmenttypes', networkequipments.NetworkequipmenttypesViewSet, basename='networkequipmenttypes')
router.register(r'printermodels', printers.PrintermodelsViewSet, basename='printermodels')
router.register(r'printertypes', printers.PrintertypesViewSet, basename='printertypes')
router.register(r'printerscartridgeinfos', printers.PrintersCartridgeinfosViewSet, basename='printerscartridgeinfos')
router.register(r'cartridgeitems', cartridges.CartridgeitemsViewSet, basename='cartridgeitems')
router.register(r'cartridgeitemsprintermodels', cartridges.CartridgeitemsPrintermodelsViewSet, basename='cartridgeitemsprintermodels')
router.register(r'cartridgeitemtypes', cartridges.CartridgeitemtypesViewSet, basename='cartridgeitemtypes')
router.register(r'consumableitems', consumableitems.ConsumableitemsViewSet, basename='consumableitems')
router.register(r'consumableitemtypes', consumableitems.ConsumableitemtypesViewSet, basename='consumableitemtypes')
router.register(r'phonemodels', phones.PhonemodelsViewSet, basename='phonemodels')
router.register(r'phonepowersupplies', phones.PhonepowersuppliesViewSet, basename='phonepowersupplies')
router.register(r'phonetypes', phones.PhonetypesViewSet, basename='phonetypes')
router.register(r'itemsracks', racks.ItemsRacksViewSet, basename='itemsracks')
router.register(r'itemsenclosures', enclosures.ItemsEnclosuresViewSet, basename='itemsenclosures')
router.register(r'pdusplugs', pdus.PdusPlugsViewSet, basename='pdusplugs')
router.register(r'pdusracks', pdus.PdusRacksViewSet, basename='pdusracks')
router.register(r'cablestrands', cables.CablestrandsViewSet, basename='cablestrands')
router.register(r'cabletypes', cables.CabletypesViewSet, basename='cabletypes')
router.register(r'devicesimcardtypes', simcards.DevicesimcardtypesViewSet, basename='devicesimcardtypes')
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
router.register(r'itemsdevicesimcards', simcards.ItemsDevicesimcardsViewSet, basename='itemsdevicesimcards')
router.register(r'itemsdevicesoundcards', ItemsDevicesoundcardsViewSet, basename='itemsdevicesoundcards')
router.register(r'peripherals', peripherals.PeripheralsViewSet, basename='peripherals')
router.register(r'peripheralmodels', peripherals.PeripheralmodelsViewSet, basename='peripheralmodels')
router.register(r'peripheraltypes', peripherals.PeripheraltypesViewSet, basename='peripheraltypes')
router.register(r'autoupdatesystems', autoupdatesystems.AutoupdatesystemsViewSet, basename='autoupdatesystems')
router.register(r'rackmodels', racks.RackmodelsViewSet, basename='rackmodels')
router.register(r'racktypes', racks.RacktypesViewSet, basename='racktypes')
router.register(r'enclosuremodels', enclosures.EnclosuremodelsViewSet, basename='enclosuremodels')
router.register(r'entities', EntitiesViewSet, basename='entities')
router.register(r'networks', networks.NetworksViewSet, basename='networks')
router.register(r'snmpcredentials', snmpcredentials.SnmpcredentialsViewSet, basename='snmpcredentials')
router.register(r'manufacturers', manufacturers.ManufacturersViewSet, basename='manufacturers')
router.register(r'dcrooms', racks.DcroomsViewSet, basename='dcrooms')
router.register(r'locations', locations.LocationsViewSet, basename='locations')
router.register(r'states', states.StatesViewSet, basename='states')
router.register(r'users', users.UsersViewSet, basename='users')
router.register(r'operatingsystems', computers.OperatingsystemsViewSet, basename='operatingsystems')

# tables
router.register(r'getComputers', computers.GetComputersViewSet, basename='getComputers')
router.register(r'getMonitors', monitors.GetMonitorsViewSet, basename='getMonitors')
router.register(r'getDevicesimcards', simcards.GetDevicesimcardsViewSet, basename='getDevicesimcards')
router.register(r'getPeripherals', peripherals.GetPeripheralsViewSet, basename='getPeripherals')
router.register(r'getPrinters', printers.GetPrintersViewSet, basename='getPrinters')
router.register(r'getEnclosures', enclosures.GetEnclosuresViewSet, basename='getEnclosures')
router.register(r'getPdus', pdus.GetPdusViewSet, basename='getPdus')
router.register(r'getSoftwares', softwares.GetSoftwaresViewSet, basename='getSoftwares')
router.register(r'getNetworkequipments', networkequipments.GetNetworkequipmentsViewSet, basename='getNetworkequipments')
router.register(r'getPhones', phones.GetPhonesViewSet, basename='getPhones')
router.register(r'getRacks', racks.GetRacksViewSet, basename='getRacks')
router.register(r'getCables', cables.GetCablesViewSet, basename='getCables')
router.register(r'getPassivedcequipments', passivedcequipments.GetPassivedcequipmentsViewSet, basename='getPassivedcequipments')
router.register(r'getConsumableitems', consumableitems.GetConsumableitemsViewSet, basename='getConsumableitems')
router.register(r'getCartridgeitems', cartridges.GetCartridgeItemsViewSet, basename='getCartridgeitems')

#selects
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
router.register(r'getNetworkequipmentsSelect', networkequipments.GetNetworkequipmentsSelectViewSet, basename='getNetworkequipmentsSelect')
router.register(r'getNetworkequipmenttypesSelect', networkequipments.GetNetworkequipmenttypesSelectViewSet, basename='getNetworkequipmenttypesSelect')
router.register(r'getNetworkequipmentmodelsSelect', networkequipments.GetNetworkequipmentmodelsSelectViewSet, basename='getNetworkequipmentmodelsSelect')
router.register(r'getDevicesimcardsSelect', simcards.GetDevicesimcardsSelectViewSet, basename='getDevicesimcardsSelect')
router.register(r'getLinesSelect', simcards.GetLinesSelectViewSet, basename='getLinesSelect')
router.register(r'getPeripheralsSelect', peripherals.GetPeripheralsSelectViewSet , basename='getPeripheralsSelect')
router.register(r'getPeripheraltypesSelect', peripherals.GetPeripheraltypesSelectViewSet , basename='getPeripheraltypesSelect')
router.register(r'getPeripheralmodelsSelect', peripherals.GetPeripheralmodelsSelectViewSet , basename='getPeripheralmodelsSelect')
router.register(r'getCabletypesSelect', cables.GetCabletypesSelectViewSet, basename='getCabletypesSelect')
router.register(r'getCablestrandsSelect', cables.GetCablestrandsSelectViewSet, basename='getCablestrandsSelect')
router.register(r'getSocketsSelect', cables.GetSocketsSelectViewSet, basename='getSocketsSelect')
router.register(r'getSocketmodelsSelect', cables.GetSocketmodelsSelectViewSet, basename='getSocketmodelsSelect')
router.register(r'getPrintersSelect', printers.GetPrintersSelectViewSet, basename='getPrintersSelect')
router.register(r'getPrintermodelsSelect', printers.GetPrintermodelsSelectViewSet, basename='getPrintermodelsSelect')
router.register(r'getPrintertypesSelect', printers.GetPrintertypesSelectViewSet, basename='getPrintertypesSelect')
router.register(r'getConsumableitemtypesSelect', consumableitems.GetConsumableitemtypesSelectViewSet, basename='getConsumableitemtypesSelect')
router.register(r'getPassivedcequipmentsSelect', passivedcequipments.GetPassivedcequipmentsSelectViewSet, basename='getPassivedcequipmentsSelect')
router.register(r'getPassivedcequipmenttypesSelect', passivedcequipments.GetPassivedcequipmenttypesSelectViewSet, basename='getPassivedcequipmenttypesSelect')
router.register(r'getPassivedcequipmentmodelsSelect', passivedcequipments.GetPassivedcequipmentmodelsSelectViewSet, basename='getPassivedcequipmentmodelsSelect')
router.register(r'getNetworkequipmenttypesSelect', networkequipments.GetNetworkequipmenttypesSelectViewSet, basename='getNetworkequipmenttypes')
router.register(r'getNetworkequipmentmodelsSelect', networkequipments.GetNetworkequipmentmodelsSelectViewSet, basename='getNetworkequipmentmodels')
router.register(r'getPhonesSelect', phones.GetPhonesSelectViewSet, basename='getPhones')
router.register(r'getPhonemodelsSelect', phones.GetPhonemodelsSelectViewSet, basename='getPhonemodels')
router.register(r'getPhonetypesSelect', phones.GetPhonetypesSelectViewSet, basename='getPhonetypes')
router.register(r'getPhonepowersuppliesSelect', phones.GetPhonepowersuppliesSelectViewSet, basename='getPhonepowersupplies')
router.register(r'getRacktypesSelect', racks.GetRacktypesSelectViewSet, basename='getRacktypes')
router.register(r'getRackmodelsSelect', racks.GetRackmodelsSelectViewSet, basename='getRackmodels')
router.register(r'getDcroomsSelect', racks.GetDcroomsSelectViewSet, basename='getDcrooms')
router.register(r'getEnclosuremoldesSelect', enclosures.GetEnclosuremodelsSelectViewSet, basename='getEnclosuremodels')
router.register(r'getPdutypesSelect', pdus.GetPdutypesSelectViewSet, basename='getPdutypes')
router.register(r'getPdumodelsSelect', pdus.GetPdumodelsSelectViewSet, basename='getPdumodels')
router.register(r'getEnclosuremodelsSelect', enclosures.GetEnclosuremodelsSelectViewSet, basename='getEnclosuremodels')
router.register(r'getComputersSelect', computers.GetComputersSelectViewSet, basename='getComputersSelect')
router.register(r'getComputertypesSelect', computers.GetComputertypesSelectViewSet, basename='getComputertypesSelect')
router.register(r'getComputermodelsSelect', computers.GetComputermodelsSelectViewSet, basename='getComputermodelsSelect')
router.register(r'getMonitortypesSelect', monitors.GetMonitortypesSelectViewSet, basename='getMonitortypesSelect')
router.register(r'getMonitormodelsSelect', monitors.GetMonitormodelsSelectViewSet, basename='getMonitormodelsSelect')
router.register(r'getSoftwarecategoriesSelect', softwares.GetSoftwarecategoriesSelectViewSet, basename='getSoftwarecategoriesSelect')
router.register(r'getCartridgeitemtypesSelect', cartridges.GetCartridgeitemtypesSelectViewSet, basename='getCartridgeitemtypesSelect')

# Dashboard Count
router.register(r'getComputersCount', computers.GetComputersCountViewSet, basename='getComputersCount')
router.register(r'getMonitorsCount', monitors.GetMonitorsCountViewSet, basename='getMonitorsCount')
router.register(r'getSoftwaresCount', softwares.GetSoftwaresCountViewSet, basename='getSoftwaresCount')
router.register(r'getSoftwarelicensesCount', softwares.GetSoftwarelicensesCountViewSet, basename='getSoftwarelicensesCount')
router.register(r'getNetworkequipmentsCount', networks.GetNetworkequipmentsCountViewSet, basename='getNetworkequipmentsCount')
router.register(r'getPrintersCount', printers.GetPrintersCountViewSet, basename='getPrintersCount')
router.register(r'getRacksCount', racks.GetRacksCountViewSet, basename='getRacksCount')
router.register(r'getPdusCount', pdus.GetPdusCountViewSet, basename='getPdusCount')
router.register(r'getEnclosuresCount', enclosures.GetEnclosuresCountViewSet, basename='getEnclosuresCount')
router.register(r'getPhonesCount', phones.GetPhonesCountViewSet, basename='getPhonesCount')

# Dashboard Graphs
router.register(r'getComputersByStates', computers.GetComputersCountByStatesViewSet, basename='getComputersByStates')
router.register(r'getComputersByManufacturers', computers.GetComputersCountByManufacturersViewSet, basename='getComputersByManufacturers')
router.register(r'getComputersByComputertypes', computers.GetComputersCountByComputertypesViewSet, basename='getComputersByComputertypes')
router.register(r'getNetworkequipmentsByManufacturers', networks.GetNetworkequipmentsCountByManufacturersViewSet, basename='getNetworkequipmentsByManufacturers')
router.register(r'getMonitorsByManufacturers', monitors.GetMonitorsCountByManufacturersViewSet, basename='getMonitorsByManufacturers')

# Asset Lists
router.register(r'getComputersList', computers.GetComputersListViewSet, basename='getComputersList')
router.register(r'getMonitorsList', monitors.GetMonitorsListViewSet, basename='getMonitorsList')
router.register(r'getSoftwaresList', softwares.GetSoftwaresListViewSet, basename='getSoftwaresList')
router.register(r'getNetworkequipmentsList', networkequipments.GetNetworkequipmentsListViewSet, basename='getNetworkequipmentsList')
router.register(r'getPrintersList', printers.GetPrintersListViewSet, basename='getPrintersList')
router.register(r'getCartridgeitemsList', cartridges.GetCartridgeitemsListViewSet, basename='getCartridgeitemsList')
router.register(r'getConsumableitemsList', consumableitems.GetConsumableitemsListViewSet, basename='getConsumableitemsList')
router.register(r'getPhonesList', phones.GetPhonesListViewSet, basename='getPhonesList')
router.register(r'getRacksList', racks.GetRacksListViewSet, basename='getRacksList')
router.register(r'getEnclosuresList', enclosures.GetEnclosuresListViewSet, basename='getEnclosuresList')
router.register(r'getPdusList', pdus.GetPdusListViewSet, basename='getPdusList')
router.register(r'getPassivedcequipmentsList', passivedcequipments.GetPassivedcequipmentsListViewSet, basename='getPassivedcequipmentsList')
router.register(r'getUnmanagedsList', unmanageds.GetUnmanagedsListViewSet, basename='getUnmanagedsList')
router.register(r'getCablesList', cables.GetCablesListViewSet, basename='getCablesList')
router.register(r'getDevicesimcardsList', simcards.GetDevicesimcardsListViewSet, basename='getDevicesimcardsList')
router.register(r'getPeripheralsList', peripherals.GetPeripheralsListViewSet, basename='getPeripheralsList')

#post-assets
router.register(r'createComputer', computers.CreateComputerViewSet, basename='createComputer')
router.register(r'createMonitor', monitors.CreateMonitorViewSet, basename='createMonitor')
router.register(r'createSoftware', softwares.CreateSoftwareViewSet, basename='createSoftware')
router.register(r'createNetworkequipment', networkequipments.CreateNetworkequipmentViewSet, basename='createNetworkequipment')
router.register(r'createPrinter', printers.CreatePrinterViewSet, basename='createPrinter')
router.register(r'createCartridgeitem', cartridges.CreateCartridgeitemViewSet, basename='createCartridgeitem')
router.register(r'createPhone', phones.CreatePhoneViewSet, basename='createPhone')
router.register(r'createRack', racks.CreateRackViewSet, basename='createRack')
router.register(r'createEnclosure', enclosures.CreateEnclosureViewSet, basename='createEnclosure')
router.register(r'createPdu', pdus.CreatePduViewSet, basename='createPdu')
router.register(r'createPassivedcequipment', passivedcequipments.CreatePassivedcequipmentViewSet, basename='createPassivedcequipment')
router.register(r'createCable', cables.CreateCableViewSet, basename='createCable')
router.register(r'createDevicesimcard', simcards.CreateDevicesimcardViewSet, basename='createDevicesimcard')
router.register(r'createPeripheral', peripherals.CreatePeripheralViewSet, basename='createPeripheral')

# Assets by id
router.register(r'getComputersById', computers.GetComputersByIdViewSet, basename='getComputersById')
router.register(r'getMonitorsById', monitors.GetMonitorsByIdViewSet, basename='getMonitorsById')
router.register(r'getSoftwaresById', softwares.GetSoftwaresByIdViewSet, basename='getSoftwaresById')
router.register(r'getNetworkequipmentsById', networkequipments.GetNetworkequipmentsByIdViewSet, basename='getNetworkequipmentsById')
router.register(r'getPeripheralsById', peripherals.GetPeripheralsByIdViewSet, basename='getPeripheralsById')
router.register(r'getPrintersById', printers.GetPrintersByIdViewSet, basename='getPrintersById')
router.register(r'getCartridgeitemsById', cartridges.GetCartridgeitemsByIdViewSet, basename='getCartridgeitemsById')
router.register(r'getConsumableitemsById', consumableitems.GetConsumableitemsByIdViewSet, basename='getConsumableitemsById')
router.register(r'getPhonesById', phones.GetPhonesByIdViewSet, basename='getPhonesById')
router.register(r'getRacksById', racks.GetRacksByIdViewSet, basename='getRacksById')
router.register(r'getEnclosuresById', enclosures.GetEnclosuresByIdViewSet, basename='getEnclosuresById')
router.register(r'getPdusById', pdus.GetPdusByIdViewSet, basename='getPdusById')
router.register(r'getPassivedcequipmentsById', passivedcequipments.GetPassivedcequipmentsByIdViewSet, basename='getPassivedcequipmentsById')
router.register(r'getItemsDevicesimcardsById', simcards.GetItemsDevicesimcardsByIdViewSet, basename='getItemsDevicesimcardsById')
router.register(r'getCablesById', cables.GetCablesByIdViewSet, basename='getCablesById')

# Update Assets by id

router.register(r'updateComputerById', computers.UpdateComputerByIdViewSet, basename='updateComputerById')
router.register(r'updateCableById', cables.UpdateCableByIdViewSet, basename='updateCableById')
router.register(r'updateEnclosureById', enclosures.UpdateEnclosureByIdViewSet, basename='updateEnclosureById')
router.register(r'updateMonitorById', monitors.UpdateMonitorByIdViewSet, basename='updateMonitorById')
router.register(r'updateNetworkequipmentById', networkequipments.UpdateNetworkequipmentByIdViewSet, basename='updateNetworkequipmentById')
router.register(r'updatePrinterById', printers.UpdatePrinterByIdViewSet, basename='updatePrinterById')
router.register(r'updatePhoneById', phones.UpdatePhoneByIdViewSet, basename='updatePhoneById')
router.register(r'updatePeripheralById', peripherals.UpdatePeripheralByIdViewSet, basename='updatePeripheralById')
router.register(r'updateSoftwareById', softwares.UpdateSoftwareByIdViewSet, basename='updateSoftwareById')
router.register(r'updateDevicesimcardById', simcards.UpdateDevicesimcardByIdViewSet, basename='updateDevicesimcardById')
router.register(r'updateRackById', racks.UpdateRackByIdViewSet, basename='updateRackById')
router.register(r'updatePduById', pdus.UpdatePduByIdViewSet, basename='updatePduById')
router.register(r'updateCartridgeitemById', cartridges.UpdateCartridgeitemByIdViewSet, basename='updateCartridgeitemById')
router.register(r'updatePassivedcequipmentById', passivedcequipments.UpdatePassivedcequipmentByIdViewSet, basename='updatePassivedcequipmentById')
