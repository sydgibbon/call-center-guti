from assets.simcards.serializers import GetDevicesimcardsSelectSerializer, GetLinesSelectSerializer
from assets.models import Devicesimcards, Lines
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetDevicesimcardsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        devicesimcards = GetDevicesimcardsSelectSerializer(Devicesimcards.objects.all(), many=True) 
        return Response(devicesimcards.data)
      
class GetLinesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        lines = GetLinesSelectSerializer(Lines.objects.all(), many=True) 
        return Response(lines.data)