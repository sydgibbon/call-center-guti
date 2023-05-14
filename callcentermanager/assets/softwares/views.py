from assets.softwares.serializers import GetSoftwarecategoriesSelectSerializer, GetSoftwaresCountSerializer, GetSoftwarelicensesCountSerializer
from assets.models import Softwarecategories, Softwares, Softwarelicenses
from rest_framework import viewsets  # import de ViewSets
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