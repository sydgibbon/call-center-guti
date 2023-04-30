from assets.printers.serializers import GetPrintermodelsSelectSerializer, GetPrintertypesSelectSerializer
from assets.models import Printermodels, Printertypes
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

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