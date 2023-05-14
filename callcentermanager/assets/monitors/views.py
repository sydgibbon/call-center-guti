from assets.monitors.serializers import GetMonitortypesSelectSerializer, GetMonitormodelsSelectSerializer, GetMonitorsCountSerializer, MonitorsByManufacturersSerializer
from assets.models import Monitortypes, Monitormodels, Monitors
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Count

class GetMonitortypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        monitortypes = GetMonitortypesSelectSerializer(Monitortypes.objects.all(), many=True)

        return Response(monitortypes.data)
    
class GetMonitormodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        monitormodels = GetMonitormodelsSelectSerializer(Monitormodels.objects.all(), many=True)

        return Response(monitormodels.data)

class GetMonitorsCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        monitorsCount = GetMonitorsCountSerializer(Monitors.objects.count())

        return Response(monitorsCount.data)

class MonitorsByManufacturersViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Monitors.objects.values('manufacturers_id__name').annotate(count=Count('id'))
        serializer = MonitorsByManufacturersSerializer(queryset, many=True)
        return Response(serializer.data)