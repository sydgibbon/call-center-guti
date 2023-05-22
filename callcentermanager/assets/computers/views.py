from assets.computers.serializers import GetComputersSelectSerializer, GetComputertypesSelectSerializer, GetComputermodelsSelectSerializer, GetComputersCountSerializer, GetComputersCountByStatesSerializer, GetComputersCountByManufacturersSerializer, GetComputersCountByComputertypesSerializer
from assets.models import Computers, Computertypes, Computermodels
from rest_framework import viewsets  # import de ViewSets
from assets.computers.serializers import ComputermodelsSerializer, ComputersItemsSerializer, ComputersSerializer, ComputertypesSerializer, GetComputersSelectSerializer, GetComputertypesSelectSerializer, GetComputermodelsSelectSerializer, GetComputersSerializer, OperatingsystemsSerializer
from assets.models import Computers, ComputersItems, Computertypes, Computermodels, Operatingsystems, States
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Count

class GetComputersSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computers = GetComputersSelectSerializer(Computers.objects.all(), many=True)

        return Response(computers.data)
    
class GetComputertypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computertypes = GetComputertypesSelectSerializer(Computertypes.objects.all(), many=True)

        return Response(computertypes.data)
    
class GetComputermodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computermodels = GetComputermodelsSelectSerializer(Computermodels.objects.all(), many=True)

        return Response(computermodels.data)
    
class GetComputersCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        computersCount = GetComputersCountSerializer(Computers.objects.count())

        return Response(computersCount.data)

class GetComputersCountByManufacturersViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Computers.objects.values('manufacturers_id__name').annotate(count=Count('id'))
        serializer = GetComputersCountByManufacturersSerializer(queryset, many=True)
        return Response(serializer.data)
    
class GetComputersCountByStatesViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Computers.objects.values('states_id__name').annotate(count=Count('id'))
        serializer = GetComputersCountByStatesSerializer(queryset, many=True)
        return Response(serializer.data)


class GetComputersCountByComputertypesViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        queryset = Computers.objects.values('computertypes_id__name').annotate(count=Count('id'))
        serializer = GetComputersCountByComputertypesSerializer(queryset, many=True)
        return Response(serializer.data)
class GetComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = GetComputersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
class ComputersViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Computers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
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
