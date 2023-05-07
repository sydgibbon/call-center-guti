from assets.networks.serializers import GetNetworksSelectSerializer, NetworksSerializer
from assets.models import Networks
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetNetworksSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networks = GetNetworksSelectSerializer(Networks.objects.all(), many=True) 
        return Response(networks.data)

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