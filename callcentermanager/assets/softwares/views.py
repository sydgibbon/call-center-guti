from assets.softwares.serializers import GetSoftwarecategoriesSelectSerializer, GetSoftwaresCountSerializer, GetSoftwarelicensesCountSerializer
from assets.models import Softwarecategories, Softwares, Softwarelicenses
from rest_framework import viewsets  # import de ViewSets
from assets.softwares.serializers import GetSoftwarecategoriesSelectSerializer, GetSoftwaresSerializer, SoftwarecategoriesSerializer, SoftwarelicensesSerializer, SoftwaresSerializer, SoftwareversionsSerializer
from assets.models import Softwarecategories, Softwarelicenses, Softwares, Softwareversions
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetSoftwarecategoriesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwarecategories = GetSoftwarecategoriesSelectSerializer(Softwarecategories.objects.all(), many=True) 
        return Response(softwarecategories.data)
    
class GetSoftwaresCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwaresCount = GetSoftwaresCountSerializer(Softwares.objects.count())

        return Response(softwaresCount.data)
    
class GetSoftwarelicensesCountViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwarelicensesCount = GetSoftwarelicensesCountSerializer(Softwarelicenses.objects.count())

        return Response(softwarelicensesCount.data)
class GetSoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = GetSoftwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    
class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = SoftwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwares.objects.filter(id__in=ids)
            queryset.delete()
        # Desde aca empezo fran
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SoftwarecategoriesViewSet(viewsets.ModelViewSet):
    queryset = Softwarecategories.objects.all()
    serializer_class = SoftwarecategoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwarecategories.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwarelicensesViewSet(viewsets.ModelViewSet):
    queryset = Softwarelicenses.objects.all()
    serializer_class = SoftwarelicensesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwarelicenses.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwareversionsViewSet(viewsets.ModelViewSet):
    queryset = Softwareversions.objects.all()
    serializer_class = SoftwareversionsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwareversions.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
