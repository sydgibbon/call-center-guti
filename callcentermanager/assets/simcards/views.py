from assets.simcards.serializers import CreateDevicesimcardSerializer, DevicesimcardsSerializer, DevicesimcardtypesSerializer, GetDevicesimcardsListSerializer, GetDevicesimcardsSelectSerializer, GetDevicesimcardsSerializer, GetLinesSelectSerializer, ItemsDevicesimcardsSerializer
from assets.models import Devicesimcards, Devicesimcardtypes, ItemsDevicesimcards, Lines
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetDevicesimcardsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        devicesimcards = GetDevicesimcardsSelectSerializer(Devicesimcards.objects.all(), many=True) 
        return Response(devicesimcards.data)
      
class GetLinesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        lines = GetLinesSelectSerializer(Lines.objects.all(), many=True) 
        return Response(lines.data)

class DevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcards.objects.all()
    serializer_class = DevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesimcards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DevicesimcardtypesViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcardtypes.objects.all()
    serializer_class = DevicesimcardtypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Devicesimcardtypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ItemsDevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = ItemsDevicesimcards.objects.all()
    serializer_class = ItemsDevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsDevicesimcards.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetDevicesimcardsViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcards.objects.all()
    serializer_class = GetDevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class GetDevicesimcardsListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        devicesimcards = GetDevicesimcardsListSerializer(Devicesimcards.objects.all(), many=True)

        return Response(devicesimcards.data)
    
class CreateDevicesimcardViewSet(viewsets.GenericViewSet):
    queryset=Devicesimcards.objects.all()
    serializer_class = CreateDevicesimcardSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)