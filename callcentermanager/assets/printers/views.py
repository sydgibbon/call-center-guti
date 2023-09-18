from assets.printers.serializers import CreatePrinterSerializer, GetPrintersListSerializer, GetPrintersSelectSerializer, GetPrintermodelsSelectSerializer, GetPrintertypesSelectSerializer, GetPrintersCountSerializer
from assets.models import Printers, Printermodels, Printertypes
from rest_framework import viewsets  # import de ViewSets
from assets.printers.serializers import GetPrintersSelectSerializer, GetPrintermodelsSelectSerializer, GetPrintersSerializer, GetPrintertypesSelectSerializer, PrintermodelsSerializer, PrintersCartridgeinfosSerializer, PrintersSerializer, PrintertypesSerializer, GetPrintersByIdSerializer
from assets.models import Printers, Printermodels, PrintersCartridgeinfos, Printertypes
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPrintersSelectViewSet(viewsets.ViewSet):
    queryset = Printers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printers = GetPrintersSelectSerializer(Printers.objects.all(), many=True) 
        return Response(printers.data)

class GetPrintermodelsSelectViewSet(viewsets.ViewSet):
    queryset = Printermodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printermodels = GetPrintermodelsSelectSerializer(Printermodels.objects.all(), many=True) 
        return Response(printermodels.data)

class GetPrintertypesSelectViewSet(viewsets.ViewSet):
    queryset = Printertypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printertypes = GetPrintertypesSelectSerializer(Printertypes.objects.all(), many=True) 
        return Response(printertypes.data)

class GetPrintersCountViewSet(viewsets.ViewSet):
    queryset = Printers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printersCount = GetPrintersCountSerializer(self.queryset)

        return Response(printersCount.data)
class GetPrintersViewSet(viewsets.ModelViewSet):
    queryset = Printers.objects.filter(is_deleted=0)
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

class GetPrintersListViewSet(viewsets.ViewSet):
    queryset = Printers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        printers = GetPrintersListSerializer(Printers.objects.all(), many=True)

        return Response(printers.data)

class CreatePrinterViewSet(viewsets.GenericViewSet):
    queryset=Printers.objects.all()
    serializer_class = CreatePrinterSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class GetPrintersByIdViewSet(viewsets.ViewSet):
    queryset = Printers.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            printer = Printers.objects.get(id=pk)
        except Printers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetPrintersByIdSerializer(printer)
        return Response(serializer.data)