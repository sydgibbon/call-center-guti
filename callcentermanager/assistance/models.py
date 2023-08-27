from datetime import datetime
from django.db import models
from datetime import timezone
import django


class ChangesTickets(models.Model):
    changes_id = models.PositiveIntegerField(blank=True, null=True)
    tickets_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'changes_tickets'
        unique_together = (('changes_id', 'tickets_id'),)


class GroupsTickets(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_tickets'
        unique_together = (('tickets_id', 'type', 'groups_id'),)


class ItemsTickets(models.Model):
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField(blank=True, null=True)
    tickets_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_tickets'
        unique_together = (('itemtype', 'items_id', 'tickets_id'),)


class OlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    olalevels_id = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'olalevels_tickets'
        unique_together = (('tickets_id', 'olalevels_id'),)


class ProblemsTickets(models.Model):
    problems_id = models.PositiveIntegerField(blank=True, null=True)
    tickets_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problems_tickets'
        unique_together = (('problems_id', 'tickets_id'),)


class ProjecttasksTickets(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    projecttasks_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projecttasks_tickets'
        unique_together = (('tickets_id', 'projecttasks_id'),)


class SlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    slalevels_id = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slalevels_tickets'
        unique_together = (('tickets_id', 'slalevels_id'),)


class SuppliersTickets(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    suppliers_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suppliers_tickets'
        unique_together = (('tickets_id', 'type', 'suppliers_id'),)


class Ticketcosts(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    actiontime = models.IntegerField()
    cost_time = models.DecimalField(max_digits=20, decimal_places=4)
    cost_fixed = models.DecimalField(max_digits=20, decimal_places=4)
    cost_material = models.DecimalField(max_digits=20, decimal_places=4)
    budgets_id = models.PositiveIntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ticketcosts'


class Ticketrecurrents(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()
    tickettemplates_id = models.PositiveIntegerField(blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    periodicity = models.CharField(max_length=255, blank=True, null=True)
    create_before = models.IntegerField()
    next_creation_date = models.DateTimeField(blank=True, null=True)
    calendars_id = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ticketrecurrents'


class Tickets(models.Model):
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    users_id_lastupdater = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField()
    users_id_recipient = models.PositiveIntegerField(blank=True, null=True)
    requesttypes_id = models.PositiveIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()
    global_validation = models.IntegerField()
    slas_id_ttr = models.PositiveIntegerField(blank=True, null=True)
    slas_id_tto = models.PositiveIntegerField(blank=True, null=True)
    slalevels_id_ttr = models.PositiveIntegerField(blank=True, null=True)
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    time_to_own = models.DateTimeField(blank=True, null=True)
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    sla_waiting_duration = models.IntegerField()
    ola_waiting_duration = models.IntegerField()
    olas_id_tto = models.PositiveIntegerField(blank=True, null=True)
    olas_id_ttr = models.PositiveIntegerField(blank=True, null=True)
    olalevels_id_ttr = models.PositiveIntegerField(blank=True, null=True)
    ola_ttr_begin_date = models.DateTimeField(blank=True, null=True)
    internal_time_to_resolve = models.DateTimeField(blank=True, null=True)
    internal_time_to_own = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    takeintoaccount_delay_stat = models.IntegerField()
    actiontime = models.IntegerField()
    is_deleted = models.IntegerField()
    locations_id = models.PositiveIntegerField(blank=True, null=True)
    validation_percent = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'tickets'


class TicketsContracts(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    contracts_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickets_contracts'
        unique_together = (('tickets_id', 'contracts_id'),)


class TicketsTickets(models.Model):
    tickets_id_1 = models.PositiveIntegerField(blank=True, null=True)
    tickets_id_2 = models.PositiveIntegerField(blank=True, null=True)
    link = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tickets_tickets'
        unique_together = (('tickets_id_1', 'tickets_id_2'),)


class TicketsUsers(models.Model):
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickets_users'
        unique_together = (
            ('tickets_id', 'type', 'users_id', 'alternative_email'),)


class Ticketsatisfactions(models.Model):
    tickets_id = models.PositiveIntegerField(unique=True)
    type = models.IntegerField()
    date_begin = models.DateTimeField(blank=True, null=True)
    date_answered = models.DateTimeField(blank=True, null=True)
    satisfaction = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ticketsatisfactions'


class Tickettasks(models.Model):
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    taskcategories_id = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    users_id_editor = models.PositiveIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    is_private = models.IntegerField()
    actiontime = models.IntegerField()
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    users_id_tech = models.PositiveIntegerField(blank=True, null=True)
    groups_id_tech = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    tasktemplates_id = models.PositiveIntegerField(blank=True, null=True)
    timeline_position = models.IntegerField()
    sourceitems_id = models.PositiveIntegerField(blank=True, null=True)
    sourceof_items_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickettasks'

# Verificar - Ver Abajo


class Tickettemplatehiddenfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField(blank=True, null=True)
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tickettemplatehiddenfields'
        unique_together = (('tickettemplates_id', 'num'),)


class Tickettemplatemandatoryfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField(blank=True, null=True)
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tickettemplatemandatoryfields'
        unique_together = (('tickettemplates_id', 'num'),)


class Tickettemplatepredefinedfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField(blank=True, null=True)
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickettemplatepredefinedfields'


class Tickettemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickettemplates'


class Ticketvalidations(models.Model):
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    tickets_id = models.PositiveIntegerField(blank=True, null=True)
    users_id_validate = models.PositiveIntegerField(blank=True, null=True)
    comment_submission = models.TextField(blank=True, null=True)
    comment_validation = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    submission_date = models.DateTimeField(blank=True, null=True)
    validation_date = models.DateTimeField(blank=True, null=True)
    timeline_position = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ticketvalidations'

# Verificar - Ver Arriba


class Logs(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField(blank=True, null=True)
    itemtype_link = models.CharField(max_length=100)
    linked_action = models.IntegerField()
    user_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    id_search_option = models.IntegerField()
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'logs'


class Events(models.Model):
    items_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'events'


class Agents(models.Model):
    deviceid = models.CharField(unique=True, max_length=255)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    agenttypes_id = models.PositiveIntegerField(blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    locked = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField(blank=True, null=True)
    useragent = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    port = models.CharField(max_length=6, blank=True, null=True)
    threads_networkdiscovery = models.IntegerField()
    threads_networkinventory = models.IntegerField()
    timeout_networkdiscovery = models.IntegerField()
    timeout_networkinventory = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'agents'


class Domains(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    domaintypes_id = models.PositiveIntegerField(blank=True, null=True)
    date_expiration = models.DateTimeField(blank=True, null=True)
    date_domaincreation = models.DateTimeField(blank=True, null=True)
    users_id_tech = models.PositiveIntegerField(blank=True, null=True)
    groups_id_tech = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'domains'


class Calendars(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    cache_duration = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'calendars'


class Recurrentchanges(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()
    changetemplates_id = models.PositiveIntegerField(blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    periodicity = models.CharField(max_length=255, blank=True, null=True)
    create_before = models.IntegerField()
    next_creation_date = models.DateTimeField(blank=True, null=True)
    calendars_id = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recurrentchanges'


class ChangesUsers(models.Model):
    changes_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'changes_users'
        unique_together = (
            ('changes_id', 'type', 'users_id', 'alternative_email'),)


class Changes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    status = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    users_id_recipient = models.PositiveIntegerField(blank=True, null=True)
    users_id_lastupdater = models.PositiveIntegerField(blank=True, null=True)
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories_id = models.PositiveIntegerField(blank=True, null=True)
    impactcontent = models.TextField(blank=True, null=True)
    controlistcontent = models.TextField(blank=True, null=True)
    rolloutplancontent = models.TextField(blank=True, null=True)
    backoutplancontent = models.TextField(blank=True, null=True)
    checklistcontent = models.TextField(blank=True, null=True)
    global_validation = models.IntegerField()
    validation_percent = models.IntegerField()
    actiontime = models.IntegerField()
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'changes'


class GroupsKnowbaseitems(models.Model):
    knowbaseitems_id = models.PositiveIntegerField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_knowbaseitems'


class GroupsProblems(models.Model):
    problems_id = models.PositiveIntegerField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_problems'
        unique_together = (('problems_id', 'type', 'groups_id'),)


class GroupsReminders(models.Model):
    reminders_id = models.PositiveIntegerField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_reminders'


class GroupsRssfeeds(models.Model):
    rssfeeds_id = models.PositiveIntegerField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_rssfeeds'


class GroupsUsers(models.Model):
    users_id = models.PositiveIntegerField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    is_dynamic = models.IntegerField()
    is_manager = models.IntegerField()
    is_userdelegate = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_users'
        unique_together = (('users_id', 'groups_id'),)

class Problems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    status = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    users_id_recipient = models.PositiveIntegerField(blank=True, null=True)
    users_id_lastupdater = models.PositiveIntegerField(blank=True, null=True)
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories_id = models.PositiveIntegerField(blank=True, null=True)
    impactcontent = models.TextField(blank=True, null=True)
    causecontent = models.TextField(blank=True, null=True)
    symptomcontent = models.TextField(blank=True, null=True)
    actiontime = models.IntegerField()
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'problems'


class ProblemsUsers(models.Model):
    problems_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problems_users'
        unique_together = (
            ('problems_id', 'type', 'users_id', 'alternative_email'),)


class Planningexternalevents(models.Model):
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    planningexternaleventtemplates_id = models.PositiveIntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    users_id_guests = models.TextField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    rrule = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    planningeventcategories_id = models.PositiveIntegerField(blank=True, null=True)
    background = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'planningexternalevents'


class Planningexternaleventtemplates(models.Model):
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    before_time = models.IntegerField()
    rrule = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    planningeventcategories_id = models.PositiveIntegerField(blank=True, null=True)
    background = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'planningexternaleventtemplates'


class Planningrecalls(models.Model):
    items_id = models.PositiveIntegerField(blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    before_time = models.IntegerField()
    when = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planningrecalls'
        unique_together = (('itemtype', 'items_id', 'users_id'),)


class Planningeventcategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'planningeventcategories'


class Crontasklogs(models.Model):
    crontasks_id = models.PositiveIntegerField(blank=True, null=True)
    crontasklogs_id = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField()
    state = models.IntegerField()
    elapsed = models.FloatField()
    volume = models.IntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crontasklogs'


class Crontasks(models.Model):
    itemtype = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    frequency = models.IntegerField()
    param = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()
    mode = models.IntegerField()
    allowmode = models.IntegerField()
    hourmin = models.IntegerField()
    hourmax = models.IntegerField()
    logs_lifetime = models.IntegerField()
    lastrun = models.DateTimeField(blank=True, null=True)
    lastcode = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, default=django.utils.timezone.now)
    date_creation = models.DateTimeField(blank=True, default=django.utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'crontasks'
        unique_together = (('itemtype', 'name'),)
