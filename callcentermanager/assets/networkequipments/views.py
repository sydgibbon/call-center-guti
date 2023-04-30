from assets.networkequipments.serializers import GetNetworkequipmenttypesSelectSerializer, GetNetworkequipmentmodelsSelectSerializer
from assets.models import Networkequipmenttypes, Networkequipmentmodels
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetNetworkequipmenttypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmenttypes = GetNetworkequipmenttypesSelectSerializer(Networkequipmenttypes.objects.all(), many=True) 
        return Response(networkequipmenttypes.data)

class GetNetworkequipmentmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmentmodels = GetNetworkequipmentmodelsSelectSerializer(Networkequipmentmodels.objects.all(), many=True) 
        return Response(networkequipmentmodels.data)