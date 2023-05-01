from assets.softwares.serializers import GetSoftwarecategoriesSelectSerializer
from assets.models import Softwarecategories
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetSoftwarecategoriesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwarecategories = GetSoftwarecategoriesSelectSerializer(Softwarecategories.objects.all(), many=True) 
        return Response(softwarecategories.data)