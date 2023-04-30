from assets.locations.serializers import GetLocationsSelectSerializer
from assets.models import Locations
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetLocationsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        locations = GetLocationsSelectSerializer(Locations.objects.all(), many=True)

        return Response(locations.data)