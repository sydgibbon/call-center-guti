from rest_framework import viewsets #import de ViewSets
from assets.serializers import * #import de todos los serializers,

#ViewSets para cada Serializer
class ComputersViewSet(viewsets.ModelViewSet):
    queryset= Computers.objects.all()
    serializer_class = ComputersSerializer