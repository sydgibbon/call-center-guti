from assets.monitors.serializers import CreateMonitorSerializer, GetMonitorsListSerializer, GetMonitortypesSelectSerializer, GetMonitormodelsSelectSerializer, GetMonitorsCountSerializer, GetMonitorsCountByManufacturersSerializer
from assets.models import Monitortypes, Monitormodels, Monitors
from rest_framework import viewsets  # import de ViewSets
from assets.monitors.serializers import GetMonitorsSerializer, GetMonitortypesSelectSerializer, GetMonitormodelsSelectSerializer, MonitormodelsSerializer, MonitorsSerializer, MonitortypesSerializer, GetMonitorsByIdSerializer
from assets.models import Monitors, Monitortypes, Monitormodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Count

class GetMonitortypesSelectViewSet(viewsets.ViewSet):
    queryset = Monitortypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        monitortypes = GetMonitortypesSelectSerializer(Monitortypes.objects.all(), many=True)

        return Response(monitortypes.data)
    
class GetMonitormodelsSelectViewSet(viewsets.ViewSet):
    queryset = Monitormodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        monitormodels = GetMonitormodelsSelectSerializer(Monitormodels.objects.all(), many=True)

        return Response(monitormodels.data)

class GetMonitorsCountViewSet(viewsets.ViewSet):
    queryset = Monitors.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        monitorsCount = GetMonitorsCountSerializer(self.queryset)

        return Response(monitorsCount.data)

class GetMonitorsCountByManufacturersViewSet(viewsets.ViewSet):
    queryset = Monitors.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Monitors.objects.values('manufacturers_id__name').annotate(count=Count('id'))
        serializer = GetMonitorsCountByManufacturersSerializer(queryset, many=True)
        return Response(serializer.data)
class GetMonitorsViewSet(viewsets.ModelViewSet):
    queryset = Monitors.objects.filter(is_deleted=0)
    serializer_class = GetMonitorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
class MonitorsViewSet(viewsets.ModelViewSet):
    queryset = Monitors.objects.all()
    serializer_class = MonitorsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Monitors.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MonitormodelsViewSet(viewsets.ModelViewSet):
    queryset = Monitormodels.objects.all()
    serializer_class = MonitormodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Monitormodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MonitortypesViewSet(viewsets.ModelViewSet):
    queryset = Monitortypes.objects.all()
    serializer_class = MonitortypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Monitortypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetMonitorsListViewSet(viewsets.ViewSet):
    queryset = Monitors.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        monitors = GetMonitorsListSerializer(Monitors.objects.all(), many=True)

        return Response(monitors.data)
    
class CreateMonitorViewSet(viewsets.GenericViewSet):
    queryset=Monitors.objects.all()
    serializer_class = CreateMonitorSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetMonitorsByIdViewSet(viewsets.ViewSet):
    queryset = Monitors.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            monitor = Monitors.objects.get(id=pk)
        except Monitors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetMonitorsByIdSerializer(monitor)
        return Response(serializer.data)