from assets.states.serializers import GetStatesSelectSerializer
from assets.models import States
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetStatesSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        states = GetStatesSelectSerializer(States.objects.all(), many=True)

        return Response(states.data)