from assets.networkequipments.serializers import GetNetworkequipmentsSelectSerializer, GetNetworkequipmentsSerializer, GetNetworkequipmenttypesSelectSerializer, GetNetworkequipmentmodelsSelectSerializer, NetworkequipmentmodelsSerializer, NetworkequipmentsSerializer, NetworkequipmenttypesSerializer
from assets.models import Networkequipments, Networkequipmenttypes, Networkequipmentmodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetNetworkequipmentsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipments = GetNetworkequipmentsSelectSerializer(Networkequipments.objects.all(), many=True) 
        return Response(networkequipments.data)

class GetNetworkequipmenttypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmenttypes = GetNetworkequipmenttypesSelectSerializer(Networkequipmenttypes.objects.all(), many=True) 
        return Response(networkequipmenttypes.data)

class GetNetworkequipmentmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmentmodels = GetNetworkequipmentmodelsSelectSerializer(Networkequipmentmodels.objects.all(), many=True) 
        return Response(networkequipmentmodels.data)

class GetNetworkequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipments.objects.all()
    serializer_class = GetNetworkequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class NetworkequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipments.objects.all()
    serializer_class = NetworkequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networkequipments.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class NetworkequipmentmodelsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipmentmodels.objects.all()
    serializer_class = NetworkequipmentmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networkequipmentmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NetworkequipmenttypesViewSet(viewsets.ModelViewSet):
    queryset = Networkequipmenttypes.objects.all()
    serializer_class = NetworkequipmenttypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Networkequipmenttypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)