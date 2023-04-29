from assets.users.serializers import GetUsersSelectSerializer
from assets.models import Users
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetUsersSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        users = GetUsersSelectSerializer(Users.objects.all(), many=True) 
        return Response(users.data)

class GetTechInChargeSelectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        users = GetUsersSelectSerializer(Users.objects.all(), many=True) 
        return Response(users.data)