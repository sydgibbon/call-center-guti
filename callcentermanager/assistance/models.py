from django.db import models

class ChangesTickets(models.Model):
    changes_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'changes_tickets'
        unique_together = (('changes_id', 'tickets_id'),)

class GroupsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_tickets'
        unique_together = (('tickets_id', 'type', 'groups_id'),)

class ItemsTickets(models.Model):
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'items_tickets'
        unique_together = (('itemtype', 'items_id', 'tickets_id'),)

class ItemsTickets(models.Model):
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'items_tickets'
        unique_together = (('itemtype', 'items_id', 'tickets_id'),)

class OlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    olalevels_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'olalevels_tickets'
        unique_together = (('tickets_id', 'olalevels_id'),)

class ProblemsTickets(models.Model):
    problems_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'problems_tickets'
        unique_together = (('problems_id', 'tickets_id'),)

class ProjecttasksTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    projecttasks_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'projecttasks_tickets'
        unique_together = (('tickets_id', 'projecttasks_id'),)

class SlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    slalevels_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slalevels_tickets'
        unique_together = (('tickets_id', 'slalevels_id'),)

class SuppliersTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    suppliers_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suppliers_tickets'
        unique_together = (('tickets_id', 'type', 'suppliers_id'),)

class Ticketcosts(models.Model):
    tickets_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    actiontime = models.IntegerField()
    cost_time = models.DecimalField(max_digits=20, decimal_places=4)
    cost_fixed = models.DecimalField(max_digits=20, decimal_places=4)
    cost_material = models.DecimalField(max_digits=20, decimal_places=4)
    budgets_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'ticketcosts'

class Ticketrecurrents(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()
    tickettemplates_id = models.PositiveIntegerField()
    begin_date = models.DateTimeField(blank=True, null=True)
    periodicity = models.CharField(max_length=255, blank=True, null=True)
    create_before = models.IntegerField()
    next_creation_date = models.DateTimeField(blank=True, null=True)
    calendars_id = models.PositiveIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ticketrecurrents'

class Tickets(models.Model):
    entities_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users_id_lastupdater = models.PositiveIntegerField()
    status = models.IntegerField()
    users_id_recipient = models.PositiveIntegerField()
    requesttypes_id = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories_id = models.PositiveIntegerField()
    type = models.IntegerField()
    global_validation = models.IntegerField()
    slas_id_ttr = models.PositiveIntegerField()
    slas_id_tto = models.PositiveIntegerField()
    slalevels_id_ttr = models.PositiveIntegerField()
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    time_to_own = models.DateTimeField(blank=True, null=True)
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    sla_waiting_duration = models.IntegerField()
    ola_waiting_duration = models.IntegerField()
    olas_id_tto = models.PositiveIntegerField()
    olas_id_ttr = models.PositiveIntegerField()
    olalevels_id_ttr = models.PositiveIntegerField()
    ola_ttr_begin_date = models.DateTimeField(blank=True, null=True)
    internal_time_to_resolve = models.DateTimeField(blank=True, null=True)
    internal_time_to_own = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    takeintoaccount_delay_stat = models.IntegerField()
    actiontime = models.IntegerField()
    is_deleted = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    validation_percent = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickets'

class TicketsContracts(models.Model):
    tickets_id = models.PositiveIntegerField()
    contracts_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'tickets_contracts'
        unique_together = (('tickets_id', 'contracts_id'),)


class TicketsTickets(models.Model):
    tickets_id_1 = models.PositiveIntegerField()
    tickets_id_2 = models.PositiveIntegerField()
    link = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tickets_tickets'
        unique_together = (('tickets_id_1', 'tickets_id_2'),)


class TicketsUsers(models.Model):
    tickets_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickets_users'
        unique_together = (('tickets_id', 'type', 'users_id', 'alternative_email'),)


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
    tickets_id = models.PositiveIntegerField()
    taskcategories_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    users_id_editor = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)
    is_private = models.IntegerField()
    actiontime = models.IntegerField()
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tasktemplates_id = models.PositiveIntegerField()
    timeline_position = models.IntegerField()
    sourceitems_id = models.PositiveIntegerField()
    sourceof_items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'tickettasks'

# Verificar - Ver Abajo

class Tickettemplatehiddenfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tickettemplatehiddenfields'
        unique_together = (('tickettemplates_id', 'num'),)


class Tickettemplatemandatoryfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tickettemplatemandatoryfields'
        unique_together = (('tickettemplates_id', 'num'),)


class Tickettemplatepredefinedfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickettemplatepredefinedfields'


class Tickettemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickettemplates'


class Ticketvalidations(models.Model):
    entities_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()
    users_id_validate = models.PositiveIntegerField()
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

