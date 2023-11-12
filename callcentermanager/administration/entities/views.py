from administration.entities.serializers import GetEntitiesSerializer
from assets.models import Entities
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetEntitiesViewSet(viewsets.ViewSet):
    queryset = Entities.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        entities = GetEntitiesSerializer(Entities.objects.all(), many=True)

        return Response(entities.data)