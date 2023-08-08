from assets.passivedcequipments.serializers import CreatePassivedcequipmentSerializer, GetPassivedcequipmentsListSerializer, GetPassivedcequipmentsSelectSerializer, GetPassivedcequipmentsSerializer, GetPassivedcequipmenttypesSelectSerializer, GetPassivedcequipmentmodelsSelectSerializer, PassivedcequipmentmodelsSerializer, PassivedcequipmentsSerializer, PassivedcequipmenttypesSerializer, GetPassivedcequipmentsByIdSerializer
from assets.models import Passivedcequipments, Passivedcequipmenttypes, Passivedcequipmentmodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPassivedcequipmentsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipments = GetPassivedcequipmentsSelectSerializer(Passivedcequipments.objects.all(), many=True) 
        return Response(passivedcequipments.data)

class GetPassivedcequipmenttypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipmenttypes = GetPassivedcequipmenttypesSelectSerializer(Passivedcequipmenttypes.objects.all(), many=True) 
        return Response(passivedcequipmenttypes.data)
    
class GetPassivedcequipmentmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipmentmodels = GetPassivedcequipmentmodelsSelectSerializer(Passivedcequipmentmodels.objects.all(), many=True) 
        return Response(passivedcequipmentmodels.data)
    
class GetPassivedcequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipments.objects.all()
    serializer_class = GetPassivedcequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
class PassivedcequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipments.objects.all()
    serializer_class = PassivedcequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipments.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PassivedcequipmenttypesViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipmenttypes.objects.all()
    serializer_class = PassivedcequipmenttypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipmenttypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PassivedcequipmentmodelsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipmentmodels.objects.all()
    serializer_class = PassivedcequipmentmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipmentmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetPassivedcequipmentsListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipments = GetPassivedcequipmentsListSerializer(Passivedcequipments.objects.all(), many=True)

        return Response(passivedcequipments.data)
    
class CreatePassivedcequipmentViewSet(viewsets.GenericViewSet):
    queryset=Passivedcequipments.objects.all()
    serializer_class = CreatePassivedcequipmentSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetPassivedcequipmentsByIdViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            passivedcequipment = Passivedcequipments.objects.get(id=pk)
        except Passivedcequipments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetPassivedcequipmentsByIdSerializer(passivedcequipment)
        return Response(serializer.data)