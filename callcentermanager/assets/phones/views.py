from assets.phones.serializers import GetPhonesSelectSerializer, GetPhonetypesSelectSerializer, GetPhonemodelsSelectSerializer, GetPhonepowersuppliesSelectSerializer
from assets.models import Phones, Phonetypes, Phonemodels, Phonepowersupplies
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPhonesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phones = GetPhonesSelectSerializer(Phones.objects.all(), many=True) 
        return Response(phones.data)
    

class GetPhonetypesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetPhonetypesSelectSerializer(Phonetypes.objects.all(), many=True) 
        return Response(states.data)
    
class GetPhonemodelsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetPhonemodelsSelectSerializer(Phonemodels.objects.all(), many=True) 
        return Response(states.data)
    
class GetPhonepowersuppliesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetPhonepowersuppliesSelectSerializer(Phonepowersupplies.objects.all(), many=True) 
        return Response(states.data)