from assets.peripherals.serializers import CreatePeripheralSerializer, GetPeripheralsListSerializer, GetPeripheralsSelectSerializer, GetPeripheraltypesSelectSerializer, GetPeripheralmodelsSelectSerializer, PeripheralmodelsSerializer, PeripheralsSerializer, GetPeripheralsSerializer, PeripheraltypesSerializer, GetPeripheralsByIdSerializer
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

class GetPeripheralsListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        peripherals = GetPeripheralsListSerializer(Peripherals.objects.all(), many=True)

        return Response(peripherals.data)
    
class CreatePeripheralViewSet(viewsets.GenericViewSet):
    queryset=Peripherals.objects.all()
    serializer_class = CreatePeripheralSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class GetPeripheralsByIdViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            peripheral = Peripherals.objects.get(id=pk)
        except Peripherals.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetPeripheralsByIdSerializer(peripheral)
        return Response(serializer.data)
    
class UpdatePeripheralByIdViewSet(viewsets.ModelViewSet):
    queryset = Peripherals.objects.all()
    serializer_class = CreatePeripheralSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class DeletePeripheralByIdViewSet(viewsets.ModelViewSet):
    queryset = Peripherals.objects.all()
    serializer_class = PeripheralsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        peripheral = Peripherals.objects.get(id=pk)
        peripheral.is_deleted = 1
        peripheral.save()
        return Response(status=status.HTTP_200_OK)