from assets.snmpcredentials.serializers import GetSnmpcredentialsSelectSerializer, SnmpcredentialsSerializer
from assets.models import Snmpcredentials
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetSnmpcredentialsSelectViewSet(viewsets.ViewSet):
    queryset = Snmpcredentials.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        snmpcredentials = GetSnmpcredentialsSelectSerializer(Snmpcredentials.objects.all(), many=True) 
        return Response(snmpcredentials.data)

class SnmpcredentialsViewSet(viewsets.ModelViewSet):
    queryset = Snmpcredentials.objects.all()
    serializer_class = SnmpcredentialsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Snmpcredentials.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)