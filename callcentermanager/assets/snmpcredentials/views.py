from assets.snmpcredentials.serializers import GetSnmpcredentialsSelectSerializer
from assets.models import Snmpcredentials
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetSnmpcredentialsSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        snmpcredentials = GetSnmpcredentialsSelectSerializer(Snmpcredentials.objects.all(), many=True) 
        return Response(snmpcredentials.data)