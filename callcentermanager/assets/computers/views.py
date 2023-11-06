from assets.computers.serializers import CreateComputerSerializer, GetComputersByIdSerializer, GetComputersSelectSerializer, GetComputertypesSelectSerializer, GetComputermodelsSelectSerializer, GetComputersCountSerializer, GetComputersCountByStatesSerializer, GetComputersCountByManufacturersSerializer, GetComputersCountByComputertypesSerializer, GetComputersListSerializer
from assets.models import Computers, Computertypes, Computermodels
from assets.computers.serializers import ComputermodelsSerializer, ComputersItemsSerializer, ComputersSerializer, ComputertypesSerializer, GetComputersSelectSerializer, GetComputertypesSelectSerializer, GetComputermodelsSelectSerializer, GetComputersSerializer, OperatingsystemsSerializer
from assets.models import Computers, ComputersItems, Computertypes, Computermodels, Operatingsystems, States
from rest_framework import viewsets, status, generics  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.decorators import action
from assets.generics.serializers import DeleteMultipleSerializer

class GetComputersSelectViewSet(viewsets.ViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computers = GetComputersSelectSerializer(Computers.objects.all(), many=True)

        return Response(computers.data)
    
class GetComputertypesSelectViewSet(viewsets.ViewSet):
    queryset = Computertypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computertypes = GetComputertypesSelectSerializer(Computertypes.objects.all(), many=True)

        return Response(computertypes.data)
    
class GetComputermodelsSelectViewSet(viewsets.ViewSet):
    queryset = Computermodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computermodels = GetComputermodelsSelectSerializer(Computermodels.objects.all(), many=True)

        return Response(computermodels.data)
    
class GetComputersCountViewSet(viewsets.ViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computersCount = GetComputersCountSerializer(self.queryset)

        return Response(computersCount.data)

class GetComputersCountByManufacturersViewSet(viewsets.ViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Computers.objects.values('manufacturers_id__name').annotate(count=Count('id'))
        serializer = GetComputersCountByManufacturersSerializer(queryset, many=True)
        return Response(serializer.data)
    
class GetComputersCountByStatesViewSet(viewsets.ViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Computers.objects.values('states_id__name').annotate(count=Count('id'))
        serializer = GetComputersCountByStatesSerializer(queryset, many=True)
        return Response(serializer.data)


class GetComputersCountByComputertypesViewSet(viewsets.ViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Computers.objects.values('computertypes_id__name').annotate(count=Count('id'))
        serializer = GetComputersCountByComputertypesSerializer(queryset, many=True)
        return Response(serializer.data)
class GetComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    serializer_class = GetComputersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
    # def get_queryset(self):

    #     queryset = Computers.objects.filter(is_deleted=0)
    #     return queryset
    
class ComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get','delete']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Computers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CreateComputerViewSet(viewsets.GenericViewSet):
    queryset=Computers.objects.all()
    serializer_class = CreateComputerSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ComputermodelsViewSet(viewsets.ModelViewSet):
    queryset = Computermodels.objects.all()
    serializer_class = ComputermodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Computermodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ComputersItemsViewSet(viewsets.ModelViewSet):
    queryset = ComputersItems.objects.all()
    serializer_class = ComputersItemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ComputersItems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComputertypesViewSet(viewsets.ModelViewSet):
    queryset = Computertypes.objects.all()
    serializer_class = ComputertypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Computertypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OperatingsystemsViewSet(viewsets.ModelViewSet):
    queryset = Operatingsystems.objects.all()
    serializer_class = OperatingsystemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = States.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetComputersListViewSet(viewsets.ViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computers = GetComputersListSerializer(Computers.objects.all(), many=True)

        return Response(computers.data)

class GetComputersByIdViewSet(viewsets.ViewSet):
    queryset = Computers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            computer = Computers.objects.get(id=pk)
        except Computers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetComputersByIdSerializer(computer)
        return Response(serializer.data)

    
class UpdateComputerByIdViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = CreateComputerSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
class DeleteComputerByIdViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        computer = Computers.objects.get(id=pk)
        computer.is_deleted = 1
        computer.save()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'], serializer_class=DeleteMultipleSerializer)
    def delete_multiple(self, request):
        object_ids = request.data.get('object_ids', [])
        serializer = DeleteMultipleSerializer(data=request.data)
        if serializer.is_valid():

            deleted_objects = []  # To store the deleted objects

            for object_id in object_ids:
                try:
                    obj = Computers.objects.get(pk=object_id)
                    obj.is_deleted = 1
                    obj.save()
                    deleted_objects.append(object_id)
                except Computers.DoesNotExist:
                    pass  # Handle the case when the object does not exist

            return Response({'message': f'{len(deleted_objects)} objects deleted successfully'})
        else:
            return Response(serializer.errors, status=400)