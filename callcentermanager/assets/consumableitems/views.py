from assets.consumableitems.serializers import GetConsumableitemtypesSelectSerializer
from assets.models import Consumableitemtypes
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetConsumableitemtypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        consumableitemtypes = GetConsumableitemtypesSelectSerializer(Consumableitemtypes.objects.all(), many=True) 
        return Response(consumableitemtypes.data)