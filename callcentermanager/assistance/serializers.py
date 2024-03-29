from rest_framework import serializers
from assistance.models import *
        
class LogsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Logs #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class ProblemsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Problems #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class ProblemsUsersSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ProblemsUsers #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model 
        
class PlanningrecallsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Planningrecalls #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model 
 