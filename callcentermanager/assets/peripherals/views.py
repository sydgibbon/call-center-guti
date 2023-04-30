from assets.peripherals.serializers import GetPeripheralsSelectSerializer, GetPeripheraltypesSelectSerializer, GetPeripheralmodelsSelectSerializer
from assets.models import Peripherals, Peripheraltypes, Peripheralmodels
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPeripheralsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        peripherals = GetPeripheralsSelectSerializer(Peripherals.objects.all(), many=True)

        return Response(peripherals.data)

class GetPeripheraltypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        peripheraltypes = GetPeripheraltypesSelectSerializer(Peripheraltypes.objects.all(), many=True)

        return Response(peripheraltypes.data)
    
class GetPeripheralmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        peripheralmodels = GetPeripheralmodelsSelectSerializer(Peripheralmodels.objects.all(), many=True)

        return Response(peripheralmodels.data)