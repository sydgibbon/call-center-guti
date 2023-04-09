from rest_framework import viewsets, views, permissions, status  # import de ViewSets
from assets.serializers import *  # import de todos los serializers,
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

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Users.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Computers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MonitorsViewSet(viewsets.ModelViewSet):
    queryset = Monitors.objects.all()
    serializer_class = MonitorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Monitors.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = SoftwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwares.objects.filter(id__in=ids)
            queryset.delete()
        # Desde aca empezo fran
        return Response(status=status.HTTP_204_NO_CONTENT)


class NetworkequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipments.objects.all()
    serializer_class = NetworkequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networkequipments.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PrintersViewSet(viewsets.ModelViewSet):
    queryset = Printers.objects.all()
    serializer_class = PrintersSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Printers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartridgesViewSet(viewsets.ModelViewSet):
    queryset = Cartridges.objects.all()
    serializer_class = CartridgesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cartridges.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConsumablesViewSet(viewsets.ModelViewSet):
    queryset = Consumables.objects.all()
    serializer_class = ConsumablesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Consumables.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhonesViewSet(viewsets.ModelViewSet):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phones.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RacksViewSet(viewsets.ModelViewSet):
    queryset = Racks.objects.all()
    serializer_class = RacksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Racks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EnclosuresViewSet(viewsets.ModelViewSet):
    queryset = Enclosures.objects.all()
    serializer_class = EnclosuresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Enclosures.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PdusViewSet(viewsets.ModelViewSet):
    queryset = Pdus.objects.all()
    serializer_class = PdusSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Pdus.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PdustypesViewSet(viewsets.ModelViewSet):
    queryset = Pdutypes.objects.all()
    serializer_class = PdutypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Pdutypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PdumodelsViewSet(viewsets.ModelViewSet):
    queryset = Pdumodels.objects.all()
    serializer_class = PdumodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Pdumodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PassivedcequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipments.objects.all()
    serializer_class = PassivedcequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipments.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PassivedcequipmenttypesViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipmenttypes.objects.all()
    serializer_class = PassivedcequipmenttypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipmenttypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PassivedcequipmentmodelsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipmentmodels.objects.all()
    serializer_class = PassivedcequipmentmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipmentmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UnmanagedsViewSet(viewsets.ModelViewSet):
    queryset = Unmanageds.objects.all()
    serializer_class = UnmanagedsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Unmanageds.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CablesViewSet(viewsets.ModelViewSet):
    queryset = Cables.objects.all()
    serializer_class = CablesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cables.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcards.objects.all()
    serializer_class = DevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesimcards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComputermodelsViewSet(viewsets.ModelViewSet):
    queryset = Computermodels.objects.all()
    serializer_class = ComputermodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Computermodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComputersItemsViewSet(viewsets.ModelViewSet):
    queryset = ComputersItems.objects.all()
    serializer_class = ComputersItemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ComputersItems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComputertypesViewSet(viewsets.ModelViewSet):
    queryset = Computertypes.objects.all()
    serializer_class = ComputertypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Computertypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MonitormodelsViewSet(viewsets.ModelViewSet):
    queryset = Monitormodels.objects.all()
    serializer_class = MonitormodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Monitormodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MonitortypesViewSet(viewsets.ModelViewSet):
    queryset = Monitortypes.objects.all()
    serializer_class = MonitortypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Monitortypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwarecategoriesViewSet(viewsets.ModelViewSet):
    queryset = Softwarecategories.objects.all()
    serializer_class = SoftwarecategoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwarecategories.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwarelicensesViewSet(viewsets.ModelViewSet):
    queryset = Softwarelicenses.objects.all()
    serializer_class = SoftwarelicensesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwarelicenses.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwareversionsViewSet(viewsets.ModelViewSet):
    queryset = Softwareversions.objects.all()
    serializer_class = SoftwareversionsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwareversions.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NetworkequipmentmodelsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipmentmodels.objects.all()
    serializer_class = NetworkequipmentmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networkequipmentmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NetworkequipmenttypesViewSet(viewsets.ModelViewSet):
    queryset = Networkequipmenttypes.objects.all()
    serializer_class = NetworkequipmenttypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networkequipmenttypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PrintermodelsViewSet(viewsets.ModelViewSet):
    queryset = Printermodels.objects.all()
    serializer_class = PrintermodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Printermodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PrintertypesViewSet(viewsets.ModelViewSet):
    queryset = Printertypes.objects.all()
    serializer_class = PrintertypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Printertypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PrintersCartridgeinfosViewSet(viewsets.ModelViewSet):
    queryset = PrintersCartridgeinfos.objects.all()
    serializer_class = PrintersCartridgeinfosSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = PrintersCartridgeinfos.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartridgeitemsViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitems.objects.all()
    serializer_class = CartridgeitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cartridgeitems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartridgeitemsPrintermodelsViewSet(viewsets.ModelViewSet):
    queryset = CartridgeitemsPrintermodels.objects.all()
    serializer_class = CartridgeitemsPrintermodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = CartridgeitemsPrintermodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartridgeitemtypesViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitemtypes.objects.all()
    serializer_class = CartridgeitemtypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cartridgeitemtypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConsumableitemsViewSet(viewsets.ModelViewSet):
    queryset = Consumableitems.objects.all()
    serializer_class = ConsumableitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Consumableitems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConsumableitemtypesViewSet(viewsets.ModelViewSet):
    queryset = Consumableitemtypes.objects.all()
    serializer_class = ConsumableitemtypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Consumableitemtypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhonemodelsViewSet(viewsets.ModelViewSet):
    queryset = Phonemodels.objects.all()
    serializer_class = PhonemodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phonemodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhonepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = Phonepowersupplies.objects.all()
    serializer_class = PhonepowersuppliesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phonepowersupplies.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhonetypesViewSet(viewsets.ModelViewSet):
    queryset = Phonetypes.objects.all()
    serializer_class = PhonetypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phonetypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsRacksViewSet(viewsets.ModelViewSet):
    queryset = ItemsRacks.objects.all()
    serializer_class = ItemsRacksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsRacks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsEnclosuresViewSet(viewsets.ModelViewSet):
    queryset = ItemsEnclosures.objects.all()
    serializer_class = ItemsEnclosuresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsEnclosures.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PdusPlugsViewSet(viewsets.ModelViewSet):
    queryset = PdusPlugs.objects.all()
    serializer_class = PdusPlugsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = PdusPlugs.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PdusRacksViewSet(viewsets.ModelViewSet):
    queryset = PdusRacks.objects.all()
    serializer_class = PdusRacksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = PdusRacks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CablestrandsViewSet(viewsets.ModelViewSet):
    queryset = Cablestrands.objects.all()
    serializer_class = CablestrandsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cablestrands.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CabletypesViewSet(viewsets.ModelViewSet):
    queryset = Cabletypes.objects.all()
    serializer_class = CabletypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cabletypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DevicesimcardtypesViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcardtypes.objects.all()
    serializer_class = DevicesimcardtypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesimcardtypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ItemsDevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesimcards.objects.all()
    serializer_class = ItemsDevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicesimcards.objects.filter(id__in=ids)
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


class PeripheralsViewSet(viewsets.ModelViewSet):
    queryset = Peripherals.objects.all()
    serializer_class = PeripheralsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Peripherals.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeripheralmodelsViewSet(viewsets.ModelViewSet):
    queryset = Peripheralmodels.objects.all()
    serializer_class = PeripheralmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Peripheralmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeripheraltypesViewSet(viewsets.ModelViewSet):
    queryset = Peripheraltypes.objects.all()
    serializer_class = PeripheraltypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Peripheraltypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AutoupdatesystemsViewSet(viewsets.ModelViewSet):
    queryset = Autoupdatesystems.objects.all()
    serializer_class = AutoupdatesystemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Autoupdatesystems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RackmodelsViewSet(viewsets.ModelViewSet):
    queryset = Rackmodels.objects.all()
    serializer_class = RackmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Rackmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RacktypesViewSet(viewsets.ModelViewSet):
    queryset = Racktypes.objects.all()
    serializer_class = RacktypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Racktypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EnclosuremodelsViewSet(viewsets.ModelViewSet):
    queryset = Enclosuremodels.objects.all()
    serializer_class = EnclosuremodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Enclosuremodels.objects.filter(id__in=ids)
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

class NetworksViewSet(viewsets.ModelViewSet):
    queryset = Networks.objects.all()
    serializer_class = NetworksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SnmpcredentialsViewSet(viewsets.ModelViewSet):
    queryset = Snmpcredentials.objects.all()
    serializer_class = SnmpcredentialsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Snmpcredentials.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ManufacturersViewSet(viewsets.ModelViewSet):
    queryset = Manufacturers.objects.all()
    serializer_class = ManufacturersSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Manufacturers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                
class DcroomsViewSet(viewsets.ModelViewSet):
    queryset = Dcrooms.objects.all()
    serializer_class = DcroomsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Dcrooms.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Locations.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class StatesViewSet(viewsets.ModelViewSet):
    queryset = States.objects.all()
    serializer_class = StatesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = States.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class OperatingsystemsViewSet(viewsets.ModelViewSet):
    queryset = Operatingsystems.objects.all()
    serializer_class = OperatingsystemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = States.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# tables
class GetComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = GetComputersSerializer
    permission_classes = (IsAuthenticated, AllowAny)

class GetMonitorsViewSet(viewsets.ModelViewSet):
    queryset = Monitors.objects.all()
    serializer_class = GetMonitorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
class GetDevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcards.objects.all()
    serializer_class = GetDevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
class GetPeripheralsViewSet(viewsets.ModelViewSet):
    queryset = Peripherals.objects.all()
    serializer_class = GetPeripheralsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
class GetPrintersViewSet(viewsets.ModelViewSet):
    queryset = Printers.objects.all()
    serializer_class = GetPrintersSerializer
    permission_classes = (IsAuthenticated, AllowAny)

class GetEnclosuresViewSet(viewsets.ModelViewSet):
    queryset = Enclosures.objects.all()
    serializer_class = GetEnclosuresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

class GetPdusViewSet(viewsets.ModelViewSet):
    queryset = Pdus.objects.all()
    serializer_class = GetPdusSerializer
    permission_classes = (IsAuthenticated, AllowAny)
class GetCartridgeItemsViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitems.objects.all()
    serializer_class = GetCartridgeItemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)


