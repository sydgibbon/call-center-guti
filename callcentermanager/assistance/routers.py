from rest_framework.routers import DefaultRouter
from assistance.events.views import EventsViewSet, PlanningeventcategoriesViewSet, PlanningexternaleventsViewSet, PlanningexternaleventtemplatesViewSet 
from assistance.changes.views import ChangesTicketsViewSet, ChangesUsersViewSet, ChangesViewSet, RecurrentchangesViewSet
from assistance.tasks.views import CrontasklogsViewSet, CrontasksViewSet, ProjecttasksTicketsViewSet, TickettasksViewSet
from assistance.tickets.views import GroupsTicketsViewSet, ItemsTicketsViewSet, OlalevelsTicketsViewSet, ProblemsTicketsViewSet, SlalevelsTicketsViewSet, SuppliersTicketsViewSet, TicketcostsViewSet, TicketrecurrentsViewSet, TicketsContractsViewSet, TicketsTicketsViewSet, TicketsUsersViewSet, TicketsViewSet, TicketsatisfactionsViewSet, TickettemplatehiddenfieldsViewSet, TickettemplatemandatoryfieldsViewSet, TickettemplatepredefinedfieldsViewSet, TickettemplatesViewSet, TicketvalidationsViewSet
from .views import *


router=DefaultRouter()
router.register(r'changestickets', ChangesTicketsViewSet, basename='changestickets')
router.register(r'groupstickets', GroupsTicketsViewSet, basename='groupstickets')
router.register(r'itemstickets', ItemsTicketsViewSet, basename='itemstickets')
router.register(r'olalevelstickets', OlalevelsTicketsViewSet, basename='olalevelstickets')
router.register(r'problemstickets', ProblemsTicketsViewSet, basename='problemstickets')
router.register(r'projecttaskstickets', ProjecttasksTicketsViewSet, basename='projecttaskstickets')
router.register(r'slalevelstickets', SlalevelsTicketsViewSet, basename='slalevelstickets')
router.register(r'supplierstickets', SuppliersTicketsViewSet, basename='supplierstickets')
router.register(r'ticketcosts', TicketcostsViewSet, basename='ticketcosts')
router.register(r'ticketrecurrents', TicketrecurrentsViewSet, basename='ticketrecurrents')
router.register(r'tickets', TicketsViewSet, basename='tickets')
router.register(r'ticketscontracts', TicketsContractsViewSet, basename='ticketscontracts')
router.register(r'ticketstickets', TicketsTicketsViewSet, basename='ticketstickets')
router.register(r'ticketsusers', TicketsUsersViewSet, basename='ticketsusers')
router.register(r'ticketsatisfactions', TicketsatisfactionsViewSet, basename='ticketsatisfactions')
router.register(r'tickettasks', TickettasksViewSet, basename='tickettasks')
router.register(r'tickettemplatehiddenfields', TickettemplatehiddenfieldsViewSet, basename='tickettemplatehiddenfields')
router.register(r'tickettemplatemandatoryfields', TickettemplatemandatoryfieldsViewSet, basename='tickettemplatemandatoryfields')
router.register(r'tickettemplatepredefinedfields', TickettemplatepredefinedfieldsViewSet, basename='tickettemplatepredefinedfields')
router.register(r'tickettemplates', TickettemplatesViewSet, basename='tickettemplates')
router.register(r'ticketvalidations', TicketvalidationsViewSet, basename='ticketvalidations')
router.register(r'logs', LogsViewSet, basename='logs')
router.register(r'events', EventsViewSet, basename='events')
router.register(r'recurrentchanges', RecurrentchangesViewSet, basename='recurrentchanges')
router.register(r'changesusers', ChangesUsersViewSet, basename='changesusers')
router.register(r'changes', ChangesViewSet, basename='changes')
router.register(r'problems', ProblemsViewSet, basename='problems')
router.register(r'problemsusers', ProblemsUsersViewSet, basename='problemsusers')
router.register(r'planningexternalevents', PlanningexternaleventsViewSet, basename='planningexternalevents')
router.register(r'planningexternaleventtemplates', PlanningexternaleventtemplatesViewSet, basename='planningexternaleventtemplates')
router.register(r'planningrecalls', PlanningrecallsViewSet, basename='planningrecalls')
router.register(r'planningeventcategories', PlanningeventcategoriesViewSet, basename='planningeventcategories')
router.register(r'crontasklogs', CrontasklogsViewSet, basename='crontasklogs')
router.register(r'Crontasks', CrontasksViewSet, basename='Crontasks')
