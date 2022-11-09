from rest_framework import serializers
from assistance.models import *

class GroupsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Groups #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class ChangesTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ChangesTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class GroupsTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = GroupsTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class ItemsTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ItemsTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class OlalevelsTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = OlalevelsTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class ProblemsTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ProblemsTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class ProjecttasksTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = ProjecttasksTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class SlalevelsTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = SlalevelsTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class SuppliersTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = SuppliersTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model

class TicketcostsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Ticketcosts #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TicketrecurrentsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Ticketrecurrents #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Tickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TicketsContractsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = TicketsContracts #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TicketsTicketsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = TicketsTickets #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TicketsUsersSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = TicketsUsers #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TicketsatisfactionsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Ticketsatisfactions #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TickettasksSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Tickettasks #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TickettemplatehiddenfieldsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Tickettemplatehiddenfields #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TickettemplatemandatoryfieldsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Tickettemplatemandatoryfields #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TickettemplatepredefinedfieldsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Tickettemplatepredefinedfields #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TickettemplatesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Tickettemplates #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class TicketvalidationsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Ticketvalidations #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class LogsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Logs #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class EventsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Events #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model
        
class RecurrentchangesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Recurrentchanges #Especificar el nombre del Model
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
        
class UsersSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Users #Especificar el nombre del Model
        fields = ['id', 'name']
        
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
        
class PlanningrecallsSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Planningrecalls #Especificar el nombre del Model
        fields = '__all__' #Para todos los atributos del model 
        
class PlanningeventcategoriesSerializer(serializers.ModelSerializer): 
    #clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)
    class Meta: #Clase meta para configurar el serializer
        model = Planningeventcategories #Especificar el nombre del Model
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