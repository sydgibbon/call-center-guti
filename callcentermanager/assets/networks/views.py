from assets.networks.serializers import GetNetworksSelectSerializer
from assets.models import Networks
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetNetworksSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networks = GetNetworksSelectSerializer(Networks.objects.all(), many=True) 
        return Response(networks.data)