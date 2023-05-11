from assets.printers.serializers import GetPrintersSelectSerializer, GetPrintermodelsSelectSerializer, GetPrintersSerializer, GetPrintertypesSelectSerializer, PrintermodelsSerializer, PrintersCartridgeinfosSerializer, PrintersSerializer, PrintertypesSerializer
from assets.models import Printers, Printermodels, PrintersCartridgeinfos, Printertypes
from rest_framework import viewsets, status  # import de ViewSets
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

class GetPrintersViewSet(viewsets.ModelViewSet):
    queryset = Printers.objects.all()
    serializer_class = GetPrintersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class PrintersViewSet(viewsets.ModelViewSet):
    queryset = Printers.objects.all()
    serializer_class = PrintersSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Printers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PrintermodelsViewSet(viewsets.ModelViewSet):
    queryset = Printermodels.objects.all()
    serializer_class = PrintermodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Printermodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PrintertypesViewSet(viewsets.ModelViewSet):
    queryset = Printertypes.objects.all()
    serializer_class = PrintertypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Printertypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PrintersCartridgeinfosViewSet(viewsets.ModelViewSet):
    queryset = PrintersCartridgeinfos.objects.all()
    serializer_class = PrintersCartridgeinfosSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = PrintersCartridgeinfos.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)