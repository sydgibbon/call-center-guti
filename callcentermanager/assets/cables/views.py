from assets.cables.serializers import GetCabletypesSelectSerializer, GetCablestrandsSelectSerializer, GetSocketsSelectSerializer, GetSocketmodelsSelectSerializer
from assets.models import Cabletypes, Cablestrands, Sockets, Socketmodels
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetCabletypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cabletypes = GetCabletypesSelectSerializer(Cabletypes.objects.all(), many=True) 
        return Response(cabletypes.data)
    
class GetCablestrandsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cablestrands = GetCablestrandsSelectSerializer(Cablestrands.objects.all(), many=True) 
        return Response(cablestrands.data)
    
class GetSocketsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        sockets = GetSocketsSelectSerializer(Sockets.objects.all(), many=True) 
        return Response(sockets.data)
        
class GetSocketmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        socketmodels = GetSocketmodelsSelectSerializer(Socketmodels.objects.all(), many=True) 
        return Response(socketmodels.data)