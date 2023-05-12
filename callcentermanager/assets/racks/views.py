from assets.racks.serializers import GetRacktypesSelectSerializer, GetRackmodelsSelectSerializer, GetDcroomsSelectSerializer, GetRacksCountSerializer
from assets.models import Racktypes, Rackmodels, Dcrooms, Racks
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetRacktypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        racktypes = GetRacktypesSelectSerializer(Racktypes.objects.all(), many=True) 
        return Response(racktypes.data)
    
class GetRackmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        rackmodels = GetRackmodelsSelectSerializer(Rackmodels.objects.all(), many=True) 
        return Response(rackmodels.data)
    
class GetDcroomsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        dcrooms = GetDcroomsSelectSerializer(Dcrooms.objects.all(), many=True) 
        return Response(dcrooms.data)
    
class GetRacksCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        racksCount = GetRacksCountSerializer(Racks.objects.count())

        return Response(racksCount.data)