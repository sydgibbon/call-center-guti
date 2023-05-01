from assets.phones.serializers import GetPhonetypesSelectSerializer, GetPhonemodelsSelectSerializer, GetPhonepowersuppliesSelectSerializer
from assets.models import Phonetypes, Phonemodels, Phonepowersupplies
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPhonetypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phonetypes = GetPhonetypesSelectSerializer(Phonetypes.objects.all(), many=True) 
        return Response(phonetypes.data)
    
class GetPhonemodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phonemodels = GetPhonemodelsSelectSerializer(Phonemodels.objects.all(), many=True) 
        return Response(phonemodels.data)
    
class GetPhonepowersuppliesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phonepowersupplies = GetPhonepowersuppliesSelectSerializer(Phonepowersupplies.objects.all(), many=True) 
        return Response(phonepowersupplies.data)