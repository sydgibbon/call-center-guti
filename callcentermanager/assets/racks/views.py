from assets.racks.serializers import GetRacktypesSelectSerializer, GetRackmodelsSelectSerializer, GetDcroomsSelectSerializer
from assets.models import Racktypes, Rackmodels, Dcrooms
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetRacktypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetRacktypesSelectSerializer(Racktypes.objects.all(), many=True) 
        return Response(states.data)
    
class GetRackmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetRackmodelsSelectSerializer(Rackmodels.objects.all(), many=True) 
        return Response(states.data)
    
class GetDcroomsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetDcroomsSelectSerializer(Dcrooms.objects.all(), many=True) 
        return Response(states.data)