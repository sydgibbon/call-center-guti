from urllib import response
from assets.models import Unmanageds
from assets.unmanageds.serializers import UnmanagedsSerializer
from rest_framework import viewsets, status
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