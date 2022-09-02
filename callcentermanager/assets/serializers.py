from rest_framework import serializers #import de serializers
from assets.models import * #import de todos los callcenterdata, proximamente se mueve a assets

class ComputerSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Computers #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model