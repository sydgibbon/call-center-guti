from assets.networks.serializers import GetNetworksSelectSerializer, GetNetworkequipmentsCountSerializer,GetNetworkequipmentsCountByManufacturersSerializer
from assets.models import Networks, Networkequipments
from rest_framework import viewsets  # import de ViewSets
from assets.networks.serializers import GetNetworksSelectSerializer, NetworksSerializer
from assets.models import Networks
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Count


class GetNetworksSelectViewSet(viewsets.ViewSet):
    queryset = Networks.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networks = GetNetworksSelectSerializer(Networks.objects.all(), many=True) 
        return Response(networks.data)
    
class GetNetworkequipmentsCountViewSet(viewsets.ViewSet):
    queryset = Networkequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmentsCount = GetNetworkequipmentsCountSerializer(self.queryset)

        return Response(networkequipmentsCount.data)

class GetNetworkequipmentsCountByManufacturersViewSet(viewsets.ViewSet):
    queryset = Networkequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Networkequipments.objects.values('manufacturers_id__name').annotate(count=Count('id'))
        serializer = GetNetworkequipmentsCountByManufacturersSerializer(queryset, many=True)
        return Response(serializer.data)

class NetworksViewSet(viewsets.ModelViewSet):
    queryset = Networks.objects.all()
    serializer_class = NetworksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
