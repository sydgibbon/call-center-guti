from rest_framework import serializers  # import de serializers
from assets.models import Users

class GetUsersSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name']

class UsersSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Users #Especificar el nombre del Model
        fields = ['id', 'name']