from assistance.models import Crontasklogs, Crontasks, ProjecttasksTickets, Tickettasks
from rest_framework import serializers


class ProjecttasksTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ProjecttasksTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class TickettasksSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Tickettasks #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class CrontasklogsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Crontasklogs #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model 
        
class CrontasksSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Crontasks #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model