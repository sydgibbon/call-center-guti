from assets.enclosures.serializers import CreateEnclosureSerializer, GetEnclosuremodelsSelectSerializer, GetEnclosuresCountSerializer, GetEnclosuresListSerializer, GetEnclosuresByIdSerializer
from assets.models import Enclosuremodels, Enclosures
from rest_framework import viewsets  # import de ViewSets
from assets.enclosures.serializers import EnclosuremodelsSerializer, EnclosuresSerializer, GetEnclosuremodelsSelectSerializer, GetEnclosuresSerializer, ItemsEnclosuresSerializer
from assets.models import Enclosuremodels, Enclosures, ItemsEnclosures
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetEnclosuremodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        enclosuremodels = GetEnclosuremodelsSelectSerializer(Enclosuremodels.objects.all(), many=True) 
        return Response(enclosuremodels.data)

class GetEnclosuresCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        enclosuresCount = GetEnclosuresCountSerializer(Enclosures.objects.count())

        return Response(enclosuresCount.data)
    
class EnclosuresViewSet(viewsets.ModelViewSet):
    queryset = Enclosures.objects.all()
    serializer_class = EnclosuresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Enclosures.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ItemsEnclosuresViewSet(viewsets.ModelViewSet):
    queryset = ItemsEnclosures.objects.all()
    serializer_class = ItemsEnclosuresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsEnclosures.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EnclosuremodelsViewSet(viewsets.ModelViewSet):
    queryset = Enclosuremodels.objects.all()
    serializer_class = EnclosuremodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Enclosuremodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetEnclosuresViewSet(viewsets.ModelViewSet):
    queryset = Enclosures.objects.all()
    serializer_class = GetEnclosuresSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class GetEnclosuresListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        enclosures = GetEnclosuresListSerializer(Enclosures.objects.all(), many=True)

        return Response(enclosures.data)
    
class CreateEnclosureViewSet(viewsets.GenericViewSet):
    queryset=Enclosures.objects.all()
    serializer_class = CreateEnclosureSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetEnclosuresByIdViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            enclosure = Enclosures.objects.get(id=pk)
        except Enclosures.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetEnclosuresByIdSerializer(enclosure)
        return Response(serializer.data)