from assets.users.serializers import GetUsersSelectSerializer, UsersSerializer
from assets.models import Users
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetUsersSelectViewSet(viewsets.ViewSet):
    queryset = Users.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        users = GetUsersSelectSerializer(Users.objects.all(), many=True) 
        return Response(users.data)

class GetTechInChargeSelectViewSet(viewsets.ViewSet):
    queryset = Users.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        users = GetUsersSelectSerializer(Users.objects.all(), many=True) 
        return Response(users.data)
    
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Users.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)