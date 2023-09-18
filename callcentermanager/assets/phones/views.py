from assets.phones.serializers import CreatePhoneSerializer, GetPhonesListSerializer, GetPhonesSelectSerializer, GetPhonetypesSelectSerializer, GetPhonemodelsSelectSerializer, GetPhonepowersuppliesSelectSerializer, GetPhonesCountSerializer
from assets.phones.serializers import GetPhonesSelectSerializer, GetPhonesSerializer, GetPhonetypesSelectSerializer, GetPhonemodelsSelectSerializer, GetPhonepowersuppliesSelectSerializer, PhonemodelsSerializer, PhonepowersuppliesSerializer, PhonesSerializer, PhonetypesSerializer, GetPhonesByIdSerializer
from assets.models import Phones, Phonetypes, Phonemodels, Phonepowersupplies
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetPhonesSelectViewSet(viewsets.ViewSet):
    queryset = Phones.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phones = GetPhonesSelectSerializer(Phones.objects.all(), many=True) 
        return Response(phones.data) 

class GetPhonetypesSelectViewSet(viewsets.ViewSet):
    queryset = Phonetypes.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phonetypes = GetPhonetypesSelectSerializer(Phonetypes.objects.all(), many=True) 
        return Response(phonetypes.data)
    
class GetPhonemodelsSelectViewSet(viewsets.ViewSet):
    queryset = Phonemodels.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phonemodels = GetPhonemodelsSelectSerializer(Phonemodels.objects.all(), many=True) 
        return Response(phonemodels.data)
    
class GetPhonepowersuppliesSelectViewSet(viewsets.ViewSet):
    queryset = Phonepowersupplies.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phonepowersupplies = GetPhonepowersuppliesSelectSerializer(Phonepowersupplies.objects.all(), many=True) 
        return Response(phonepowersupplies.data)
    
class GetPhonesCountViewSet(viewsets.ViewSet):
    queryset = Phones.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phonesCount = GetPhonesCountSerializer(self.queryset)

        return Response(phonesCount.data)
class GetPhonesViewSet(viewsets.ModelViewSet):
    queryset = Phones.objects.filter(is_deleted=0)
    serializer_class = GetPhonesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

class PhonesViewSet(viewsets.ModelViewSet):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phones.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PhonemodelsViewSet(viewsets.ModelViewSet):
    queryset = Phonemodels.objects.all()
    serializer_class = PhonemodelsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phonemodels.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhonepowersuppliesViewSet(viewsets.ModelViewSet):
    queryset = Phonepowersupplies.objects.all()
    serializer_class = PhonepowersuppliesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phonepowersupplies.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhonetypesViewSet(viewsets.ModelViewSet):
    queryset = Phonetypes.objects.all()
    serializer_class = PhonetypesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Phonetypes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetPhonesListViewSet(viewsets.ViewSet):
    queryset = Phones.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        phones = GetPhonesListSerializer(Phones.objects.all(), many=True)

        return Response(phones.data)
    
class CreatePhoneViewSet(viewsets.GenericViewSet):
    queryset=Phones.objects.all()
    serializer_class = CreatePhoneSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetPhonesByIdViewSet(viewsets.ViewSet):
    queryset = Phones.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            phone = Phones.objects.get(id=pk)
        except Phones.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetPhonesByIdSerializer(phone)
        return Response(serializer.data)