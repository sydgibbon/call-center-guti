from assets.networkequipments.serializers import CreateNetworkequipmentSerializer, GetNetworkequipmentsListSerializer, GetNetworkequipmentsSelectSerializer, GetNetworkequipmentsSerializer, GetNetworkequipmenttypesSelectSerializer, GetNetworkequipmentmodelsSelectSerializer, NetworkequipmentmodelsSerializer, NetworkequipmentsSerializer, NetworkequipmenttypesSerializer, GetNetworkequipmentsByIdSerializer
from assets.models import Networkequipments, Networkequipmenttypes, Networkequipmentmodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetNetworkequipmentsSelectViewSet(viewsets.ViewSet):
    queryset = Networkequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipments = GetNetworkequipmentsSelectSerializer(Networkequipments.objects.all(), many=True) 
        return Response(networkequipments.data)

class GetNetworkequipmenttypesSelectViewSet(viewsets.ViewSet):
    queryset = Networkequipmenttypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmenttypes = GetNetworkequipmenttypesSelectSerializer(Networkequipmenttypes.objects.all(), many=True) 
        return Response(networkequipmenttypes.data)

class GetNetworkequipmentmodelsSelectViewSet(viewsets.ViewSet):
    queryset = Networkequipmentmodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipmentmodels = GetNetworkequipmentmodelsSelectSerializer(Networkequipmentmodels.objects.all(), many=True) 
        return Response(networkequipmentmodels.data)

class GetNetworkequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Networkequipments.objects.filter(is_deleted=0)
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

    
class GetNetworkequipmentsListViewSet(viewsets.ViewSet):
    queryset = Networkequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        networkequipments = GetNetworkequipmentsListSerializer(Networkequipments.objects.all(), many=True)

        return Response(networkequipments.data)

class CreateNetworkequipmentViewSet(viewsets.GenericViewSet):
    queryset=Networkequipments.objects.all()
    serializer_class = CreateNetworkequipmentSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class GetNetworkequipmentsByIdViewSet(viewsets.ViewSet):
    queryset = Networkequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            networkequipment = Networkequipments.objects.get(id=pk)
        except Networkequipments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetNetworkequipmentsByIdSerializer(networkequipment)
        return Response(serializer.data)
    
class UpdateNetworkequipmentByIdViewSet(viewsets.ModelViewSet):
    queryset = Networkequipments.objects.all()
    serializer_class = CreateNetworkequipmentSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class DeleteNetworkequipmentByIdViewSet(viewsets.ModelViewSet):
    queryset = Networkequipments.objects.all()
    serializer_class = NetworkequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        networkequipment = Networkequipments.objects.get(id=pk)
        networkequipment.is_deleted = 1
        networkequipment.save()
        return Response(status=status.HTTP_200_OK)