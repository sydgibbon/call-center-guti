from rest_framework import viewsets, status
from assistance.changes.serializers import ChangesSerializer, ChangesTicketsSerializer, ChangesUsersSerializer, RecurrentchangesSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from assistance.models import Changes, ChangesTickets, ChangesUsers, Recurrentchanges
from rest_framework.response import Response

class ChangesTicketsViewSet(viewsets.ModelViewSet):
    queryset = ChangesTickets.objects.all()
    serializer_class = ChangesTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ChangesTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangesUsersViewSet(viewsets.ModelViewSet):
    queryset = ChangesUsers.objects.all()
    serializer_class = ChangesUsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ChangesUsers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangesViewSet(viewsets.ModelViewSet):
    queryset = Changes.objects.all()
    serializer_class = ChangesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Changes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecurrentchangesViewSet(viewsets.ModelViewSet):
    queryset = Recurrentchanges.objects.all()
    serializer_class = RecurrentchangesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Recurrentchanges.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)