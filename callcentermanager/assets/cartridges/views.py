from assets.cartridges.serializers import GetCartridgeitemtypesSelectSerializer
from assets.models import Cartridgeitemtypes
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetCartridgeitemtypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cartridgeitemtypes = GetCartridgeitemtypesSelectSerializer(Cartridgeitemtypes.objects.all(), many=True) 
        return Response(cartridgeitemtypes.data)