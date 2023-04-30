from assets.computers.serializers import GetComputertypesSelectSerializer, GetComputermodelsSelectSerializer
from assets.models import Computertypes, Computermodels
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetComputertypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computertypes = GetComputertypesSelectSerializer(Computertypes.objects.all(), many=True)

        return Response(computertypes.data)
    
class GetComputermodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computermodels = GetComputermodelsSelectSerializer(Computermodels.objects.all(), many=True)

        return Response(computermodels.data)