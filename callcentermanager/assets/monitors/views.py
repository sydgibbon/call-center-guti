from assets.monitors.serializers import GetMonitorsSerializer, GetMonitortypesSelectSerializer, GetMonitormodelsSelectSerializer, MonitormodelsSerializer, MonitorsSerializer, MonitortypesSerializer
from assets.models import Monitors, Monitortypes, Monitormodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

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

class GetMonitorsViewSet(viewsets.ModelViewSet):
    queryset = Monitors.objects.all()
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
    