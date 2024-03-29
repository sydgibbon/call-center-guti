from rest_framework import viewsets, views, permissions, status  # import de ViewSets
from assets.generics.serializers import *  # import de todos los serializers,
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import login

# ViewSets para cada Serializer

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class DevicebatteriesViewSet(viewsets.ModelViewSet):
    queryset = Devicebatteries.objects.all()
    serializer_class = DevicebatteriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicebatteries.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicebatterymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicebatterymodels.objects.all()
    serializer_class = DevicebatterymodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicebatterymodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicebatterytypesViewSet(viewsets.ModelViewSet):
    queryset = Devicebatterytypes.objects.all()
    serializer_class = DevicebatterytypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicebatterytypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicecameramodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicecameramodels.objects.all()
    serializer_class = DevicecameramodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicecameramodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicecamerasViewSet(viewsets.ModelViewSet):
    queryset = Devicecameras.objects.all()
    serializer_class = DevicecamerasSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicecameras.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicecasemodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicecasemodels.objects.all()
    serializer_class = DevicecasemodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicecasemodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicecasesViewSet(viewsets.ModelViewSet):
    queryset = Devicecases.objects.all()
    serializer_class = DevicecasesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicecases.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicecasetypesViewSet(viewsets.ModelViewSet):
    queryset = Devicecasetypes.objects.all()
    serializer_class = DevicecasetypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicecasetypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicecontrolmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicecontrolmodels.objects.all()
    serializer_class = DevicecontrolmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicecontrolmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # Arranca Nata


class DevicecontrolsViewSet(viewsets.ModelViewSet):
    queryset = Devicecontrols.objects.all()
    serializer_class = DevicecontrolsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicecontrols.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicedrivemodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicedrivemodels.objects.all()
    serializer_class = DevicedrivemodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicedrivemodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicedrivesViewSet(viewsets.ModelViewSet):
    queryset = Devicedrives.objects.all()
    serializer_class = DevicedrivesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicedrives.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicefirmwaremodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwaremodels.objects.all()
    serializer_class = DevicefirmwaremodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicefirmwaremodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicefirmwaresViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwares.objects.all()
    serializer_class = DevicefirmwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicefirmwares.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicefirmwaretypesViewSet(viewsets.ModelViewSet):
    queryset = Devicefirmwaretypes.objects.all()
    serializer_class = DevicefirmwaretypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicefirmwaretypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicegenericmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicegenericmodels.objects.all()
    serializer_class = DevicegenericmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicegenericmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicegenericsViewSet(viewsets.ModelViewSet):
    queryset = Devicegenerics.objects.all()
    serializer_class = DevicegenericsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicegenerics.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicegenerictypesViewSet(viewsets.ModelViewSet):
    queryset = Devicegenerictypes.objects.all()
    serializer_class = DevicegenerictypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicegenerictypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicegraphiccardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicegraphiccardmodels.objects.all()
    serializer_class = DevicegraphiccardmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicegraphiccardmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicegraphiccardsViewSet(viewsets.ModelViewSet):
    queryset = Devicegraphiccards.objects.all()
    serializer_class = DevicegraphiccardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicegraphiccards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceharddrivemodelsViewSet(viewsets.ModelViewSet):
    queryset = Deviceharddrivemodels.objects.all()
    serializer_class = DeviceharddrivemodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Deviceharddrivemodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceharddrivesViewSet(viewsets.ModelViewSet):
    queryset = Deviceharddrives.objects.all()
    serializer_class = DeviceharddrivemodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Deviceharddrives.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicememoriesViewSet(viewsets.ModelViewSet):
    queryset = Devicememories.objects.all()
    serializer_class = DevicememoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicememories.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicememorymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicememorymodels.objects.all()
    serializer_class = DevicememorymodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicememorymodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicememorytypesViewSet(viewsets.ModelViewSet):
    queryset = Devicememorytypes.objects.all()
    serializer_class = DevicememorytypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicememorytypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicemotherboardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicemotherboardmodels.objects.all()
    serializer_class = DevicemotherboardmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicemotherboardmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset = Devicemotherboards.objects.all()
    serializer_class = DevicemotherboardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicemotherboards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicenetworkcardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicenetworkcardmodels.objects.all()
    serializer_class = DevicenetworkcardmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicenetworkcardmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicenetworkcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicenetworkcards.objects.all()
    serializer_class = DevicenetworkcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicenetworkcards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicepcimodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicepcimodels.objects.all()
    serializer_class = DevicepcimodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicepcimodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicepcisViewSet(viewsets.ModelViewSet):
    queryset = Devicepcis.objects.all()
    serializer_class = DevicepcisSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicepcis.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = Devicepowersupplies.objects.all()
    serializer_class = DevicepowersuppliesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicepowersupplies.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicepowersupplymodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicepowersupplymodels.objects.all()
    serializer_class = DevicepowersupplymodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicepowersupplymodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceprocessormodelsViewSet(viewsets.ModelViewSet):
    queryset = Deviceprocessormodels.objects.all()
    serializer_class = DeviceprocessormodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Deviceprocessormodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceprocessorsViewSet(viewsets.ModelViewSet):
    queryset = Deviceprocessors.objects.all()
    serializer_class = DeviceprocessorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Deviceprocessors.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicesensormodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicesensormodels.objects.all()
    serializer_class = DevicesensormodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesensormodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicesensorsViewSet(viewsets.ModelViewSet):
    queryset = Devicesensors.objects.all()
    serializer_class = DevicesensorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesensors.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicesensortypesViewSet(viewsets.ModelViewSet):
    queryset = Devicesensortypes.objects.all()
    serializer_class = DevicesensortypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesensortypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicesoundcardmodelsViewSet(viewsets.ModelViewSet):
    queryset = Devicesoundcardmodels.objects.all()
    serializer_class = DevicesoundcardmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesoundcardmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicesoundcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesoundcards.objects.all()
    serializer_class = DevicesoundcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesoundcards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicebatteriesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicebatteries.objects.all()
    serializer_class = ItemsDevicebatteriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicebatteries.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicecamerasViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecameras.objects.all()
    serializer_class = ItemsDevicecamerasSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicecameras.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicecamerasImageformatsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecamerasImageformats.objects.all()
    serializer_class = ItemsDevicecamerasImageformatsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicecamerasImageformats.objects.filter(
                id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicecamerasImageresolutionsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecamerasImageresolutions.objects.all()
    serializer_class = ItemsDevicecamerasImageresolutionsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicecamerasImageresolutions.objects.filter(
                id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicecasesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecases.objects.all()
    serializer_class = ItemsDevicecasesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicecases.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicecontrolsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicecontrols.objects.all()
    serializer_class = ItemsDevicecontrolsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicecontrols.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicedrivesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicedrives.objects.all()
    serializer_class = ItemsDevicedrivesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicedrives.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicefirmwaresViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicefirmwares.objects.all()
    serializer_class = ItemsDevicefirmwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicefirmwares.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicegenericsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicegenerics.objects.all()
    serializer_class = ItemsDevicegenericsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicegenerics.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicegraphiccardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicegraphiccards.objects.all()
    serializer_class = ItemsDevicegraphiccardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicegraphiccards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDeviceharddrivesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDeviceharddrives.objects.all()
    serializer_class = ItemsDeviceharddrivesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDeviceharddrives.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicememoriesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicememories.objects.all()
    serializer_class = ItemsDevicememoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicememories.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicemotherboards.objects.all()
    serializer_class = ItemsDevicemotherboardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicemotherboards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicenetworkcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicenetworkcards.objects.all()
    serializer_class = ItemsDevicenetworkcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicenetworkcards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicepcisViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicepcis.objects.all()
    serializer_class = ItemsDevicepcisSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicepcis.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicepowersupplies.objects.all()
    serializer_class = ItemsDevicepowersuppliesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicepowersupplies.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDeviceprocessorsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDeviceprocessors.objects.all()
    serializer_class = ItemsDeviceprocessorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDeviceprocessors.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsDevicesensorsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesensors.objects.all()
    serializer_class = ItemsDevicesensorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicesensors.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemsDevicesoundcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesoundcards.objects.all()
    serializer_class = ItemsDevicesoundcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicesoundcards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EntitiesViewSet(viewsets.ModelViewSet):
    queryset = Entities.objects.all()
    serializer_class = EntitiesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Entities.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# tables
