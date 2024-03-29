from assets.passivedcequipments.serializers import CreatePassivedcequipmentSerializer, GetPassivedcequipmentsListSerializer, GetPassivedcequipmentsSelectSerializer, GetPassivedcequipmentsSerializer, GetPassivedcequipmenttypesSelectSerializer, GetPassivedcequipmentmodelsSelectSerializer, PassivedcequipmentmodelsSerializer, PassivedcequipmentsSerializer, PassivedcequipmenttypesSerializer, GetPassivedcequipmentsByIdSerializer
from assets.models import Passivedcequipments, Passivedcequipmenttypes, Passivedcequipmentmodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from assets.generics.serializers import DeleteMultipleSerializer
from rest_framework.decorators import action

class GetPassivedcequipmentsSelectViewSet(viewsets.ViewSet):
    queryset = Passivedcequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipments = GetPassivedcequipmentsSelectSerializer(Passivedcequipments.objects.all(), many=True) 
        return Response(passivedcequipments.data)

class GetPassivedcequipmenttypesSelectViewSet(viewsets.ViewSet):
    queryset = Passivedcequipmenttypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipmenttypes = GetPassivedcequipmenttypesSelectSerializer(Passivedcequipmenttypes.objects.all(), many=True) 
        return Response(passivedcequipmenttypes.data)
    
class GetPassivedcequipmentmodelsSelectViewSet(viewsets.ViewSet):
    queryset = Passivedcequipmentmodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipmentmodels = GetPassivedcequipmentmodelsSelectSerializer(Passivedcequipmentmodels.objects.all(), many=True) 
        return Response(passivedcequipmentmodels.data)
    
class GetPassivedcequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipments.objects.all()
    serializer_class = GetPassivedcequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
class PassivedcequipmentsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipments.objects.all()
    serializer_class = PassivedcequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipments.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PassivedcequipmenttypesViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipmenttypes.objects.all()
    serializer_class = PassivedcequipmenttypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipmenttypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PassivedcequipmentmodelsViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipmentmodels.objects.all()
    serializer_class = PassivedcequipmentmodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Passivedcequipmentmodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetPassivedcequipmentsListViewSet(viewsets.ViewSet):
    queryset = Passivedcequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        passivedcequipments = GetPassivedcequipmentsListSerializer(Passivedcequipments.objects.all(), many=True)

        return Response(passivedcequipments.data)
    
class CreatePassivedcequipmentViewSet(viewsets.GenericViewSet):
    queryset=Passivedcequipments.objects.all()
    serializer_class = CreatePassivedcequipmentSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetPassivedcequipmentsByIdViewSet(viewsets.ViewSet):
    queryset = Passivedcequipments.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            passivedcequipment = Passivedcequipments.objects.get(id=pk)
        except Passivedcequipments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetPassivedcequipmentsByIdSerializer(passivedcequipment)
        return Response(serializer.data)

class UpdatePassivedcequipmentByIdViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipments.objects.all()
    serializer_class = CreatePassivedcequipmentSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class DeletePassivedcequipmentByIdViewSet(viewsets.ModelViewSet):
    queryset = Passivedcequipments.objects.all()
    serializer_class = PassivedcequipmentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        passivedcequipment = Passivedcequipments.objects.get(id=pk)
        passivedcequipment.is_deleted = 1
        passivedcequipment.save()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['delete'], serializer_class=DeleteMultipleSerializer)
    def delete_multiple(self, request):
        object_ids = request.data.get('object_ids', [])
        serializer = DeleteMultipleSerializer(data=request.data)
        if serializer.is_valid():

            deleted_objects = []  # To store the deleted objects

            for object_id in object_ids:
                try:
                    obj = Passivedcequipments.objects.get(pk=object_id)
                    obj.is_deleted = 1
                    obj.save()
                    deleted_objects.append(object_id)
                except Passivedcequipments.DoesNotExist:
                    pass  # Handle the case when the object does not exist

            return Response({'message': f'{len(deleted_objects)} objects deleted successfully'})
        else:
            return Response(serializer.errors, status=400)
