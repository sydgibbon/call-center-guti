from assets.cartridges.serializers import CartridgeitemsPrintermodelsSerializer, CartridgeitemsSerializer, CartridgeitemtypesSerializer, CartridgesSerializer, CreateCartridgeitemSerializer, GetCartridgeItemsSerializer, GetCartridgeitemsListSerializer, GetCartridgeitemtypesSelectSerializer, GetCartridgeitemsByIdSerializer
from assets.models import Cartridgeitems, CartridgeitemsPrintermodels, Cartridgeitemtypes, Cartridges
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetCartridgeitemtypesSelectViewSet(viewsets.ViewSet):
    queryset = Cartridgeitemtypes.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cartridgeitemtypes = GetCartridgeitemtypesSelectSerializer(Cartridgeitemtypes.objects.all(), many=True) 
        return Response(cartridgeitemtypes.data)

class CartridgesViewSet(viewsets.ModelViewSet):
    queryset = Cartridges.objects.all()
    serializer_class = CartridgesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cartridges.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CartridgeitemsViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitems.objects.all()
    serializer_class = CartridgeitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cartridgeitems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartridgeitemsPrintermodelsViewSet(viewsets.ModelViewSet):
    queryset = CartridgeitemsPrintermodels.objects.all()
    serializer_class = CartridgeitemsPrintermodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = CartridgeitemsPrintermodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartridgeitemtypesViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitemtypes.objects.all()
    serializer_class = CartridgeitemtypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cartridgeitemtypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetCartridgeItemsViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitems.objects.filter(is_deleted=0)
    serializer_class = GetCartridgeItemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class GetCartridgeitemsListViewSet(viewsets.ViewSet):
    queryset = Cartridgeitems.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cartridgeitems = GetCartridgeitemsListSerializer(Cartridgeitems.objects.all(), many=True)

        return Response(cartridgeitems.data)
    
    
class CreateCartridgeitemViewSet(viewsets.GenericViewSet):
    queryset=Cartridgeitems.objects.all()
    serializer_class = CreateCartridgeitemSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetCartridgeitemsByIdViewSet(viewsets.ViewSet):
    queryset = Cartridgeitems.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            cartridgeitem = Cartridgeitems.objects.get(id=pk)
        except Cartridgeitems.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetCartridgeitemsByIdSerializer(cartridgeitem)
        return Response(serializer.data)