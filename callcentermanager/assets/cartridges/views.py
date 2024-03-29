from assets.cartridges.serializers import CartridgeitemsPrintermodelsSerializer, CartridgeitemsSerializer, CartridgeitemtypesSerializer, CartridgesSerializer, CreateCartridgeitemSerializer, GetCartridgeItemsSerializer, GetCartridgeitemsListSerializer, GetCartridgeitemtypesSelectSerializer, GetCartridgeitemsByIdSerializer
from assets.models import Cartridgeitems, CartridgeitemsPrintermodels, Cartridgeitemtypes, Cartridges
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from assets.generics.serializers import DeleteMultipleSerializer

class GetCartridgeitemtypesSelectViewSet(viewsets.ViewSet):
    queryset = Cartridgeitemtypes.objects.all()
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
    
class UpdateCartridgeitemByIdViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitems.objects.all()
    serializer_class = CreateCartridgeitemSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class DeleteCartridgeitemByIdViewSet(viewsets.ModelViewSet):
    queryset = Cartridgeitems.objects.all()
    serializer_class = CartridgeitemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        cartridgeitem = Cartridgeitems.objects.get(id=pk)
        cartridgeitem.is_deleted = 1
        cartridgeitem.save()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['delete'], serializer_class=DeleteMultipleSerializer)
    def delete_multiple(self, request):
        object_ids = request.data.get('object_ids', [])
        serializer = DeleteMultipleSerializer(data=request.data)
        if serializer.is_valid():

            deleted_objects = []  # To store the deleted objects

            for object_id in object_ids:
                try:
                    obj = Cartridgeitems.objects.get(pk=object_id)
                    obj.is_deleted = 1
                    obj.save()
                    deleted_objects.append(object_id)
                except Cartridgeitems.DoesNotExist:
                    pass  # Handle the case when the object does not exist

            return Response({'message': f'{len(deleted_objects)} objects deleted successfully'})
        else:
            return Response(serializer.errors, status=400)
