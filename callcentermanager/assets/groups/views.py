from assets.groups.serializers import GetGroupsSelectSerializer
from assets.models import Groups
from rest_framework import viewsets  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetGroupsSelectViewSet(viewsets.ViewSet):
    queryset = Groups.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        groups = GetGroupsSelectSerializer(Groups.objects.all(), many=True) 
        return Response(groups.data)
    

class GetGroupInChargeSelectViewSet(viewsets.ViewSet):
    queryset = Groups.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        groups = GetGroupsSelectSerializer(Groups.objects.all(), many=True) 
        return Response(groups.data)