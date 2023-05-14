from assets.consumables.serializers import ConsumableitemsSerializer, ConsumableitemtypesSerializer, ConsumablesSerializer, GetConsumableitemsSerializer, GetConsumableitemtypesSelectSerializer
from assets.models import Consumableitems, Consumableitemtypes, Consumables
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetConsumableitemtypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        consumableitemtypes = GetConsumableitemtypesSelectSerializer(Consumableitemtypes.objects.all(), many=True) 
        return Response(consumableitemtypes.data)
    
class ConsumableitemsViewSet(viewsets.ModelViewSet):
    queryset = Consumableitems.objects.all()
    serializer_class = ConsumableitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Consumableitems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConsumableitemtypesViewSet(viewsets.ModelViewSet):
    queryset = Consumableitemtypes.objects.all()
    serializer_class = ConsumableitemtypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Consumableitemtypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConsumablesViewSet(viewsets.ModelViewSet):
    queryset = Consumables.objects.all()
    serializer_class = ConsumablesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Consumables.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetConsumableitemsViewSet(viewsets.ModelViewSet):
    queryset = Consumableitems.objects.all()
    serializer_class = GetConsumableitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']