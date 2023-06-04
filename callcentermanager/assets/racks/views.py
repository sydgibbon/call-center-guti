from assets.racks.serializers import GetRacksListSerializer, GetRacktypesSelectSerializer, GetRackmodelsSelectSerializer, GetDcroomsSelectSerializer, GetRacksCountSerializer
from assets.models import Racktypes, Rackmodels, Dcrooms, Racks
from rest_framework import viewsets  # import de ViewSets
from assets.racks.serializers import DcroomsSerializer, GetRacksSerializer, GetRacktypesSelectSerializer, GetRackmodelsSelectSerializer, GetDcroomsSelectSerializer, ItemsRacksSerializer, RackmodelsSerializer, RacksSerializer, RacktypesSerializer
from assets.models import ItemsRacks, Racks, Racktypes, Rackmodels, Dcrooms
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetRacktypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        racktypes = GetRacktypesSelectSerializer(Racktypes.objects.all(), many=True) 
        return Response(racktypes.data)
    
class GetRackmodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        rackmodels = GetRackmodelsSelectSerializer(Rackmodels.objects.all(), many=True) 
        return Response(rackmodels.data)
    
class GetDcroomsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        dcrooms = GetDcroomsSelectSerializer(Dcrooms.objects.all(), many=True) 
        return Response(dcrooms.data)
    
class GetRacksCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        racksCount = GetRacksCountSerializer(Racks.objects.count())

        return Response(racksCount.data)
class RacksViewSet(viewsets.ModelViewSet):
    queryset = Racks.objects.all()
    serializer_class = RacksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Racks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemsRacksViewSet(viewsets.ModelViewSet):
    queryset = ItemsRacks.objects.all()
    serializer_class = ItemsRacksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsRacks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RackmodelsViewSet(viewsets.ModelViewSet):
    queryset = Rackmodels.objects.all()
    serializer_class = RackmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Rackmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RacktypesViewSet(viewsets.ModelViewSet):
    queryset = Racktypes.objects.all()
    serializer_class = RacktypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Racktypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DcroomsViewSet(viewsets.ModelViewSet):
    queryset = Dcrooms.objects.all()
    serializer_class = DcroomsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Dcrooms.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetRacksViewSet(viewsets.ModelViewSet):
    queryset = Racks.objects.all()
    serializer_class = GetRacksSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class GetRacksListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        racks = GetRacksListSerializer(Racks.objects.all(), many=True)

        return Response(racks.data)