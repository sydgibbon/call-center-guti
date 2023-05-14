from assets.pdu.serializers import GetPdutypesSelectSerializer, GetPdumodelsSelectSerializer, GetPdusCountSerializer
from assets.models import Pdutypes, Pdumodels, Pdus
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPdutypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdutypes = GetPdutypesSelectSerializer(Pdutypes.objects.all(), many=True) 
        return Response(pdutypes.data)
    
class GetPdumodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdumodels = GetPdumodelsSelectSerializer(Pdumodels.objects.all(), many=True) 
        return Response(pdumodels.data)

class GetPdusCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        pdusCount = GetPdusCountSerializer(Pdus.objects.count())

        return Response(pdusCount.data)