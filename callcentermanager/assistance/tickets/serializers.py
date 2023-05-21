from rest_framework import serializers

from assistance.models import GroupsTickets, ItemsTickets, OlalevelsTickets, ProblemsTickets, SlalevelsTickets, SuppliersTickets, Ticketcosts, Ticketrecurrents, Tickets, TicketsContracts, TicketsTickets, TicketsUsers, Ticketsatisfactions, Tickettemplatehiddenfields, Tickettemplatemandatoryfields, Tickettemplatepredefinedfields, Tickettemplates, Ticketvalidations

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