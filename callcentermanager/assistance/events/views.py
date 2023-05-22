from rest_framework import viewsets, status
from assistance.events.serializers import EventsSerializer, PlanningeventcategoriesSerializer, PlanningexternaleventsSerializer, PlanningexternaleventtemplatesSerializer  # import de ViewSets
from assistance.serializers import *  # import de todos los serializers,
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Events.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlanningexternaleventsViewSet(viewsets.ModelViewSet):
    queryset = Planningexternalevents.objects.all()
    serializer_class = PlanningexternaleventsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Planningexternalevents.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlanningexternaleventtemplatesViewSet(viewsets.ModelViewSet):
    queryset = Planningexternaleventtemplates.objects.all()
    serializer_class = PlanningexternaleventtemplatesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Planningexternaleventtemplates.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlanningeventcategoriesViewSet(viewsets.ModelViewSet):
    queryset = Planningeventcategories.objects.all()
    serializer_class = PlanningeventcategoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Planningeventcategories.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)