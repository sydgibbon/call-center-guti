from rest_framework import serializers #import de serializers
from assets.models import * #import de todos los callcenterdata, proximamente se mueve a assets

class ComputersSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Computers #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicemotherboardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicemotherboards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicenetworkcardmodelsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicenetworkcardmodels #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicenetworkcardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicenetworkcards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicepcimodelsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicepcimodels #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicepcisSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicepcis #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicepowersuppliesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicepowersupplies #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicepowersupplymodelsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicepowersupplymodels #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DeviceprocessormodelsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Deviceprocessormodels #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DeviceprocessorsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Deviceprocessors #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicesensormodelsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicesensormodels #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicesensorsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicesensors #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicesensortypesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicesensortypes #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicesoundcardmodelsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicesoundcardmodels #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class DevicesoundcardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Devicesoundcards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicebatteriesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicebatteries #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicecamerasSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicecameras #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicecamerasImageformatsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicecamerasImageformats #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicecamerasImageresolutionsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicecamerasImageresolutions #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicecasesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicecases #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicecontrolsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicecontrols #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class IItemsDevicedrivesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = IItemsDevicedrives #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicefirmwaresSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicefirmwares #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicegenericsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicegenerics #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicegraphiccardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicegraphiccards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDeviceharddrivesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDeviceharddrives #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemItemsDevicememoriesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemItemsDevicememories #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicemotherboardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicemotherboards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicenetworkcardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicenetworkcards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicepcisSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicepcis #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicepowersuppliesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicepowersupplies #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDeviceprocessorsSerializer(serializers.ModelSerializer):  
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDeviceprocessors #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicesensorsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicesensors #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicesimcardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicesimcards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ItemsDevicesoundcardsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsDevicesoundcards #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model


