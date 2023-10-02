from urllib import response
from assets.models import Unmanageds
from assets.unmanageds.serializers import GetUnmanagedsListSerializer, UnmanagedsSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class UnmanagedsViewSet(viewsets.ModelViewSet):
    queryset = Unmanageds.objects.all()
    serializer_class = UnmanagedsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Unmanageds.objects.filter(id__in=ids)
            queryset.delete()
        return response(status=status.HTTP_204_NO_CONTENT)

class GetUnmanagedsListViewSet(viewsets.ViewSet):
    queryset = Unmanageds.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        unmanageds = GetUnmanagedsListSerializer(Unmanageds.objects.all(), many=True)

        return Response(unmanageds.data)