from assets.consumables.serializers import ConsumableitemsSerializer, ConsumableitemtypesSerializer, ConsumablesSerializer, GetConsumableitemsSerializer, GetConsumableitemtypesSelectSerializer, GetConsumableitemsListSerializer, GetConsumableitemsByIdSerializer, CreateConsumableItemsSerializer
from assets.models import Consumableitems, Consumableitemtypes, Consumables
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from assets.generics.serializers import DeleteMultipleSerializer
from rest_framework.decorators import action

class GetConsumableitemtypesSelectViewSet(viewsets.ViewSet):
    queryset = Consumableitemtypes.objects.all()
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
    queryset = Consumableitems.objects.filter(is_deleted=0)
    serializer_class = GetConsumableitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class GetConsumableitemsListViewSet(viewsets.ViewSet):
    queryset = Consumableitems.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        consumableitems = GetConsumableitemsListSerializer(Consumableitems.objects.all(), many=True)

        return Response(consumableitems.data)

class GetConsumableitemsByIdViewSet(viewsets.ViewSet):
    queryset = Consumableitems.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            consumableitem = Consumableitems.objects.get(id=pk)
        except Consumableitems.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetConsumableitemsByIdSerializer(consumableitem)
        return Response(serializer.data)
    
class UpdateConsumableByIdViewSet(viewsets.ModelViewSet):
    queryset = Consumables.objects.all()
    serializer_class = CreateConsumableItemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)
class CreateConsumableItemsViewSet(viewsets.GenericViewSet):
    queryset=Consumableitems.objects.all()
    serializer_class = CreateConsumableItemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class DeleteConsumableitemByIdViewSet(viewsets.ModelViewSet):
    queryset = Consumableitems.objects.all()
    serializer_class = ConsumableitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']
    @action(detail=False, methods=['delete'], serializer_class=DeleteMultipleSerializer)
    def delete_multiple(self, request):
        object_ids = request.data.get('object_ids', [])
        serializer = DeleteMultipleSerializer(data=request.data)
        if serializer.is_valid():

            deleted_objects = []  # To store the deleted objects

            for object_id in object_ids:
                try:
                    obj = Consumableitems.objects.get(pk=object_id)
                    obj.delete()
                    deleted_objects.append(object_id)
                except Consumableitems.DoesNotExist:
                    pass  # Handle the case when the object does not exist

            return Response({'message': f'{len(deleted_objects)} objects deleted successfully'})
        else:
            return Response(serializer.errors, status=400)