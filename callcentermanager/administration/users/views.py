from administration.users.serializers import GetUsersSerializer
from assets.models import Users
from rest_framework import viewsets, status, generics  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetUsersViewSet(viewsets.ViewSet):
    queryset = Users.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        users = GetUsersSerializer(Users.objects.all(), many=True)

        return Response(users.data)