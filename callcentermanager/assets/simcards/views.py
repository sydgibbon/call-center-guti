from assets.simcards.serializers import CreateDevicesimcardSerializer, DevicesimcardsSerializer, DevicesimcardtypesSerializer, GetDevicesimcardsListSerializer, GetDevicesimcardsSelectSerializer, GetDevicesimcardsSerializer, GetLinesSelectSerializer, ItemsDevicesimcardsSerializer, GetItemsDevicesimcardsByIdSerializer
from assets.models import Devicesimcards, Devicesimcardtypes, ItemsDevicesimcards, Lines
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from assets.generics.serializers import DeleteMultipleSerializer

class GetDevicesimcardsSelectViewSet(viewsets.ViewSet):
    queryset = Devicesimcards.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        devicesimcards = GetDevicesimcardsSelectSerializer(Devicesimcards.objects.all(), many=True) 
        return Response(devicesimcards.data)
      
class GetLinesSelectViewSet(viewsets.ViewSet):
    queryset = Lines.objects.filter(is_deleted=0)
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
    queryset = Devicesimcards.objects.filter(is_deleted=0)
    serializer_class = GetDevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class GetDevicesimcardsListViewSet(viewsets.ViewSet):
    queryset = Devicesimcards.objects.filter(is_deleted=0)
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

class GetItemsDevicesimcardsByIdViewSet(viewsets.ViewSet):
    queryset = Devicesimcards.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            itemsDevicesimcard = ItemsDevicesimcards.objects.get(id=pk)
        except ItemsDevicesimcards.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetItemsDevicesimcardsByIdSerializer(itemsDevicesimcard)
        return Response(serializer.data)
    
class UpdateDevicesimcardByIdViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcards.objects.all()
    serializer_class = CreateDevicesimcardSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteDevicesimcardByIdViewSet(viewsets.ModelViewSet):
    queryset = Devicesimcards.objects.all()
    serializer_class = DevicesimcardsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        devicesimcard = Devicesimcards.objects.get(id=pk)
        devicesimcard.is_deleted = 1
        devicesimcard.save()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['delete'], serializer_class=DeleteMultipleSerializer)
    def delete_multiple(self, request):
        object_ids = request.data.get('object_ids', [])
        serializer = DeleteMultipleSerializer(data=request.data)
        if serializer.is_valid():

            deleted_objects = []  # To store the deleted objects

            for object_id in object_ids:
                try:
                    obj = Devicesimcards.objects.get(pk=object_id)
                    obj.is_deleted = 1
                    obj.save()
                    deleted_objects.append(object_id)
                except Devicesimcards.DoesNotExist:
                    pass  # Handle the case when the object does not exist

            return Response({'message': f'{len(deleted_objects)} objects deleted successfully'})
        else:
            return Response(serializer.errors, status=400)