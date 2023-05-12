from assets.computers.serializers import GetComputersSelectSerializer, GetComputertypesSelectSerializer, GetComputermodelsSelectSerializer, GetComputersCountSerializer, CountByStatusSerializer
from assets.models import Computers, Computertypes, Computermodels
from rest_framework import viewsets  # import de ViewSets
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

class CountByStatusViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']


    def list(self, request):
        queryset = Computers.objects.values('manufacturers_id').annotate(count=Count('id'))
        serializer = CountByStatusSerializer(queryset, many=True)
        return Response(serializer.data)