from assets.enclosures.serializers import GetEnclosuremodelsSelectSerializer, GetEnclosuresCountSerializer
from assets.models import Enclosuremodels, Enclosures
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetEnclosuremodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        enclosuremodels = GetEnclosuremodelsSelectSerializer(Enclosuremodels.objects.all(), many=True) 
        return Response(enclosuremodels.data)

class GetEnclosuresCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        enclosuresCount = GetEnclosuresCountSerializer(Enclosures.objects.count())

        return Response(enclosuresCount.data)