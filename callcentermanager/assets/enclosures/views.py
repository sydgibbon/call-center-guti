from assets.enclosures.serializers import GetEnclosuremodelsSelectSerializer
from assets.models import Enclosuremodels
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetEnclosuremodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetEnclosuremodelsSelectSerializer(Enclosuremodels.objects.all(), many=True) 
        return Response(states.data)