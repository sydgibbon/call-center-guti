from assets.pdus.serializers import CreatePduSerializer, GetPdusListSerializer, GetPdusSerializer, GetPdutypesSelectSerializer, GetPdumodelsSelectSerializer, PdumodelsSerializer, PdusPlugsSerializer, PdusRacksSerializer, PdusSerializer, PdutypesSerializer, GetPdusByIdSerializer
from assets.models import Pdus, PdusPlugs, PdusRacks, Pdutypes, Pdumodels
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from assets.pdus.serializers import GetPdutypesSelectSerializer, GetPdumodelsSelectSerializer, GetPdusCountSerializer
from assets.models import Pdutypes, Pdumodels, Pdus
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPdutypesSelectViewSet(viewsets.ViewSet):
    queryset = Pdutypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdutypes = GetPdutypesSelectSerializer(Pdutypes.objects.all(), many=True) 
        return Response(pdutypes.data)
    
class GetPdumodelsSelectViewSet(viewsets.ViewSet):
    queryset = Pdumodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdumodels = GetPdumodelsSelectSerializer(Pdumodels.objects.all(), many=True) 
        return Response(pdumodels.data)

class GetPdusCountViewSet(viewsets.ViewSet):
    queryset = Pdus.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdusCount = GetPdusCountSerializer(self.queryset)

        return Response(pdusCount.data)

class GetPdutypesSelectViewSet(viewsets.ViewSet):
    queryset = Pdutypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdutypes = GetPdutypesSelectSerializer(Pdutypes.objects.all(), many=True) 
        return Response(pdutypes.data)
    
class GetPdumodelsSelectViewSet(viewsets.ViewSet):
    queryset = Pdumodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdumodels = GetPdumodelsSelectSerializer(Pdumodels.objects.all(), many=True) 
        return Response(pdumodels.data)

class GetPdusViewSet(viewsets.ModelViewSet):
    queryset = Pdus.objects.filter(is_deleted=0)
    serializer_class = GetPdusSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
class PdusViewSet(viewsets.ModelViewSet):
    queryset = Pdus.objects.all()
    serializer_class = PdusSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Pdus.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PdustypesViewSet(viewsets.ModelViewSet):
    queryset = Pdutypes.objects.all()
    serializer_class = PdutypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Pdutypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PdumodelsViewSet(viewsets.ModelViewSet):
    queryset = Pdumodels.objects.all()
    serializer_class = PdumodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Pdumodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PdusPlugsViewSet(viewsets.ModelViewSet):
    queryset = PdusPlugs.objects.all()
    serializer_class = PdusPlugsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = PdusPlugs.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PdusRacksViewSet(viewsets.ModelViewSet):
    queryset = PdusRacks.objects.all()
    serializer_class = PdusRacksSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = PdusRacks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetPdusListViewSet(viewsets.ViewSet):
    queryset = Pdus.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdus = GetPdusListSerializer(Pdus.objects.all(), many=True)

        return Response(pdus.data)

class CreatePduViewSet(viewsets.GenericViewSet):
    queryset=Pdus.objects.all()
    serializer_class = CreatePduSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetPdusByIdViewSet(viewsets.ViewSet):
    queryset = Pdus.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            pdu = Pdus.objects.get(id=pk)
        except Pdus.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetPdusByIdSerializer(pdu)
        return Response(serializer.data)
    
class UpdatePduByIdViewSet(viewsets.ModelViewSet):
    queryset = Pdus.objects.all()
    serializer_class = CreatePduSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class DeletePduByIdViewSet(viewsets.ModelViewSet):
    queryset = Pdus.objects.all()
    serializer_class = PdusSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        pdu = Pdus.objects.get(id=pk)
        pdu.is_deleted = 1
        pdu.save()
        return Response(status=status.HTTP_200_OK)