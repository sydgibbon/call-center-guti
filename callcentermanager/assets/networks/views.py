from assets.networks.serializers import GetNetworksSelectSerializer, GetNetworkequipmentsCountSerializer, NetworkequipmentsByManufacturersSerializer
from assets.models import Networks, Networkequipments
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Count


class GetNetworksSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networks = GetNetworksSelectSerializer(Networks.objects.all(), many=True) 
        return Response(networks.data)
    
class GetNetworkequipmentsCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmentsCount = GetNetworkequipmentsCountSerializer(Networkequipments.objects.count())

        return Response(networkequipmentsCount.data)

class NetworkequipmentsByManufacturersViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Networkequipments.objects.values('manufacturers_id__name').annotate(count=Count('id'))
        serializer = NetworkequipmentsByManufacturersSerializer(queryset, many=True)
        return Response(serializer.data)