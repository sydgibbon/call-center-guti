from assets.softwares.serializers import CreateSoftwareSerializer, GetSoftwarecategoriesSelectSerializer, GetSoftwaresCountSerializer, GetSoftwarelicensesCountSerializer, GetSoftwaresListSerializer
from assets.models import Softwarecategories, Softwares, Softwarelicenses
from rest_framework import viewsets  # import de ViewSets
from assets.softwares.serializers import GetSoftwarecategoriesSelectSerializer, GetSoftwaresSerializer, SoftwarecategoriesSerializer, SoftwarelicensesSerializer, SoftwaresSerializer, SoftwareversionsSerializer, GetSoftwaresByIdSerializer
from assets.models import Softwarecategories, Softwarelicenses, Softwares, Softwareversions
from rest_framework import viewsets, status  # import de ViewSets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from assets.generics.serializers import DeleteMultipleSerializer

class GetSoftwarecategoriesSelectViewSet(viewsets.ViewSet):
    queryset = Softwarecategories.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwarecategories = GetSoftwarecategoriesSelectSerializer(Softwarecategories.objects.all(), many=True) 
        return Response(softwarecategories.data)
    
class GetSoftwaresCountViewSet(viewsets.ViewSet):
    queryset = Softwares.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwaresCount = GetSoftwaresCountSerializer(self.queryset)

        return Response(softwaresCount.data)
    
class GetSoftwarelicensesCountViewSet(viewsets.ViewSet):
    queryset = Softwarelicenses.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwarelicensesCount = GetSoftwarelicensesCountSerializer(self.queryset)

        return Response(softwarelicensesCount.data)
class GetSoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.filter(is_deleted=0)
    serializer_class = GetSoftwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']
    
class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = SoftwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwares.objects.filter(id__in=ids)
            queryset.delete()
        # Desde aca empezo fran
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SoftwarecategoriesViewSet(viewsets.ModelViewSet):
    queryset = Softwarecategories.objects.all()
    serializer_class = SoftwarecategoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwarecategories.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwarelicensesViewSet(viewsets.ModelViewSet):
    queryset = Softwarelicenses.objects.all()
    serializer_class = SoftwarelicensesSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwarelicenses.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SoftwareversionsViewSet(viewsets.ModelViewSet):
    queryset = Softwareversions.objects.all()
    serializer_class = SoftwareversionsSerializer
    permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Softwareversions.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetSoftwaresListViewSet(viewsets.ViewSet):
    queryset = Softwares.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request, format=None):
        softwares = GetSoftwaresListSerializer(Softwares.objects.all(), many=True)

        return Response(softwares.data)

class CreateSoftwareViewSet(viewsets.GenericViewSet):
    queryset=Softwares.objects.all()
    serializer_class = CreateSoftwareSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['post']

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetSoftwaresByIdViewSet(viewsets.ViewSet):
    queryset = Softwares.objects.filter(is_deleted=0)
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['get']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            software = Softwares.objects.get(id=pk)
        except Softwares.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetSoftwaresByIdSerializer(software)
        return Response(serializer.data)
    
class UpdateSoftwareByIdViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = CreateSoftwareSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['put']

    def list(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteSoftwareByIdViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = SoftwaresSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    http_method_names = ['delete']

    def destroy(self, request, pk=None):
        software = Softwares.objects.get(id=pk)
        software.is_deleted = 1
        software.save()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['delete'], serializer_class=DeleteMultipleSerializer)
    def delete_multiple(self, request):
        object_ids = request.data.get('object_ids', [])
        serializer = DeleteMultipleSerializer(data=request.data)
        if serializer.is_valid():

            deleted_objects = []  # To store the deleted objects

            for object_id in object_ids:
                try:
                    obj = Softwares.objects.get(pk=object_id)
                    obj.is_deleted = 1
                    obj.save()
                    deleted_objects.append(object_id)
                except Softwares.DoesNotExist:
                    pass  # Handle the case when the object does not exist

            return Response({'message': f'{len(deleted_objects)} objects deleted successfully'})
        else:
            return Response(serializer.errors, status=400)