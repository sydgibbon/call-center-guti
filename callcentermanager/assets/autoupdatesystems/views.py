from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer, GetAutoupdatesystemsSelectSerializer
from assets.models import Autoupdatesystems
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class GetAutoupdatesystemsSelectViewSet(viewsets.ViewSet):
    queryset = Autoupdatesystems.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        autoupdatesystems = GetAutoupdatesystemsSelectSerializer(Autoupdatesystems.objects.all(), many=True) 
        return Response(autoupdatesystems.data)

class AutoupdatesystemsViewSet(viewsets.ModelViewSet):
    queryset = Autoupdatesystems.objects.all()
    serializer_class = AutoupdatesystemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Autoupdatesystems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)