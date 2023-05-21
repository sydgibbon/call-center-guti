from rest_framework import serializers
from assistance.models import Changes, ChangesTickets, ChangesUsers, Recurrentchanges

class ChangesTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ChangesTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ChangesUsersSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ChangesUsers #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class ChangesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Changes #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class RecurrentchangesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Recurrentchanges #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model