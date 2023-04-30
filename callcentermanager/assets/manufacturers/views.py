from assets.manufacturers.serializers import GetManufacturersSelectSerializer
from assets.models import Manufacturers
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetManufacturersSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        manufacturers = GetManufacturersSelectSerializer(Manufacturers.objects.all(), many=True) 
        return Response(manufacturers.data)