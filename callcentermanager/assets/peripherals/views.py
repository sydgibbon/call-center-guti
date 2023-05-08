from assets.peripherals.serializers import GetPeripheralsSelectSerializer, GetPeripheraltypesSelectSerializer, GetPeripheralmodelsSelectSerializer, PeripheralmodelsSerializer, PeripheralsSerializer, GetPeripheralsSerializer, PeripheraltypesSerializer
from assets.models import Peripherals, Peripheraltypes, Peripheralmodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPeripheralsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        peripherals = GetPeripheralsSelectSerializer(Peripherals.objects.all(), many=True)

        return Response(peripherals.data)

class GetPeripheraltypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        peripheraltypes = GetPeripheraltypesSelectSerializer(Peripheraltypes.objects.all(), many=True)

        return Response(peripheraltypes.data)
    
class GetPeripheralmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        peripheralmodels = GetPeripheralmodelsSelectSerializer(Peripheralmodels.objects.all(), many=True)

        return Response(peripheralmodels.data)
    
class GetPeripheralsViewSet(viewsets.ModelViewSet):
    queryset = Peripherals.objects.all()
    serializer_class = GetPeripheralsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
class PeripheralsViewSet(viewsets.ModelViewSet):
    queryset = Peripherals.objects.all()
    serializer_class = PeripheralsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Peripherals.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeripheralmodelsViewSet(viewsets.ModelViewSet):
    queryset = Peripheralmodels.objects.all()
    serializer_class = PeripheralmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Peripheralmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeripheraltypesViewSet(viewsets.ModelViewSet):
    queryset = Peripheraltypes.objects.all()
    serializer_class = PeripheraltypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Peripheraltypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)