from django.shortcuts import render

from rest_framework import viewsets  # import de ViewSets
from assistance.serializers import *  # import de todos los serializers,
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.
class ChangesTicketsViewSet(viewsets.ModelViewSet):
    queryset = ChangesTickets.objects.all()
    serializer_class = ChangesTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GroupsTicketsViewSet(viewsets.ModelViewSet):
    queryset = GroupsTickets.objects.all()
    serializer_class = GroupsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ItemsTicketsViewSet(viewsets.ModelViewSet):
    queryset = ItemsTickets.objects.all()
    serializer_class = ItemsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OlalevelsTicketsViewSet(viewsets.ModelViewSet):
    queryset = OlalevelsTickets.objects.all()
    serializer_class = OlalevelsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProblemsTicketsViewSet(viewsets.ModelViewSet):
    queryset = ProblemsTickets.objects.all()
    serializer_class = ProblemsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProjecttasksTicketsViewSet(viewsets.ModelViewSet):
    queryset = ProjecttasksTickets.objects.all()
    serializer_class = ProjecttasksTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SlalevelsTicketsTicketsViewSet(viewsets.ModelViewSet):
    queryset = SlalevelsTicketsTickets.objects.all()
    serializer_class = SlalevelsTicketsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SuppliersTicketsViewSet(viewsets.ModelViewSet):
    queryset = SuppliersTickets.objects.all()
    serializer_class = SuppliersTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketcostsViewSet(viewsets.ModelViewSet):
    queryset = Ticketcosts.objects.all()
    serializer_class = TicketcostsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketrecurrentsViewSet(viewsets.ModelViewSet):
    queryset = Ticketrecurrents.objects.all()
    serializer_class = TicketrecurrentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketsContractsViewSet(viewsets.ModelViewSet):
    queryset = TicketsContracts.objects.all()
    serializer_class = TicketsContractsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketsTicketsViewSet(viewsets.ModelViewSet):
    queryset = TicketsTickets.objects.all()
    serializer_class = TicketsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketsUsersViewSet(viewsets.ModelViewSet):
    queryset = TicketsUsers.objects.all()
    serializer_class = TicketsUsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketsatisfactionsViewSet(viewsets.ModelViewSet):
    queryset = Ticketsatisfactions.objects.all()
    serializer_class = TicketsatisfactionsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TickettasksViewSet(viewsets.ModelViewSet):
    queryset = Tickettasks.objects.all()
    serializer_class = TickettasksSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TickettemplatehiddenfieldsViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplatehiddenfields.objects.all()
    serializer_class = TickettemplatehiddenfieldsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TickettemplatemandatoryfieldsViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplatemandatoryfields.objects.all()
    serializer_class = TickettemplatemandatoryfieldsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TickettemplatepredefinedfieldsViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplatepredefinedfields.objects.all()
    serializer_class = TickettemplatepredefinedfieldsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TickettemplatesViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplates.objects.all()
    serializer_class = TickettemplatesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TicketvalidationsViewSet(viewsets.ModelViewSet):
    queryset = Ticketvalidations.objects.all()
    serializer_class = TicketvalidationsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RecurrentchangesViewSet(viewsets.ModelViewSet):
    queryset = Recurrentchanges.objects.all()
    serializer_class = RecurrentchangesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ChangesUsersViewSet(viewsets.ModelViewSet):
    queryset = ChangesUsers.objects.all()
    serializer_class = ChangesUsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ChangesViewSet(viewsets.ModelViewSet):
    queryset = Changes.objects.all()
    serializer_class = ChangesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProblemsViewSet(viewsets.ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProblemsUsersViewSet(viewsets.ModelViewSet):
    queryset = ProblemsUsers.objects.all()
    serializer_class = ProblemsUsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PlanningexternaleventsViewSet(viewsets.ModelViewSet):
    queryset = Planningexternalevents.objects.all()
    serializer_class = PlanningexternaleventsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PlanningexternaleventtemplatesViewSet(viewsets.ModelViewSet):
    queryset = Planningexternaleventtemplates.objects.all()
    serializer_class = PlanningexternaleventtemplatesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PlanningrecallsViewSet(viewsets.ModelViewSet):
    queryset = Planningrecalls.objects.all()
    serializer_class = PlanningrecallsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PlanningeventcategoriesViewSet(viewsets.ModelViewSet):
    queryset = Planningeventcategories.objects.all()
    serializer_class = PlanningeventcategoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CrontasklogsViewSet(viewsets.ModelViewSet):
    queryset = Crontasklogs.objects.all()
    serializer_class = CrontasklogsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CrontasksViewSet(viewsets.ModelViewSet):
    queryset = Crontasks.objects.all()
    serializer_class = CrontasksSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)