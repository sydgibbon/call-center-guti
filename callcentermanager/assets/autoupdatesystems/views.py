from assets.autoupdatesystems.serializers import GetAutoupdatesystemsSelectSerializer
from assets.models import Autoupdatesystems
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetAutoupdatesystemsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        autoupdatesystems = GetAutoupdatesystemsSelectSerializer(Autoupdatesystems.objects.all(), many=True) 
        return Response(autoupdatesystems.data)