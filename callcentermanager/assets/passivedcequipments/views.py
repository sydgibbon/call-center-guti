from assets.passivedcequipments.serializers import GetPassivedcequipmentsSelectSerializer, GetPassivedcequipmenttypesSelectSerializer, GetPassivedcequipmentmodelsSelectSerializer
from assets.models import Passivedcequipments, Passivedcequipmenttypes, Passivedcequipmentmodels
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPassivedcequipmentsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipments = GetPassivedcequipmentsSelectSerializer(Passivedcequipments.objects.all(), many=True) 
        return Response(passivedcequipments.data)

class GetPassivedcequipmenttypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipmenttypes = GetPassivedcequipmenttypesSelectSerializer(Passivedcequipmenttypes.objects.all(), many=True) 
        return Response(passivedcequipmenttypes.data)
    
class GetPassivedcequipmentmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipmentmodels = GetPassivedcequipmentmodelsSelectSerializer(Passivedcequipmentmodels.objects.all(), many=True) 
        return Response(passivedcequipmentmodels.data)