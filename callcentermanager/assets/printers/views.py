from assets.printers.serializers import GetPrintersSelectSerializer, GetPrintermodelsSelectSerializer, GetPrintertypesSelectSerializer, GetPrintersCountSerializer
from assets.models import Printers, Printermodels, Printertypes
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPrintersSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printers = GetPrintersSelectSerializer(Printers.objects.all(), many=True) 
        return Response(printers.data)

class GetPrintermodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printermodels = GetPrintermodelsSelectSerializer(Printermodels.objects.all(), many=True) 
        return Response(printermodels.data)

class GetPrintertypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printertypes = GetPrintertypesSelectSerializer(Printertypes.objects.all(), many=True) 
        return Response(printertypes.data)

class GetPrintersCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printersCount = GetPrintersCountSerializer(Printers.objects.count())

        return Response(printersCount.data)