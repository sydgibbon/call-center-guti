from rest_framework import viewsets #import de ViewSets
from assets.serializers import * #import de todos los serializers,

#ViewSets para cada Serializer
class ComputersViewSet(viewsets.ModelViewSet):
    queryset= Computers.objects.all()
    serializer_class = ComputersSerializer

class MonitorsViewSet(viewsets.ModelViewSet):
    queryset= Monitors.objects.all()
    serializer_class = MonitorsSerializer

class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset= Softwares.objects.all()
    serializer_class = SoftwaresSerializer

#Desde aca empezo fran

class DevicemotherboardsViewSet(viewsets.ModelViewSet):
    queryset= Devicemotherboards.objects.all()
    serializer_class = DevicemotherboardsSerializer

class DevicenetworkcardmodelsViewSet(viewsets.ModelViewSet):
    queryset= Devicenetworkcardmodels.objects.all()
    serializer_class = DevicenetworkcardmodelsSerializer 