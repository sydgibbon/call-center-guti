from assets.phones.serializers import GetPhonetypesSelectSerializer, GetPhonemodelsSelectSerializer, GetPhonepowersuppliesSelectSerializer
from assets.models import Phonetypes, Phonemodels, Phonepowersupplies
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPhonetypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        Phonetypes = GetPhonetypesSelectSerializer(Phonetypes.objects.all(), many=True) 
        return Response(Phonetypes.data)
    
class GetPhonemodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        Phonemodels = GetPhonemodelsSelectSerializer(Phonemodels.objects.all(), many=True) 
        return Response(Phonemodels.data)
    
class GetPhonepowersuppliesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        Phonepowersupplies = GetPhonepowersuppliesSelectSerializer(Phonepowersupplies.objects.all(), many=True) 
        return Response(Phonepowersupplies.data)