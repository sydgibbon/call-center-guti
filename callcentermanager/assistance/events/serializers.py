from rest_framework import serializers
from assistance.models import Events, Planningeventcategories, Planningexternalevents, Planningexternaleventtemplates


class EventsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Events #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class PlanningexternaleventsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Planningexternalevents #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model 

class PlanningexternaleventtemplatesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Planningexternaleventtemplates #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model 

class PlanningeventcategoriesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Planningeventcategories #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model 