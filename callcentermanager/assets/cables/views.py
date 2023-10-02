from assets.cables.serializers import CablesSerializer, CablestrandsSerializer, CabletypesSerializer, CreateCableSerializer, GetCablesListSerializer, GetCablesSerializer, GetCabletypesSelectSerializer, GetCablestrandsSelectSerializer, GetSocketsSelectSerializer, GetSocketmodelsSelectSerializer, GetCablesByIdSerializer
from assets.models import Cables, Cabletypes, Cablestrands, Sockets, Socketmodels
from rest_framework import viewsets, status, generics  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetCabletypesSelectViewSet(viewsets.ViewSet):
    queryset = Cabletypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cabletypes = GetCabletypesSelectSerializer(Cabletypes.objects.all(), many=True) 
        return Response(cabletypes.data)
    
class GetCablestrandsSelectViewSet(viewsets.ViewSet):
    queryset = Cablestrands.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cablestrands = GetCablestrandsSelectSerializer(Cablestrands.objects.all(), many=True) 
        return Response(cablestrands.data)
    
class GetSocketsSelectViewSet(viewsets.ViewSet):
    queryset = Sockets.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        sockets = GetSocketsSelectSerializer(Sockets.objects.all(), many=True) 
        return Response(sockets.data)
        
class GetSocketmodelsSelectViewSet(viewsets.ViewSet):
    queryset = Socketmodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        socketmodels = GetSocketmodelsSelectSerializer(Socketmodels.objects.all(), many=True) 
        return Response(socketmodels.data)
    
class CablesViewSet(viewsets.ModelViewSet):
    queryset = Cables.objects.all()
    serializer_class = CablesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cables.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetCablesViewSet(viewsets.ModelViewSet):
    queryset = Cables.objects.all()
    serializer_class = GetCablesSerializer
    http_method_names = ['get']

class CablestrandsViewSet(viewsets.ModelViewSet):
    queryset = Cablestrands.objects.all()
    serializer_class = CablestrandsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cablestrands.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CabletypesViewSet(viewsets.ModelViewSet):
    queryset = Cabletypes.objects.all()
    serializer_class = CabletypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Cabletypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetCablesListViewSet(viewsets.ViewSet):
    queryset = Cables.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        cables = GetCablesListSerializer(Cables.objects.all(), many=True)

        return Response(cables.data)
    
class CreateCableViewSet(viewsets.GenericViewSet):
    queryset=Cables.objects.all()
    serializer_class = CreateCableSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class GetCablesByIdViewSet(viewsets.ViewSet):
    queryset = Cables.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            cable = Cables.objects.get(id=pk)
        except Cables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetCablesByIdSerializer(cable)
        return Response(serializer.data)

class UpdateCableByIdViewSet(viewsets.ModelViewSet):
    queryset = Cables.objects.all()
    serializer_class = CreateCableSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class DeleteCableByIdViewSet(viewsets.ModelViewSet):
    queryset = Cables.objects.all()
    serializer_class = CablesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']
