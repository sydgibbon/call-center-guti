
from rest_framework import serializers  # import de serializers
from assets.models import Groups

class GetGroupsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id', 'name']

class GroupsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Groups #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model