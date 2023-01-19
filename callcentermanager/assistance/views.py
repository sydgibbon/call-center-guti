from django.shortcuts import render

from rest_framework import viewsets, status  # import de ViewSets
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
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ChangesTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupsTicketsViewSet(viewsets.ModelViewSet):
    queryset = GroupsTickets.objects.all()
    serializer_class = GroupsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = GroupsTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemsTicketsViewSet(viewsets.ModelViewSet):
    queryset = ItemsTickets.objects.all()
    serializer_class = ItemsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ItemsTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OlalevelsTicketsViewSet(viewsets.ModelViewSet):
    queryset = OlalevelsTickets.objects.all()
    serializer_class = OlalevelsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = OlalevelsTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProblemsTicketsViewSet(viewsets.ModelViewSet):
    queryset = ProblemsTickets.objects.all()
    serializer_class = ProblemsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ProblemsTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjecttasksTicketsViewSet(viewsets.ModelViewSet):
    queryset = ProjecttasksTickets.objects.all()
    serializer_class = ProjecttasksTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ProjecttasksTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SlalevelsTicketsViewSet(viewsets.ModelViewSet):
    queryset = SlalevelsTickets.objects.all()
    serializer_class = SlalevelsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = SlalevelsTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SuppliersTicketsViewSet(viewsets.ModelViewSet):
    queryset = SuppliersTickets.objects.all()
    serializer_class = SuppliersTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = SuppliersTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketcostsViewSet(viewsets.ModelViewSet):
    queryset = Ticketcosts.objects.all()
    serializer_class = TicketcostsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Ticketcosts.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketrecurrentsViewSet(viewsets.ModelViewSet):
    queryset = Ticketrecurrents.objects.all()
    serializer_class = TicketrecurrentsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Ticketrecurrents.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Tickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketsContractsViewSet(viewsets.ModelViewSet):
    queryset = TicketsContracts.objects.all()
    serializer_class = TicketsContractsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = TicketsContracts.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketsTicketsViewSet(viewsets.ModelViewSet):
    queryset = TicketsTickets.objects.all()
    serializer_class = TicketsTicketsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = TicketsTickets.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketsUsersViewSet(viewsets.ModelViewSet):
    queryset = TicketsUsers.objects.all()
    serializer_class = TicketsUsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = TicketsUsers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketsatisfactionsViewSet(viewsets.ModelViewSet):
    queryset = Ticketsatisfactions.objects.all()
    serializer_class = TicketsatisfactionsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Ticketsatisfactions.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TickettasksViewSet(viewsets.ModelViewSet):
    queryset = Tickettasks.objects.all()
    serializer_class = TickettasksSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Tickettasks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TickettemplatehiddenfieldsViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplatehiddenfields.objects.all()
    serializer_class = TickettemplatehiddenfieldsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Tickettemplatehiddenfields.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TickettemplatemandatoryfieldsViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplatemandatoryfields.objects.all()
    serializer_class = TickettemplatemandatoryfieldsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Tickettemplatemandatoryfields.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TickettemplatepredefinedfieldsViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplatepredefinedfields.objects.all()
    serializer_class = TickettemplatepredefinedfieldsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Tickettemplatepredefinedfields.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TickettemplatesViewSet(viewsets.ModelViewSet):
    queryset = Tickettemplates.objects.all()
    serializer_class = TickettemplatesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Tickettemplates.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketvalidationsViewSet(viewsets.ModelViewSet):
    queryset = Ticketvalidations.objects.all()
    serializer_class = TicketvalidationsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Ticketvalidations.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Logs.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Events.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecurrentchangesViewSet(viewsets.ModelViewSet):
    queryset = Recurrentchanges.objects.all()
    serializer_class = RecurrentchangesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Recurrentchanges.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangesUsersViewSet(viewsets.ModelViewSet):
    queryset = ChangesUsers.objects.all()
    serializer_class = ChangesUsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ChangesUsers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangesViewSet(viewsets.ModelViewSet):
    queryset = Changes.objects.all()
    serializer_class = ChangesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Changes.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProblemsViewSet(viewsets.ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Problems.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProblemsUsersViewSet(viewsets.ModelViewSet):
    queryset = ProblemsUsers.objects.all()
    serializer_class = ProblemsUsersSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = ProblemsUsers.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlanningexternaleventsViewSet(viewsets.ModelViewSet):
    queryset = Planningexternalevents.objects.all()
    serializer_class = PlanningexternaleventsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Planningexternalevents.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlanningexternaleventtemplatesViewSet(viewsets.ModelViewSet):
    queryset = Planningexternaleventtemplates.objects.all()
    serializer_class = PlanningexternaleventtemplatesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Planningexternaleventtemplates.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlanningrecallsViewSet(viewsets.ModelViewSet):
    queryset = Planningrecalls.objects.all()
    serializer_class = PlanningrecallsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Planningrecalls.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlanningeventcategoriesViewSet(viewsets.ModelViewSet):
    queryset = Planningeventcategories.objects.all()
    serializer_class = PlanningeventcategoriesSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Planningeventcategories.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CrontasklogsViewSet(viewsets.ModelViewSet):
    queryset = Crontasklogs.objects.all()
    serializer_class = CrontasklogsSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Crontasklogs.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CrontasksViewSet(viewsets.ModelViewSet):
    queryset = Crontasks.objects.all()
    serializer_class = CrontasksSerializer
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        ids = request.query_params.get('ids').split(',')
        if ids:
            queryset = Crontasks.objects.filter(id__in=ids)
            queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)