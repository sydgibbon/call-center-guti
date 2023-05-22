from assistance.models import Crontasklogs, Crontasks, ProjecttasksTickets, Tickettasks
from assistance.tasks.serializers import CrontasklogsSerializer, CrontasksSerializer, ProjecttasksTicketsSerializer, TickettasksSerializer
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class ProjecttasksTicketsViewSet(viewsets.ModelViewSet):
    queryset = ProjecttasksTickets.objects.all()
    serializer_class = ProjecttasksTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ProjecttasksTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TickettasksViewSet(viewsets.ModelViewSet):
    queryset = Tickettasks.objects.all()
    serializer_class = TickettasksSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Tickettasks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CrontasklogsViewSet(viewsets.ModelViewSet):
    queryset = Crontasklogs.objects.all()
    serializer_class = CrontasklogsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Crontasklogs.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CrontasksViewSet(viewsets.ModelViewSet):
    queryset = Crontasks.objects.all()
    serializer_class = CrontasksSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Crontasks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)