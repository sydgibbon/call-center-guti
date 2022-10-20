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

class Logs(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    itemtype_link = models.CharField(max_length=100)
    linked_action = models.IntegerField()
    user_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    id_search_option = models.IntegerField()
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'logs'

class Events(models.Model):
    items_id = models.PositiveIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'events'

class Recurrentchanges(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()
    changetemplates_id = models.PositiveIntegerField()
    begin_date = models.DateTimeField(blank=True, null=True)
    periodicity = models.CharField(max_length=255, blank=True, null=True)
    create_before = models.IntegerField()
    next_creation_date = models.DateTimeField(blank=True, null=True)
    calendars_id = models.PositiveIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recurrentchanges'

class ChangesUsers(models.Model):
    changes_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'changes_users'
        unique_together = (('changes_id', 'type', 'users_id', 'alternative_email'),)

class Changes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    status = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    users_id_recipient = models.PositiveIntegerField()
    users_id_lastupdater = models.PositiveIntegerField()
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories_id = models.PositiveIntegerField()
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
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'changes'

class Users(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    password_last_update = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    use_mode = models.IntegerField()
    list_limit = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    auths_id = models.PositiveIntegerField()
    authtype = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_sync = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    usertitles_id = models.PositiveIntegerField()
    usercategories_id = models.PositiveIntegerField()
    date_format = models.IntegerField(blank=True, null=True)
    number_format = models.IntegerField(blank=True, null=True)
    names_format = models.IntegerField(blank=True, null=True)
    csv_delimiter = models.CharField(max_length=1, blank=True, null=True)
    is_ids_visible = models.IntegerField(blank=True, null=True)
    use_flat_dropdowntree = models.IntegerField(blank=True, null=True)
    show_jobs_at_login = models.IntegerField(blank=True, null=True)
    priority_1 = models.CharField(max_length=20, blank=True, null=True)
    priority_2 = models.CharField(max_length=20, blank=True, null=True)
    priority_3 = models.CharField(max_length=20, blank=True, null=True)
    priority_4 = models.CharField(max_length=20, blank=True, null=True)
    priority_5 = models.CharField(max_length=20, blank=True, null=True)
    priority_6 = models.CharField(max_length=20, blank=True, null=True)
    followup_private = models.IntegerField(blank=True, null=True)
    task_private = models.IntegerField(blank=True, null=True)
    default_requesttypes_id = models.PositiveIntegerField(blank=True, null=True)
    password_forget_token = models.CharField(max_length=40, blank=True, null=True)
    password_forget_token_date = models.DateTimeField(blank=True, null=True)
    user_dn = models.TextField(blank=True, null=True)
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    show_count_on_tabs = models.IntegerField(blank=True, null=True)
    refresh_views = models.IntegerField(blank=True, null=True)
    set_default_tech = models.IntegerField(blank=True, null=True)
    personal_token = models.CharField(max_length=255, blank=True, null=True)
    personal_token_date = models.DateTimeField(blank=True, null=True)
    api_token = models.CharField(max_length=255, blank=True, null=True)
    api_token_date = models.DateTimeField(blank=True, null=True)
    cookie_token = models.CharField(max_length=255, blank=True, null=True)
    cookie_token_date = models.DateTimeField(blank=True, null=True)
    display_count_on_home = models.IntegerField(blank=True, null=True)
    notification_to_myself = models.IntegerField(blank=True, null=True)
    duedateok_color = models.CharField(max_length=255, blank=True, null=True)
    duedatewarning_color = models.CharField(max_length=255, blank=True, null=True)
    duedatecritical_color = models.CharField(max_length=255, blank=True, null=True)
    duedatewarning_less = models.IntegerField(blank=True, null=True)
    duedatecritical_less = models.IntegerField(blank=True, null=True)
    duedatewarning_unit = models.CharField(max_length=255, blank=True, null=True)
    duedatecritical_unit = models.CharField(max_length=255, blank=True, null=True)
    display_options = models.TextField(blank=True, null=True)
    is_deleted_ldap = models.IntegerField()
    pdffont = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    keep_devices_when_purging_item = models.IntegerField(blank=True, null=True)
    privatebookmarkorder = models.TextField(blank=True, null=True)
    backcreated = models.IntegerField(blank=True, null=True)
    task_state = models.IntegerField(blank=True, null=True)
    palette = models.CharField(max_length=20, blank=True, null=True)
    page_layout = models.CharField(max_length=20, blank=True, null=True)
    fold_menu = models.IntegerField(blank=True, null=True)
    fold_search = models.IntegerField(blank=True, null=True)
    savedsearches_pinned = models.TextField(blank=True, null=True)
    timeline_order = models.CharField(max_length=20, blank=True, null=True)
    itil_layout = models.TextField(blank=True, null=True)
    richtext_layout = models.CharField(max_length=20, blank=True, null=True)
    set_default_requester = models.IntegerField(blank=True, null=True)
    lock_autolock_mode = models.IntegerField(blank=True, null=True)
    lock_directunlock_notification = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    highcontrast_css = models.IntegerField(blank=True, null=True)
    plannings = models.TextField(blank=True, null=True)
    sync_field = models.CharField(max_length=255, blank=True, null=True)
    groups_id = models.PositiveIntegerField()
    users_id_supervisor = models.PositiveIntegerField()
    timezone = models.CharField(max_length=50, blank=True, null=True)
    default_dashboard_central = models.CharField(max_length=100, blank=True, null=True)
    default_dashboard_assets = models.CharField(max_length=100, blank=True, null=True)
    default_dashboard_helpdesk = models.CharField(max_length=100, blank=True, null=True)
    default_dashboard_mini_ticket = models.CharField(max_length=100, blank=True, null=True)
    default_central_tab = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'
        unique_together = (('name', 'authtype', 'auths_id'),)

class Problems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    status = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    users_id_recipient = models.PositiveIntegerField()
    users_id_lastupdater = models.PositiveIntegerField()
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories_id = models.PositiveIntegerField()
    impactcontent = models.TextField(blank=True, null=True)
    causecontent = models.TextField(blank=True, null=True)
    symptomcontent = models.TextField(blank=True, null=True)
    actiontime = models.IntegerField()
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problems'

class ProblemsUsers(models.Model):
    problems_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problems_users'
        unique_together = (('problems_id', 'type', 'users_id', 'alternative_email'),)

class Planningexternalevents(models.Model):
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    planningexternaleventtemplates_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    users_id_guests = models.TextField(blank=True, null=True)
    groups_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    rrule = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    planningeventcategories_id = models.PositiveIntegerField()
    background = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planningexternalevents'


class Planningexternaleventtemplates(models.Model):
    entities_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    before_time = models.IntegerField()
    rrule = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    planningeventcategories_id = models.PositiveIntegerField()
    background = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planningexternaleventtemplates'


class Planningrecalls(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    users_id = models.PositiveIntegerField()
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
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planningeventcategories'

class Crontasklogs(models.Model):
    crontasks_id = models.PositiveIntegerField()
    crontasklogs_id = models.PositiveIntegerField()
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
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crontasks'
        unique_together = (('itemtype', 'name'),)

