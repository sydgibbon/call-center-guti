from django.db import models

class GlpiAgents(models.Model):
    deviceid = models.CharField(unique=True, max_length=255)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    agenttypes_id = models.PositiveIntegerField()
    last_contact = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    locked = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    useragent = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    port = models.CharField(max_length=6, blank=True, null=True)
    threads_networkdiscovery = models.IntegerField()
    threads_networkinventory = models.IntegerField()
    timeout_networkdiscovery = models.IntegerField()
    timeout_networkinventory = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_agents'


class GlpiAgenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_agenttypes'


class GlpiAlerts(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    type = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'glpi_alerts'
        unique_together = (('itemtype', 'items_id', 'type'),)


class GlpiApiclients(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    ipv4_range_start = models.BigIntegerField(blank=True, null=True)
    ipv4_range_end = models.BigIntegerField(blank=True, null=True)
    ipv6 = models.CharField(max_length=255, blank=True, null=True)
    app_token = models.CharField(max_length=255, blank=True, null=True)
    app_token_date = models.DateTimeField(blank=True, null=True)
    dolog_method = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_apiclients'


class GlpiApplianceenvironments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_applianceenvironments'


class GlpiAppliances(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    appliancetypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    applianceenvironments_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    states_id = models.PositiveIntegerField()
    externalidentifier = models.CharField(unique=True, max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    is_helpdesk_visible = models.IntegerField()
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_appliances'


class GlpiAppliancesItems(models.Model):
    appliances_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_appliances_items'
        unique_together = (('appliances_id', 'items_id', 'itemtype'),)


class GlpiAppliancesItemsRelations(models.Model):
    appliances_items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_appliances_items_relations'


class GlpiAppliancetypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    externalidentifier = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_appliancetypes'


class GlpiAuthldapreplicates(models.Model):
    authldaps_id = models.PositiveIntegerField()
    host = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    timeout = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_authldapreplicates'


class GlpiAuthldaps(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    basedn = models.CharField(max_length=255, blank=True, null=True)
    rootdn = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField()
    condition = models.TextField(blank=True, null=True)
    login_field = models.CharField(max_length=255, blank=True, null=True)
    sync_field = models.CharField(max_length=255, blank=True, null=True)
    use_tls = models.IntegerField()
    group_field = models.CharField(max_length=255, blank=True, null=True)
    group_condition = models.TextField(blank=True, null=True)
    group_search_type = models.IntegerField()
    group_member_field = models.CharField(max_length=255, blank=True, null=True)
    email1_field = models.CharField(max_length=255, blank=True, null=True)
    realname_field = models.CharField(max_length=255, blank=True, null=True)
    firstname_field = models.CharField(max_length=255, blank=True, null=True)
    phone_field = models.CharField(max_length=255, blank=True, null=True)
    phone2_field = models.CharField(max_length=255, blank=True, null=True)
    mobile_field = models.CharField(max_length=255, blank=True, null=True)
    comment_field = models.CharField(max_length=255, blank=True, null=True)
    use_dn = models.IntegerField()
    time_offset = models.IntegerField()
    deref_option = models.IntegerField()
    title_field = models.CharField(max_length=255, blank=True, null=True)
    category_field = models.CharField(max_length=255, blank=True, null=True)
    language_field = models.CharField(max_length=255, blank=True, null=True)
    entity_field = models.CharField(max_length=255, blank=True, null=True)
    entity_condition = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_default = models.IntegerField()
    is_active = models.IntegerField()
    rootdn_passwd = models.CharField(max_length=255, blank=True, null=True)
    registration_number_field = models.CharField(max_length=255, blank=True, null=True)
    email2_field = models.CharField(max_length=255, blank=True, null=True)
    email3_field = models.CharField(max_length=255, blank=True, null=True)
    email4_field = models.CharField(max_length=255, blank=True, null=True)
    location_field = models.CharField(max_length=255, blank=True, null=True)
    responsible_field = models.CharField(max_length=255, blank=True, null=True)
    pagesize = models.IntegerField()
    ldap_maxlimit = models.IntegerField()
    can_support_pagesize = models.IntegerField()
    picture_field = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    inventory_domain = models.CharField(max_length=255, blank=True, null=True)
    tls_certfile = models.TextField(blank=True, null=True)
    tls_keyfile = models.TextField(blank=True, null=True)
    use_bind = models.IntegerField()
    timeout = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_authldaps'


class GlpiAuthmails(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    connect_string = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_authmails'


class GlpiAutoupdatesystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_autoupdatesystems'


class GlpiBlacklistedmailcontents(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_blacklistedmailcontents'


class GlpiBlacklists(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_blacklists'


class GlpiBudgets(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=20, decimal_places=4)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    budgettypes_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_budgets'


class GlpiBudgettypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_budgettypes'


class GlpiBusinesscriticities(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    businesscriticities_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_businesscriticities'
        unique_together = (('businesscriticities_id', 'name'),)


class GlpiCables(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    itemtype_endpoint_a = models.CharField(max_length=255, blank=True, null=True)
    itemtype_endpoint_b = models.CharField(max_length=255, blank=True, null=True)
    items_id_endpoint_a = models.PositiveIntegerField()
    items_id_endpoint_b = models.PositiveIntegerField()
    socketmodels_id_endpoint_a = models.PositiveIntegerField()
    socketmodels_id_endpoint_b = models.PositiveIntegerField()
    sockets_id_endpoint_a = models.PositiveIntegerField()
    sockets_id_endpoint_b = models.PositiveIntegerField()
    cablestrands_id = models.PositiveIntegerField()
    color = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    states_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    cabletypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cables'


class GlpiCablestrands(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cablestrands'


class GlpiCabletypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cabletypes'


class GlpiCalendars(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    cache_duration = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_calendars'


class GlpiCalendarsHolidays(models.Model):
    calendars_id = models.PositiveIntegerField()
    holidays_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_calendars_holidays'
        unique_together = (('calendars_id', 'holidays_id'),)


class GlpiCalendarsegments(models.Model):
    calendars_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    day = models.IntegerField()
    begin = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_calendarsegments'


class GlpiCartridgeitems(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    cartridgeitemtypes_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField()
    stock_target = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cartridgeitems'


class GlpiCartridgeitemsPrintermodels(models.Model):
    cartridgeitems_id = models.PositiveIntegerField()
    printermodels_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_cartridgeitems_printermodels'
        unique_together = (('printermodels_id', 'cartridgeitems_id'),)


class GlpiCartridgeitemtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cartridgeitemtypes'


class GlpiCartridges(models.Model):
    entities_id = models.PositiveIntegerField()
    cartridgeitems_id = models.PositiveIntegerField()
    printers_id = models.PositiveIntegerField()
    date_in = models.DateField(blank=True, null=True)
    date_use = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    pages = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cartridges'


class GlpiCertificates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    certificatetypes_id = models.PositiveIntegerField()
    dns_name = models.CharField(max_length=255, blank=True, null=True)
    dns_suffix = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    locations_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    is_autosign = models.IntegerField()
    date_expiration = models.DateField(blank=True, null=True)
    states_id = models.PositiveIntegerField()
    command = models.TextField(blank=True, null=True)
    certificate_request = models.TextField(blank=True, null=True)
    certificate_item = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_certificates'


class GlpiCertificatesItems(models.Model):
    certificates_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_certificates_items'
        unique_together = (('certificates_id', 'itemtype', 'items_id'),)


class GlpiCertificatetypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_certificatetypes'


class GlpiChangecosts(models.Model):
    changes_id = models.PositiveIntegerField()
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
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changecosts'


class GlpiChanges(models.Model):
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
        managed = False
        db_table = 'glpi_changes'


class GlpiChangesGroups(models.Model):
    changes_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changes_groups'
        unique_together = (('changes_id', 'type', 'groups_id'),)


class GlpiChangesItems(models.Model):
    changes_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changes_items'
        unique_together = (('changes_id', 'itemtype', 'items_id'),)


class GlpiChangesProblems(models.Model):
    changes_id = models.PositiveIntegerField()
    problems_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changes_problems'
        unique_together = (('changes_id', 'problems_id'),)


class GlpiChangesSuppliers(models.Model):
    changes_id = models.PositiveIntegerField()
    suppliers_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changes_suppliers'
        unique_together = (('changes_id', 'type', 'suppliers_id'),)


class GlpiChangesTickets(models.Model):
    changes_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changes_tickets'
        unique_together = (('changes_id', 'tickets_id'),)


class GlpiChangesUsers(models.Model):
    changes_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changes_users'
        unique_together = (('changes_id', 'type', 'users_id', 'alternative_email'),)


class GlpiChangetasks(models.Model):
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    changes_id = models.PositiveIntegerField()
    taskcategories_id = models.PositiveIntegerField()
    state = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    users_id_editor = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)
    actiontime = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tasktemplates_id = models.PositiveIntegerField()
    timeline_position = models.IntegerField()
    is_private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changetasks'


class GlpiChangetemplatehiddenfields(models.Model):
    changetemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changetemplatehiddenfields'
        unique_together = (('changetemplates_id', 'num'),)


class GlpiChangetemplatemandatoryfields(models.Model):
    changetemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changetemplatemandatoryfields'
        unique_together = (('changetemplates_id', 'num'),)


class GlpiChangetemplatepredefinedfields(models.Model):
    changetemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changetemplatepredefinedfields'


class GlpiChangetemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changetemplates'


class GlpiChangevalidations(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    users_id = models.PositiveIntegerField()
    changes_id = models.PositiveIntegerField()
    users_id_validate = models.PositiveIntegerField()
    comment_submission = models.TextField(blank=True, null=True)
    comment_validation = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    submission_date = models.DateTimeField(blank=True, null=True)
    validation_date = models.DateTimeField(blank=True, null=True)
    timeline_position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changevalidations'


class GlpiClusters(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    states_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    clustertypes_id = models.PositiveIntegerField()
    autoupdatesystems_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_clusters'


class GlpiClustertypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_clustertypes'


class GlpiComputerantiviruses(models.Model):
    computers_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    antivirus_version = models.CharField(max_length=255, blank=True, null=True)
    signature_version = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    is_uptodate = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_expiration = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computerantiviruses'


class GlpiComputermodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computermodels'


class GlpiComputers(models.Model):
    entities_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    autoupdatesystems_id = models.PositiveIntegerField()
    locations_id = models.PositiveIntegerField()
    networks_id = models.PositiveIntegerField()
    computermodels_id = models.PositiveIntegerField()
    computertypes_id = models.PositiveIntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()
    last_inventory_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computers'


class GlpiComputersItems(models.Model):
    items_id = models.PositiveIntegerField()
    computers_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_computers_items'


class GlpiComputertypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computertypes'


class GlpiComputervirtualmachines(models.Model):
    entities_id = models.PositiveIntegerField()
    computers_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    virtualmachinestates_id = models.PositiveIntegerField()
    virtualmachinesystems_id = models.PositiveIntegerField()
    virtualmachinetypes_id = models.PositiveIntegerField()
    uuid = models.CharField(max_length=255)
    vcpu = models.IntegerField()
    ram = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computervirtualmachines'


class GlpiConfigs(models.Model):
    context = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_configs'
        unique_together = (('context', 'name'),)


class GlpiConsumableitems(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    consumableitemtypes_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField()
    stock_target = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_consumableitems'


class GlpiConsumableitemtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_consumableitemtypes'


class GlpiConsumables(models.Model):
    entities_id = models.PositiveIntegerField()
    consumableitems_id = models.PositiveIntegerField()
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_consumables'


class GlpiContacts(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    contacttypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    usertitles_id = models.PositiveIntegerField()
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contacts'


class GlpiContactsSuppliers(models.Model):
    suppliers_id = models.PositiveIntegerField()
    contacts_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_contacts_suppliers'
        unique_together = (('suppliers_id', 'contacts_id'),)


class GlpiContacttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contacttypes'


class GlpiContractcosts(models.Model):
    contracts_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    budgets_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_contractcosts'


class GlpiContracts(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    contracttypes_id = models.PositiveIntegerField()
    begin_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField()
    notice = models.IntegerField()
    periodicity = models.IntegerField()
    billing = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    accounting_number = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    week_begin_hour = models.TimeField()
    week_end_hour = models.TimeField()
    saturday_begin_hour = models.TimeField()
    saturday_end_hour = models.TimeField()
    use_saturday = models.IntegerField()
    sunday_begin_hour = models.TimeField()
    sunday_end_hour = models.TimeField()
    use_sunday = models.IntegerField()
    max_links_allowed = models.IntegerField()
    alert = models.IntegerField()
    renewal = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_template = models.IntegerField()
    states_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contracts'


class GlpiContractsItems(models.Model):
    contracts_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_contracts_items'
        unique_together = (('contracts_id', 'itemtype', 'items_id'),)


class GlpiContractsSuppliers(models.Model):
    suppliers_id = models.PositiveIntegerField()
    contracts_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_contracts_suppliers'
        unique_together = (('suppliers_id', 'contracts_id'),)


class GlpiContracttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contracttypes'


class GlpiCrontasklogs(models.Model):
    crontasks_id = models.PositiveIntegerField()
    crontasklogs_id = models.PositiveIntegerField()
    date = models.DateTimeField()
    state = models.IntegerField()
    elapsed = models.FloatField()
    volume = models.IntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_crontasklogs'


class GlpiCrontasks(models.Model):
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
        managed = False
        db_table = 'glpi_crontasks'
        unique_together = (('itemtype', 'name'),)


class GlpiDashboardsDashboards(models.Model):
    key = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_dashboards_dashboards'


class GlpiDashboardsFilters(models.Model):
    dashboards_dashboards_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    filter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_dashboards_filters'


class GlpiDashboardsItems(models.Model):
    dashboards_dashboards_id = models.PositiveIntegerField()
    gridstack_id = models.CharField(max_length=100)
    card_id = models.CharField(max_length=100)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    card_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_dashboards_items'


class GlpiDashboardsRights(models.Model):
    dashboards_dashboards_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_dashboards_rights'
        unique_together = (('dashboards_dashboards_id', 'itemtype', 'items_id'),)


class GlpiDatabaseinstancecategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_databaseinstancecategories'


class GlpiDatabaseinstances(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    port = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    size = models.IntegerField()
    databaseinstancetypes_id = models.PositiveIntegerField()
    databaseinstancecategories_id = models.PositiveIntegerField()
    locations_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    is_onbackup = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    is_helpdesk_visible = models.IntegerField()
    is_dynamic = models.IntegerField()
    autoupdatesystems_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_lastboot = models.DateTimeField(blank=True, null=True)
    date_lastbackup = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_databaseinstances'


class GlpiDatabaseinstancetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_databaseinstancetypes'


class GlpiDatabases(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    databaseinstances_id = models.PositiveIntegerField()
    is_onbackup = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    date_lastbackup = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_databases'


class GlpiDatacenters(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_datacenters'


class GlpiDcrooms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    vis_cols = models.IntegerField(blank=True, null=True)
    vis_rows = models.IntegerField(blank=True, null=True)
    blueprint = models.TextField(blank=True, null=True)
    datacenters_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_dcrooms'


class GlpiDevicebatteries(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    voltage = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    devicebatterytypes_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicebatterymodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicebatteries'


class GlpiDevicebatterymodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicebatterymodels'


class GlpiDevicebatterytypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicebatterytypes'


class GlpiDevicecameramodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecameramodels'


class GlpiDevicecameras(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    flashunit = models.IntegerField()
    lensfacing = models.CharField(max_length=255, blank=True, null=True)
    orientation = models.CharField(max_length=255, blank=True, null=True)
    focallength = models.CharField(max_length=255, blank=True, null=True)
    sensorsize = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicecameramodels_id = models.PositiveIntegerField(blank=True, null=True)
    support = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecameras'


class GlpiDevicecasemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecasemodels'


class GlpiDevicecases(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicecasetypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicecasemodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecases'


class GlpiDevicecasetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecasetypes'


class GlpiDevicecontrolmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecontrolmodels'


class GlpiDevicecontrols(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    is_raid = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    interfacetypes_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicecontrolmodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecontrols'


class GlpiDevicedrivemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicedrivemodels'


class GlpiDevicedrives(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    is_writer = models.IntegerField()
    speed = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    interfacetypes_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicedrivemodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicedrives'


class GlpiDevicefirmwaremodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicefirmwaremodels'


class GlpiDevicefirmwares(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwaretypes_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicefirmwaremodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicefirmwares'


class GlpiDevicefirmwaretypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicefirmwaretypes'


class GlpiDevicegenericmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegenericmodels'


class GlpiDevicegenerics(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicegenerictypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    devicegenericmodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegenerics'


class GlpiDevicegenerictypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegenerictypes'


class GlpiDevicegraphiccardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegraphiccardmodels'


class GlpiDevicegraphiccards(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    interfacetypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    memory_default = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicegraphiccardmodels_id = models.PositiveIntegerField(blank=True, null=True)
    chipset = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegraphiccards'


class GlpiDeviceharddrivemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceharddrivemodels'


class GlpiDeviceharddrives(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    rpm = models.CharField(max_length=255, blank=True, null=True)
    interfacetypes_id = models.PositiveIntegerField()
    cache = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    capacity_default = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    deviceharddrivemodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceharddrives'


class GlpiDevicememories(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    frequence = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    size_default = models.IntegerField()
    devicememorytypes_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicememorymodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicememories'


class GlpiDevicememorymodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicememorymodels'


class GlpiDevicememorytypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicememorytypes'


class GlpiDevicemotherboardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicemotherboardmodels'


class GlpiDevicemotherboards(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    chipset = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicemotherboardmodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicemotherboards'


class GlpiDevicenetworkcardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicenetworkcardmodels'


class GlpiDevicenetworkcards(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    bandwidth = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    mac_default = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicenetworkcardmodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicenetworkcards'


class GlpiDevicepcimodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepcimodels'


class GlpiDevicepcis(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    devicenetworkcardmodels_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicepcimodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepcis'


class GlpiDevicepowersupplies(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    power = models.CharField(max_length=255, blank=True, null=True)
    is_atx = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicepowersupplymodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepowersupplies'


class GlpiDevicepowersupplymodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepowersupplymodels'


class GlpiDeviceprocessormodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceprocessormodels'


class GlpiDeviceprocessors(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    frequence = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    frequency_default = models.IntegerField()
    nbcores_default = models.IntegerField(blank=True, null=True)
    nbthreads_default = models.IntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    deviceprocessormodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceprocessors'


class GlpiDevicesensormodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesensormodels'


class GlpiDevicesensors(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicesensortypes_id = models.PositiveIntegerField()
    devicesensormodels_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesensors'


class GlpiDevicesensortypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesensortypes'


class GlpiDevicesimcards(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    manufacturers_id = models.PositiveIntegerField()
    voltage = models.IntegerField(blank=True, null=True)
    devicesimcardtypes_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    allow_voip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_devicesimcards'


class GlpiDevicesimcardtypes(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesimcardtypes'


class GlpiDevicesoundcardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesoundcardmodels'


class GlpiDevicesoundcards(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    devicesoundcardmodels_id = models.PositiveIntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesoundcards'


class GlpiDisplaypreferences(models.Model):
    itemtype = models.CharField(max_length=100)
    num = models.IntegerField()
    rank = models.IntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_displaypreferences'
        unique_together = (('users_id', 'itemtype', 'num'),)


class GlpiDocumentcategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    documentcategories_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documentcategories'
        unique_together = (('documentcategories_id', 'name'),)


class GlpiDocuments(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    documentcategories_id = models.PositiveIntegerField()
    mime = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    link = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()
    sha1sum = models.CharField(max_length=40, blank=True, null=True)
    is_blacklisted = models.IntegerField()
    tag = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documents'


class GlpiDocumentsItems(models.Model):
    documents_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    timeline_position = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documents_items'
        unique_together = (('documents_id', 'itemtype', 'items_id', 'timeline_position'),)


class GlpiDocumenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ext = models.CharField(unique=True, max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    mime = models.CharField(max_length=255, blank=True, null=True)
    is_uploadable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documenttypes'


class GlpiDomainrecords(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    data_obj = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    domains_id = models.PositiveIntegerField()
    domainrecordtypes_id = models.PositiveIntegerField()
    ttl = models.IntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domainrecords'


class GlpiDomainrecordtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    fields = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domainrecordtypes'


class GlpiDomainrelations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domainrelations'


class GlpiDomains(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    domaintypes_id = models.PositiveIntegerField()
    date_expiration = models.DateTimeField(blank=True, null=True)
    date_domaincreation = models.DateTimeField(blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domains'


class GlpiDomainsItems(models.Model):
    domains_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    domainrelations_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_domains_items'
        unique_together = (('domains_id', 'itemtype', 'items_id'),)


class GlpiDomaintypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domaintypes'


class GlpiDropdowntranslations(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_dropdowntranslations'
        unique_together = (('itemtype', 'items_id', 'language', 'field'),)


class GlpiEnclosuremodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_enclosuremodels'


class GlpiEnclosures(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    enclosuremodels_id = models.PositiveIntegerField(blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    orientation = models.IntegerField(blank=True, null=True)
    power_supplies = models.IntegerField()
    states_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_enclosures'


class GlpiEntities(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    sons_cache = models.TextField(blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    admin_email = models.CharField(max_length=255, blank=True, null=True)
    admin_email_name = models.CharField(max_length=255, blank=True, null=True)
    from_email = models.CharField(max_length=255, blank=True, null=True)
    from_email_name = models.CharField(max_length=255, blank=True, null=True)
    noreply_email = models.CharField(max_length=255, blank=True, null=True)
    noreply_email_name = models.CharField(max_length=255, blank=True, null=True)
    replyto_email = models.CharField(max_length=255, blank=True, null=True)
    replyto_email_name = models.CharField(max_length=255, blank=True, null=True)
    notification_subject_tag = models.CharField(max_length=255, blank=True, null=True)
    ldap_dn = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    authldaps_id = models.PositiveIntegerField()
    mail_domain = models.CharField(max_length=255, blank=True, null=True)
    entity_ldapfilter = models.TextField(blank=True, null=True)
    mailing_signature = models.TextField(blank=True, null=True)
    cartridges_alert_repeat = models.IntegerField()
    consumables_alert_repeat = models.IntegerField()
    use_licenses_alert = models.IntegerField()
    send_licenses_alert_before_delay = models.IntegerField()
    use_certificates_alert = models.IntegerField()
    send_certificates_alert_before_delay = models.IntegerField()
    certificates_alert_repeat_interval = models.IntegerField()
    use_contracts_alert = models.IntegerField()
    send_contracts_alert_before_delay = models.IntegerField()
    use_infocoms_alert = models.IntegerField()
    send_infocoms_alert_before_delay = models.IntegerField()
    use_reservations_alert = models.IntegerField()
    use_domains_alert = models.IntegerField()
    send_domains_alert_close_expiries_delay = models.IntegerField()
    send_domains_alert_expired_delay = models.IntegerField()
    autoclose_delay = models.IntegerField()
    autopurge_delay = models.IntegerField()
    notclosed_delay = models.IntegerField()
    calendars_strategy = models.IntegerField()
    calendars_id = models.PositiveIntegerField()
    auto_assign_mode = models.IntegerField()
    tickettype = models.IntegerField()
    max_closedate = models.DateTimeField(blank=True, null=True)
    inquest_config = models.IntegerField()
    inquest_rate = models.IntegerField()
    inquest_delay = models.IntegerField()
    inquest_url = models.CharField(db_column='inquest_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    autofill_warranty_date = models.CharField(max_length=255)
    autofill_use_date = models.CharField(max_length=255)
    autofill_buy_date = models.CharField(max_length=255)
    autofill_delivery_date = models.CharField(max_length=255)
    autofill_order_date = models.CharField(max_length=255)
    tickettemplates_strategy = models.IntegerField()
    tickettemplates_id = models.PositiveIntegerField()
    changetemplates_strategy = models.IntegerField()
    changetemplates_id = models.PositiveIntegerField()
    problemtemplates_strategy = models.IntegerField()
    problemtemplates_id = models.PositiveIntegerField()
    entities_strategy_software = models.IntegerField()
    entities_id_software = models.PositiveIntegerField()
    default_contract_alert = models.IntegerField()
    default_infocom_alert = models.IntegerField()
    default_cartridges_alarm_threshold = models.IntegerField()
    default_consumables_alarm_threshold = models.IntegerField()
    delay_send_emails = models.IntegerField()
    is_notif_enable_default = models.IntegerField()
    inquest_duration = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    autofill_decommission_date = models.CharField(max_length=255)
    suppliers_as_private = models.IntegerField()
    anonymize_support_agents = models.IntegerField()
    display_users_initials = models.IntegerField()
    contracts_strategy_default = models.IntegerField()
    contracts_id_default = models.PositiveIntegerField()
    enable_custom_css = models.IntegerField()
    custom_css_code = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    altitude = models.CharField(max_length=255, blank=True, null=True)
    transfers_strategy = models.IntegerField()
    transfers_id = models.PositiveIntegerField()
    agent_base_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_entities'
        unique_together = (('entities_id', 'name'),)


class GlpiEntitiesKnowbaseitems(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_entities_knowbaseitems'


class GlpiEntitiesReminders(models.Model):
    reminders_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_entities_reminders'


class GlpiEntitiesRssfeeds(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_entities_rssfeeds'


class GlpiEvents(models.Model):
    items_id = models.PositiveIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_events'


class GlpiFieldblacklists(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    itemtype = models.CharField(max_length=255)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_fieldblacklists'


class GlpiFieldunicities(models.Model):
    name = models.CharField(max_length=255)
    is_recursive = models.IntegerField()
    itemtype = models.CharField(max_length=255)
    entities_id = models.PositiveIntegerField()
    fields = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    action_refuse = models.IntegerField()
    action_notify = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_fieldunicities'


class GlpiFilesystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_filesystems'


class GlpiFqdns(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdn = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_fqdns'


class GlpiGroups(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    ldap_field = models.CharField(max_length=255, blank=True, null=True)
    ldap_value = models.TextField(blank=True, null=True)
    ldap_group_dn = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    groups_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_requester = models.IntegerField()
    is_watcher = models.IntegerField()
    is_assign = models.IntegerField()
    is_task = models.IntegerField()
    is_notify = models.IntegerField()
    is_itemgroup = models.IntegerField()
    is_usergroup = models.IntegerField()
    is_manager = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_groups'


class GlpiGroupsKnowbaseitems(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_knowbaseitems'


class GlpiGroupsProblems(models.Model):
    problems_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_problems'
        unique_together = (('problems_id', 'type', 'groups_id'),)


class GlpiGroupsReminders(models.Model):
    reminders_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_reminders'


class GlpiGroupsRssfeeds(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_rssfeeds'


class GlpiGroupsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_tickets'
        unique_together = (('tickets_id', 'type', 'groups_id'),)


class GlpiGroupsUsers(models.Model):
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    is_dynamic = models.IntegerField()
    is_manager = models.IntegerField()
    is_userdelegate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_users'
        unique_together = (('users_id', 'groups_id'),)


class GlpiHolidays(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_perpetual = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_holidays'


class GlpiImageformats(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_imageformats'


class GlpiImageresolutions(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    is_video = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_imageresolutions'


class GlpiImpactcompounds(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'glpi_impactcompounds'


class GlpiImpactcontexts(models.Model):
    positions = models.TextField()
    zoom = models.FloatField()
    pan_x = models.FloatField()
    pan_y = models.FloatField()
    impact_color = models.CharField(max_length=255)
    depends_color = models.CharField(max_length=255)
    impact_and_depends_color = models.CharField(max_length=255)
    show_depends = models.IntegerField()
    show_impact = models.IntegerField()
    max_depth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_impactcontexts'


class GlpiImpactitems(models.Model):
    itemtype = models.CharField(max_length=255)
    items_id = models.PositiveIntegerField()
    parent_id = models.PositiveIntegerField()
    impactcontexts_id = models.PositiveIntegerField()
    is_slave = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_impactitems'
        unique_together = (('itemtype', 'items_id'),)


class GlpiImpactrelations(models.Model):
    itemtype_source = models.CharField(max_length=255)
    items_id_source = models.PositiveIntegerField()
    itemtype_impacted = models.CharField(max_length=255)
    items_id_impacted = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_impactrelations'
        unique_together = (('itemtype_source', 'items_id_source', 'itemtype_impacted', 'items_id_impacted'),)


class GlpiInfocoms(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    buy_date = models.DateField(blank=True, null=True)
    use_date = models.DateField(blank=True, null=True)
    warranty_duration = models.IntegerField()
    warranty_info = models.CharField(max_length=255, blank=True, null=True)
    suppliers_id = models.PositiveIntegerField()
    order_number = models.CharField(max_length=255, blank=True, null=True)
    delivery_number = models.CharField(max_length=255, blank=True, null=True)
    immo_number = models.CharField(max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=20, decimal_places=4)
    warranty_value = models.DecimalField(max_digits=20, decimal_places=4)
    sink_time = models.IntegerField()
    sink_type = models.IntegerField()
    sink_coeff = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    bill = models.CharField(max_length=255, blank=True, null=True)
    budgets_id = models.PositiveIntegerField()
    alert = models.IntegerField()
    order_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    inventory_date = models.DateField(blank=True, null=True)
    warranty_date = models.DateField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    decommission_date = models.DateTimeField(blank=True, null=True)
    businesscriticities_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_infocoms'
        unique_together = (('itemtype', 'items_id'),)


class GlpiInterfacetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_interfacetypes'


class GlpiIpaddresses(models.Model):
    entities_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    version = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    binary_0 = models.PositiveIntegerField()
    binary_1 = models.PositiveIntegerField()
    binary_2 = models.PositiveIntegerField()
    binary_3 = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    mainitems_id = models.PositiveIntegerField()
    mainitemtype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ipaddresses'


class GlpiIpaddressesIpnetworks(models.Model):
    ipaddresses_id = models.PositiveIntegerField()
    ipnetworks_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_ipaddresses_ipnetworks'
        unique_together = (('ipaddresses_id', 'ipnetworks_id'),)


class GlpiIpnetworks(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    ipnetworks_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    addressable = models.IntegerField()
    version = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    address_0 = models.PositiveIntegerField()
    address_1 = models.PositiveIntegerField()
    address_2 = models.PositiveIntegerField()
    address_3 = models.PositiveIntegerField()
    netmask = models.CharField(max_length=40, blank=True, null=True)
    netmask_0 = models.PositiveIntegerField()
    netmask_1 = models.PositiveIntegerField()
    netmask_2 = models.PositiveIntegerField()
    netmask_3 = models.PositiveIntegerField()
    gateway = models.CharField(max_length=40, blank=True, null=True)
    gateway_0 = models.PositiveIntegerField()
    gateway_1 = models.PositiveIntegerField()
    gateway_2 = models.PositiveIntegerField()
    gateway_3 = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ipnetworks'


class GlpiIpnetworksVlans(models.Model):
    ipnetworks_id = models.PositiveIntegerField()
    vlans_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_ipnetworks_vlans'
        unique_together = (('ipnetworks_id', 'vlans_id'),)


class GlpiItemsClusters(models.Model):
    clusters_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_clusters'
        unique_together = (('clusters_id', 'itemtype', 'items_id'),)


class GlpiItemsDevicebatteries(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicebatteries_id = models.PositiveIntegerField()
    manufacturing_date = models.DateField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    real_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicebatteries'


class GlpiItemsDevicecameras(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecameras_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicecameras'


class GlpiItemsDevicecamerasImageformats(models.Model):
    item_devicecameras_id = models.PositiveIntegerField()
    imageformats_id = models.PositiveIntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicecameras_imageformats'


class GlpiItemsDevicecamerasImageresolutions(models.Model):
    item_devicecameras_id = models.PositiveIntegerField()
    imageresolutions_id = models.PositiveIntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicecameras_imageresolutions'


class GlpiItemsDevicecases(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecases_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicecases'


class GlpiItemsDevicecontrols(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecontrols_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicecontrols'


class GlpiItemsDevicedrives(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicedrives_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicedrives'


class GlpiItemsDevicefirmwares(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwares_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicefirmwares'


class GlpiItemsDevicegenerics(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegenerics_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicegenerics'


class GlpiItemsDevicegraphiccards(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegraphiccards_id = models.PositiveIntegerField()
    memory = models.IntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicegraphiccards'


class GlpiItemsDeviceharddrives(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceharddrives_id = models.PositiveIntegerField()
    capacity = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_deviceharddrives'


class GlpiItemsDevicememories(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicememories_id = models.PositiveIntegerField()
    size = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicememories'


class GlpiItemsDevicemotherboards(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicemotherboards_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicemotherboards'


class GlpiItemsDevicenetworkcards(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicenetworkcards_id = models.PositiveIntegerField()
    mac = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicenetworkcards'


class GlpiItemsDevicepcis(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepcis_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicepcis'


class GlpiItemsDevicepowersupplies(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepowersupplies_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicepowersupplies'


class GlpiItemsDeviceprocessors(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceprocessors_id = models.PositiveIntegerField()
    frequency = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    nbcores = models.IntegerField(blank=True, null=True)
    nbthreads = models.IntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_deviceprocessors'


class GlpiItemsDevicesensors(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesensors_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicesensors'


class GlpiItemsDevicesimcards(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    devicesimcards_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    states_id = models.PositiveIntegerField()
    locations_id = models.PositiveIntegerField()
    lines_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    pin = models.CharField(max_length=255)
    pin2 = models.CharField(max_length=255)
    puk = models.CharField(max_length=255)
    puk2 = models.CharField(max_length=255)
    msin = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicesimcards'


class GlpiItemsDevicesoundcards(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesoundcards_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_devicesoundcards'


class GlpiItemsDisks(models.Model):
    entities_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    mountpoint = models.CharField(max_length=255, blank=True, null=True)
    filesystems_id = models.PositiveIntegerField()
    totalsize = models.IntegerField()
    freesize = models.IntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    encryption_status = models.IntegerField()
    encryption_tool = models.CharField(max_length=255, blank=True, null=True)
    encryption_algorithm = models.CharField(max_length=255, blank=True, null=True)
    encryption_type = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_items_disks'


class GlpiItemsEnclosures(models.Model):
    enclosures_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255)
    items_id = models.PositiveIntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_enclosures'
        unique_together = (('itemtype', 'items_id'),)


class GlpiItemsKanbans(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    state = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_items_kanbans'
        unique_together = (('itemtype', 'items_id', 'users_id'),)


class GlpiItemsOperatingsystems(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    operatingsystems_id = models.PositiveIntegerField()
    operatingsystemversions_id = models.PositiveIntegerField()
    operatingsystemservicepacks_id = models.PositiveIntegerField()
    operatingsystemarchitectures_id = models.PositiveIntegerField()
    operatingsystemkernelversions_id = models.PositiveIntegerField()
    license_number = models.CharField(max_length=255, blank=True, null=True)
    licenseid = models.CharField(max_length=255, blank=True, null=True)
    operatingsystemeditions_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_operatingsystems'
        unique_together = (('items_id', 'itemtype', 'operatingsystems_id', 'operatingsystemarchitectures_id'),)


class GlpiItemsProblems(models.Model):
    problems_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_problems'
        unique_together = (('problems_id', 'itemtype', 'items_id'),)


class GlpiItemsProjects(models.Model):
    projects_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_projects'
        unique_together = (('projects_id', 'itemtype', 'items_id'),)


class GlpiItemsRacks(models.Model):
    racks_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255)
    items_id = models.PositiveIntegerField()
    position = models.IntegerField()
    orientation = models.IntegerField(blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    hpos = models.IntegerField()
    is_reserved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_racks'
        unique_together = (('itemtype', 'items_id', 'is_reserved'),)


class GlpiItemsRemotemanagements(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    remoteid = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_remotemanagements'


class GlpiItemsSoftwarelicenses(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    softwarelicenses_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_softwarelicenses'


class GlpiItemsSoftwareversions(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    softwareversions_id = models.PositiveIntegerField()
    is_deleted_item = models.IntegerField()
    is_template_item = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_install = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_items_softwareversions'
        unique_together = (('itemtype', 'items_id', 'softwareversions_id'),)


class GlpiItemsTickets(models.Model):
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_tickets'
        unique_together = (('itemtype', 'items_id', 'tickets_id'),)


class GlpiItilcategories(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    itilcategories_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    knowbaseitemcategories_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_helpdeskvisible = models.IntegerField()
    tickettemplates_id_incident = models.PositiveIntegerField()
    tickettemplates_id_demand = models.PositiveIntegerField()
    changetemplates_id = models.PositiveIntegerField()
    problemtemplates_id = models.PositiveIntegerField()
    is_incident = models.IntegerField()
    is_request = models.IntegerField()
    is_problem = models.IntegerField()
    is_change = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_itilcategories'


class GlpiItilfollowups(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    users_id_editor = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)
    is_private = models.IntegerField()
    requesttypes_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    timeline_position = models.IntegerField()
    sourceitems_id = models.PositiveIntegerField()
    sourceof_items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_itilfollowups'


class GlpiItilfollowuptemplates(models.Model):
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    requesttypes_id = models.PositiveIntegerField()
    is_private = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_itilfollowuptemplates'


class GlpiItilsProjects(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    projects_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_itils_projects'
        unique_together = (('itemtype', 'items_id', 'projects_id'),)


class GlpiItilsolutions(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    solutiontypes_id = models.PositiveIntegerField()
    solutiontype_name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_approval = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    user_name = models.CharField(max_length=255, blank=True, null=True)
    users_id_editor = models.PositiveIntegerField()
    users_id_approval = models.PositiveIntegerField()
    user_name_approval = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    itilfollowups_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_itilsolutions'


class GlpiKnowbaseitemcategories(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    knowbaseitemcategories_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    sons_cache = models.TextField(blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitemcategories'
        unique_together = (('entities_id', 'knowbaseitemcategories_id', 'name'),)


class GlpiKnowbaseitems(models.Model):
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    is_faq = models.IntegerField()
    users_id = models.PositiveIntegerField()
    view = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems'


class GlpiKnowbaseitemsComments(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    parent_comment_id = models.PositiveIntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_comments'


class GlpiKnowbaseitemsItems(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_items'
        unique_together = (('itemtype', 'items_id', 'knowbaseitems_id'),)


class GlpiKnowbaseitemsKnowbaseitemcategories(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    knowbaseitemcategories_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_knowbaseitemcategories'


class GlpiKnowbaseitemsProfiles(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_profiles'


class GlpiKnowbaseitemsRevisions(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    revision = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_revisions'
        unique_together = (('knowbaseitems_id', 'revision', 'language'),)


class GlpiKnowbaseitemsUsers(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_users'


class GlpiKnowbaseitemtranslations(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitemtranslations'


class GlpiLineoperators(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    mcc = models.IntegerField(blank=True, null=True)
    mnc = models.IntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_lineoperators'
        unique_together = (('mcc', 'mnc'),)


class GlpiLines(models.Model):
    name = models.CharField(max_length=255)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    caller_num = models.CharField(max_length=255)
    caller_name = models.CharField(max_length=255)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    lineoperators_id = models.PositiveIntegerField()
    locations_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    linetypes_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_lines'


class GlpiLinetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_linetypes'


class GlpiLinks(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    open_window = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_links'


class GlpiLinksItemtypes(models.Model):
    links_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_links_itemtypes'
        unique_together = (('itemtype', 'links_id'),)


class GlpiLocations(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    altitude = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_locations'
        unique_together = (('entities_id', 'locations_id', 'name'),)


class GlpiLockedfields(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    field = models.CharField(max_length=50)
    value = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_global = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_lockedfields'
        unique_together = (('itemtype', 'items_id', 'field'),)


class GlpiLogs(models.Model):
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
        managed = False
        db_table = 'glpi_logs'


class GlpiMailcollectors(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    filesize_max = models.IntegerField()
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    passwd = models.CharField(max_length=255, blank=True, null=True)
    accepted = models.CharField(max_length=255, blank=True, null=True)
    refused = models.CharField(max_length=255, blank=True, null=True)
    errors = models.IntegerField()
    use_mail_date = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    requester_field = models.IntegerField()
    add_cc_to_observer = models.IntegerField()
    collect_only_unread = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_mailcollectors'


class GlpiManuallinks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=8096)
    open_window = models.IntegerField()
    icon = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_manuallinks'


class GlpiManufacturers(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_manufacturers'


class GlpiMonitormodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_monitormodels'


class GlpiMonitors(models.Model):
    entities_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    have_micro = models.IntegerField()
    have_speaker = models.IntegerField()
    have_subd = models.IntegerField()
    have_bnc = models.IntegerField()
    have_dvi = models.IntegerField()
    have_pivot = models.IntegerField()
    have_hdmi = models.IntegerField()
    have_displayport = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    monitortypes_id = models.PositiveIntegerField()
    monitormodels_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    autoupdatesystems_id = models.PositiveIntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_monitors'


class GlpiMonitortypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_monitortypes'


class GlpiNetworkaliases(models.Model):
    entities_id = models.PositiveIntegerField()
    networknames_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdns_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkaliases'


class GlpiNetworkequipmentmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkequipmentmodels'


class GlpiNetworkequipments(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    networks_id = models.PositiveIntegerField()
    networkequipmenttypes_id = models.PositiveIntegerField()
    networkequipmentmodels_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    autoupdatesystems_id = models.PositiveIntegerField()
    sysdescr = models.TextField(blank=True, null=True)
    cpu = models.IntegerField()
    uptime = models.CharField(max_length=255)
    last_inventory_update = models.DateTimeField(blank=True, null=True)
    snmpcredentials_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_networkequipments'


class GlpiNetworkequipmenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkequipmenttypes'


class GlpiNetworkinterfaces(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkinterfaces'


class GlpiNetworknames(models.Model):
    entities_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    fqdns_id = models.PositiveIntegerField()
    ipnetworks_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networknames'


class GlpiNetworkportaggregates(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    networkports_id_list = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportaggregates'


class GlpiNetworkportaliases(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    networkports_id_alias = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportaliases'


class GlpiNetworkportconnectionlogs(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    connected = models.IntegerField()
    networkports_id_source = models.PositiveIntegerField()
    networkports_id_destination = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_networkportconnectionlogs'


class GlpiNetworkportdialups(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportdialups'


class GlpiNetworkportethernets(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    items_devicenetworkcards_id = models.PositiveIntegerField()
    type = models.CharField(max_length=10, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportethernets'


class GlpiNetworkportfiberchannels(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    items_devicenetworkcards_id = models.PositiveIntegerField()
    networkportfiberchanneltypes_id = models.PositiveIntegerField()
    wwn = models.CharField(max_length=16, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportfiberchannels'


class GlpiNetworkportfiberchanneltypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportfiberchanneltypes'


class GlpiNetworkportlocals(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportlocals'


class GlpiNetworkportmetrics(models.Model):
    date = models.DateField(blank=True, null=True)
    ifinbytes = models.BigIntegerField()
    ifinerrors = models.BigIntegerField()
    ifoutbytes = models.BigIntegerField()
    ifouterrors = models.BigIntegerField()
    networkports_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportmetrics'
        unique_together = (('networkports_id', 'date'),)


class GlpiNetworkports(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    logical_number = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    instantiation_type = models.CharField(max_length=255, blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    ifmtu = models.IntegerField()
    ifspeed = models.BigIntegerField()
    ifinternalstatus = models.CharField(max_length=255, blank=True, null=True)
    ifconnectionstatus = models.IntegerField()
    iflastchange = models.CharField(max_length=255, blank=True, null=True)
    ifinbytes = models.BigIntegerField()
    ifinerrors = models.BigIntegerField()
    ifoutbytes = models.BigIntegerField()
    ifouterrors = models.BigIntegerField()
    ifstatus = models.CharField(max_length=255, blank=True, null=True)
    ifdescr = models.CharField(max_length=255, blank=True, null=True)
    ifalias = models.CharField(max_length=255, blank=True, null=True)
    portduplex = models.CharField(max_length=255, blank=True, null=True)
    trunk = models.IntegerField()
    lastup = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkports'


class GlpiNetworkportsNetworkports(models.Model):
    networkports_id_1 = models.PositiveIntegerField()
    networkports_id_2 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_networkports_networkports'
        unique_together = (('networkports_id_1', 'networkports_id_2'),)


class GlpiNetworkportsVlans(models.Model):
    networkports_id = models.PositiveIntegerField()
    vlans_id = models.PositiveIntegerField()
    tagged = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_networkports_vlans'
        unique_together = (('networkports_id', 'vlans_id'),)


class GlpiNetworkporttypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    value_decimal = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_importable = models.IntegerField()
    instantiation_type = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkporttypes'


class GlpiNetworkportwifis(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    items_devicenetworkcards_id = models.PositiveIntegerField()
    wifinetworks_id = models.PositiveIntegerField()
    networkportwifis_id = models.PositiveIntegerField()
    version = models.CharField(max_length=20, blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportwifis'


class GlpiNetworks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networks'


class GlpiNotepads(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    users_id_lastupdater = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_notepads'


class GlpiNotifications(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    event = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    allow_response = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_notifications'


class GlpiNotificationsNotificationtemplates(models.Model):
    notifications_id = models.PositiveIntegerField()
    mode = models.CharField(max_length=20)
    notificationtemplates_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_notifications_notificationtemplates'
        unique_together = (('notifications_id', 'mode', 'notificationtemplates_id'),)


class GlpiNotificationtargets(models.Model):
    items_id = models.PositiveIntegerField()
    type = models.IntegerField()
    notifications_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_notificationtargets'


class GlpiNotificationtemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_notificationtemplates'


class GlpiNotificationtemplatetranslations(models.Model):
    notificationtemplates_id = models.PositiveIntegerField()
    language = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    content_text = models.TextField(blank=True, null=True)
    content_html = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_notificationtemplatetranslations'


class GlpiNotimportedemails(models.Model):
    from_field = models.CharField(db_column='from', max_length=255)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=255)
    mailcollectors_id = models.PositiveIntegerField()
    date = models.DateTimeField()
    subject = models.TextField(blank=True, null=True)
    messageid = models.CharField(max_length=255)
    reason = models.IntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_notimportedemails'


class GlpiObjectlocks(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'glpi_objectlocks'
        unique_together = (('itemtype', 'items_id'),)


class GlpiOlalevelactions(models.Model):
    olalevels_id = models.PositiveIntegerField()
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevelactions'


class GlpiOlalevelcriterias(models.Model):
    olalevels_id = models.PositiveIntegerField()
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevelcriterias'


class GlpiOlalevels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    olas_id = models.PositiveIntegerField()
    execution_time = models.IntegerField()
    is_active = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    match = models.CharField(max_length=10, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevels'


class GlpiOlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    olalevels_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevels_tickets'
        unique_together = (('tickets_id', 'olalevels_id'),)


class GlpiOlas(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    type = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    number_time = models.IntegerField()
    use_ticket_calendar = models.IntegerField()
    calendars_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    definition_time = models.CharField(max_length=255, blank=True, null=True)
    end_of_working_day = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    slms_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_olas'


class GlpiOperatingsystemarchitectures(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemarchitectures'


class GlpiOperatingsystemeditions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemeditions'


class GlpiOperatingsystemkernels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemkernels'


class GlpiOperatingsystemkernelversions(models.Model):
    operatingsystemkernels_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemkernelversions'


class GlpiOperatingsystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystems'


class GlpiOperatingsystemservicepacks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemservicepacks'


class GlpiOperatingsystemversions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemversions'


class GlpiPassivedcequipmentmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_passivedcequipmentmodels'


class GlpiPassivedcequipments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    passivedcequipmentmodels_id = models.PositiveIntegerField(blank=True, null=True)
    passivedcequipmenttypes_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    states_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_passivedcequipments'


class GlpiPassivedcequipmenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_passivedcequipmenttypes'


class GlpiPcivendors(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    vendorid = models.CharField(max_length=4)
    deviceid = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pcivendors'
        unique_together = (('vendorid', 'deviceid'),)


class GlpiPdumodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    max_power = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    is_rackable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdumodels'


class GlpiPdus(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    pdumodels_id = models.PositiveIntegerField(blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    states_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    pdutypes_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdus'


class GlpiPdusPlugs(models.Model):
    plugs_id = models.PositiveIntegerField()
    pdus_id = models.PositiveIntegerField()
    number_plugs = models.IntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdus_plugs'


class GlpiPdusRacks(models.Model):
    racks_id = models.PositiveIntegerField()
    pdus_id = models.PositiveIntegerField()
    side = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdus_racks'


class GlpiPdutypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdutypes'


class GlpiPendingreasons(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    followup_frequency = models.IntegerField()
    followups_before_resolution = models.IntegerField()
    itilfollowuptemplates_id = models.PositiveIntegerField()
    solutiontemplates_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pendingreasons'


class GlpiPendingreasonsItems(models.Model):
    pendingreasons_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    followup_frequency = models.IntegerField()
    followups_before_resolution = models.IntegerField()
    bump_count = models.IntegerField()
    last_bump_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pendingreasons_items'
        unique_together = (('items_id', 'itemtype'),)


class GlpiPeripheralmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_peripheralmodels'


class GlpiPeripherals(models.Model):
    entities_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    peripheraltypes_id = models.PositiveIntegerField()
    peripheralmodels_id = models.PositiveIntegerField()
    brand = models.CharField(max_length=255, blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    autoupdatesystems_id = models.PositiveIntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_peripherals'


class GlpiPeripheraltypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_peripheraltypes'


class GlpiPhonemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_phonemodels'


class GlpiPhonepowersupplies(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_phonepowersupplies'


class GlpiPhones(models.Model):
    entities_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    phonetypes_id = models.PositiveIntegerField()
    phonemodels_id = models.PositiveIntegerField()
    brand = models.CharField(max_length=255, blank=True, null=True)
    phonepowersupplies_id = models.PositiveIntegerField()
    number_line = models.CharField(max_length=255, blank=True, null=True)
    have_headset = models.IntegerField()
    have_hp = models.IntegerField()
    manufacturers_id = models.PositiveIntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    autoupdatesystems_id = models.PositiveIntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()
    last_inventory_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_phones'


class GlpiPhonetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_phonetypes'


class GlpiPlanningeventcategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_planningeventcategories'


class GlpiPlanningexternalevents(models.Model):
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
        managed = False
        db_table = 'glpi_planningexternalevents'


class GlpiPlanningexternaleventtemplates(models.Model):
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
        managed = False
        db_table = 'glpi_planningexternaleventtemplates'


class GlpiPlanningrecalls(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    users_id = models.PositiveIntegerField()
    before_time = models.IntegerField()
    when = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_planningrecalls'
        unique_together = (('itemtype', 'items_id', 'users_id'),)


class GlpiPlugins(models.Model):
    directory = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    state = models.IntegerField()
    author = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugins'


class GlpiPlugs(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugs'


class GlpiPrinterlogs(models.Model):
    printers_id = models.PositiveIntegerField()
    total_pages = models.IntegerField()
    bw_pages = models.IntegerField()
    color_pages = models.IntegerField()
    rv_pages = models.IntegerField()
    prints = models.IntegerField()
    bw_prints = models.IntegerField()
    color_prints = models.IntegerField()
    copies = models.IntegerField()
    bw_copies = models.IntegerField()
    color_copies = models.IntegerField()
    scanned = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    faxed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_printerlogs'
        unique_together = (('printers_id', 'date'),)


class GlpiPrintermodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_printermodels'


class GlpiPrinters(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    have_serial = models.IntegerField()
    have_parallel = models.IntegerField()
    have_usb = models.IntegerField()
    have_wifi = models.IntegerField()
    have_ethernet = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    memory_size = models.CharField(max_length=255, blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    networks_id = models.PositiveIntegerField()
    printertypes_id = models.PositiveIntegerField()
    printermodels_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    init_pages_counter = models.IntegerField()
    last_pages_counter = models.IntegerField()
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    sysdescr = models.TextField(blank=True, null=True)
    last_inventory_update = models.DateTimeField(blank=True, null=True)
    snmpcredentials_id = models.PositiveIntegerField()
    autoupdatesystems_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_printers'


class GlpiPrintersCartridgeinfos(models.Model):
    printers_id = models.PositiveIntegerField()
    property = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_printers_cartridgeinfos'


class GlpiPrintertypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_printertypes'


class GlpiProblemcosts(models.Model):
    problems_id = models.PositiveIntegerField()
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
        managed = False
        db_table = 'glpi_problemcosts'


class GlpiProblems(models.Model):
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
        managed = False
        db_table = 'glpi_problems'


class GlpiProblemsSuppliers(models.Model):
    problems_id = models.PositiveIntegerField()
    suppliers_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problems_suppliers'
        unique_together = (('problems_id', 'type', 'suppliers_id'),)


class GlpiProblemsTickets(models.Model):
    problems_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_problems_tickets'
        unique_together = (('problems_id', 'tickets_id'),)


class GlpiProblemsUsers(models.Model):
    problems_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problems_users'
        unique_together = (('problems_id', 'type', 'users_id', 'alternative_email'),)


class GlpiProblemtasks(models.Model):
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    problems_id = models.PositiveIntegerField()
    taskcategories_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    users_id_editor = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)
    actiontime = models.IntegerField()
    state = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tasktemplates_id = models.PositiveIntegerField()
    timeline_position = models.IntegerField()
    is_private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_problemtasks'


class GlpiProblemtemplatehiddenfields(models.Model):
    problemtemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplatehiddenfields'
        unique_together = (('problemtemplates_id', 'num'),)


class GlpiProblemtemplatemandatoryfields(models.Model):
    problemtemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplatemandatoryfields'
        unique_together = (('problemtemplates_id', 'num'),)


class GlpiProblemtemplatepredefinedfields(models.Model):
    problemtemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplatepredefinedfields'


class GlpiProblemtemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplates'


class GlpiProfilerights(models.Model):
    profiles_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    rights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profilerights'
        unique_together = (('profiles_id', 'name'),)


class GlpiProfiles(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    interface = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField()
    helpdesk_hardware = models.IntegerField()
    helpdesk_item_type = models.TextField(blank=True, null=True)
    ticket_status = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    problem_status = models.TextField(blank=True, null=True)
    create_ticket_on_login = models.IntegerField()
    tickettemplates_id = models.PositiveIntegerField()
    changetemplates_id = models.PositiveIntegerField()
    problemtemplates_id = models.PositiveIntegerField()
    change_status = models.TextField(blank=True, null=True)
    managed_domainrecordtypes = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_profiles'


class GlpiProfilesReminders(models.Model):
    reminders_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profiles_reminders'


class GlpiProfilesRssfeeds(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profiles_rssfeeds'


class GlpiProfilesUsers(models.Model):
    users_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    is_dynamic = models.IntegerField()
    is_default_profile = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profiles_users'


class GlpiProjectcosts(models.Model):
    projects_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    budgets_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_projectcosts'


class GlpiProjects(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    projects_id = models.PositiveIntegerField()
    projectstates_id = models.PositiveIntegerField()
    projecttypes_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    plan_start_date = models.DateTimeField(blank=True, null=True)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    real_start_date = models.DateTimeField(blank=True, null=True)
    real_end_date = models.DateTimeField(blank=True, null=True)
    percent_done = models.IntegerField()
    auto_percent_done = models.IntegerField()
    show_on_global_gantt = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    projecttemplates_id = models.PositiveIntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projects'


class GlpiProjectstates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    is_finished = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projectstates'


class GlpiProjecttasklinks(models.Model):
    projecttasks_id_source = models.PositiveIntegerField()
    source_uuid = models.CharField(max_length=255)
    projecttasks_id_target = models.PositiveIntegerField()
    target_uuid = models.CharField(max_length=255)
    type = models.IntegerField()
    lag = models.SmallIntegerField(blank=True, null=True)
    lead = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasklinks'


class GlpiProjecttasks(models.Model):
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    projects_id = models.PositiveIntegerField()
    projecttasks_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    plan_start_date = models.DateTimeField(blank=True, null=True)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    real_start_date = models.DateTimeField(blank=True, null=True)
    real_end_date = models.DateTimeField(blank=True, null=True)
    planned_duration = models.IntegerField()
    effective_duration = models.IntegerField()
    projectstates_id = models.PositiveIntegerField()
    projecttasktypes_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    percent_done = models.IntegerField()
    auto_percent_done = models.IntegerField()
    is_milestone = models.IntegerField()
    projecttasktemplates_id = models.PositiveIntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasks'


class GlpiProjecttasksTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    projecttasks_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_projecttasks_tickets'
        unique_together = (('tickets_id', 'projecttasks_id'),)


class GlpiProjecttaskteams(models.Model):
    projecttasks_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_projecttaskteams'
        unique_together = (('projecttasks_id', 'itemtype', 'items_id'),)


class GlpiProjecttasktemplates(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    projects_id = models.PositiveIntegerField()
    projecttasks_id = models.PositiveIntegerField()
    plan_start_date = models.DateTimeField(blank=True, null=True)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    real_start_date = models.DateTimeField(blank=True, null=True)
    real_end_date = models.DateTimeField(blank=True, null=True)
    planned_duration = models.IntegerField()
    effective_duration = models.IntegerField()
    projectstates_id = models.PositiveIntegerField()
    projecttasktypes_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    percent_done = models.IntegerField()
    is_milestone = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasktemplates'


class GlpiProjecttasktypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasktypes'


class GlpiProjectteams(models.Model):
    projects_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_projectteams'
        unique_together = (('projects_id', 'itemtype', 'items_id'),)


class GlpiProjecttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttypes'


class GlpiQueuednotifications(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    notificationtemplates_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    sent_try = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    sender = models.TextField(blank=True, null=True)
    sendername = models.TextField(blank=True, null=True)
    recipient = models.TextField(blank=True, null=True)
    recipientname = models.TextField(blank=True, null=True)
    replyto = models.TextField(blank=True, null=True)
    replytoname = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    body_text = models.TextField(blank=True, null=True)
    messageid = models.TextField(blank=True, null=True)
    documents = models.TextField(blank=True, null=True)
    mode = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'glpi_queuednotifications'


class GlpiRackmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rackmodels'


class GlpiRacks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    rackmodels_id = models.PositiveIntegerField(blank=True, null=True)
    manufacturers_id = models.PositiveIntegerField()
    racktypes_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    number_units = models.IntegerField(blank=True, null=True)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    dcrooms_id = models.PositiveIntegerField()
    room_orientation = models.IntegerField()
    position = models.CharField(max_length=50, blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    max_power = models.IntegerField()
    mesured_power = models.IntegerField()
    max_weight = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_racks'


class GlpiRacktypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_racktypes'


class GlpiRecurrentchanges(models.Model):
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
        managed = False
        db_table = 'glpi_recurrentchanges'


class GlpiRefusedequipments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    rules_id = models.PositiveIntegerField()
    method = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    agents_id = models.PositiveIntegerField()
    autoupdatesystems_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_refusedequipments'


class GlpiRegisteredids(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_registeredids'


class GlpiReminders(models.Model):
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    is_planned = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    begin_view_date = models.DateTimeField(blank=True, null=True)
    end_view_date = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_reminders'


class GlpiRemindersUsers(models.Model):
    reminders_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_reminders_users'


class GlpiRemindertranslations(models.Model):
    reminders_id = models.PositiveIntegerField()
    language = models.CharField(max_length=5, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_remindertranslations'


class GlpiRequesttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_helpdesk_default = models.IntegerField()
    is_followup_default = models.IntegerField()
    is_mail_default = models.IntegerField()
    is_mailfollowup_default = models.IntegerField()
    is_active = models.IntegerField()
    is_ticketheader = models.IntegerField()
    is_itilfollowup = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_requesttypes'


class GlpiReservationitems(models.Model):
    itemtype = models.CharField(max_length=100)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    items_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_reservationitems'
        unique_together = (('itemtype', 'items_id'),)


class GlpiReservations(models.Model):
    reservationitems_id = models.PositiveIntegerField()
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_reservations'


class GlpiRssfeeds(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    refresh_rate = models.IntegerField()
    max_items = models.IntegerField()
    have_error = models.IntegerField()
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rssfeeds'


class GlpiRssfeedsUsers(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_rssfeeds_users'


class GlpiRuleactions(models.Model):
    rules_id = models.PositiveIntegerField()
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ruleactions'


class GlpiRulecriterias(models.Model):
    rules_id = models.PositiveIntegerField()
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rulecriterias'


class GlpiRulematchedlogs(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    rules_id = models.PositiveIntegerField(blank=True, null=True)
    agents_id = models.PositiveIntegerField()
    method = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rulematchedlogs'


class GlpiRulerightparameters(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rulerightparameters'


class GlpiRules(models.Model):
    entities_id = models.PositiveIntegerField()
    sub_type = models.CharField(max_length=255)
    ranking = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    match = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rules'


class GlpiSavedsearches(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    users_id = models.PositiveIntegerField()
    is_private = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    query = models.TextField(blank=True, null=True)
    last_execution_time = models.IntegerField(blank=True, null=True)
    do_count = models.IntegerField()
    last_execution_date = models.DateTimeField(blank=True, null=True)
    counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_savedsearches'


class GlpiSavedsearchesAlerts(models.Model):
    savedsearches_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    operator = models.IntegerField()
    value = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    frequency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_savedsearches_alerts'
        unique_together = (('savedsearches_id', 'operator', 'value'),)


class GlpiSavedsearchesUsers(models.Model):
    users_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    savedsearches_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_savedsearches_users'
        unique_together = (('users_id', 'itemtype'),)


class GlpiSlalevelactions(models.Model):
    slalevels_id = models.PositiveIntegerField()
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevelactions'


class GlpiSlalevelcriterias(models.Model):
    slalevels_id = models.PositiveIntegerField()
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevelcriterias'


class GlpiSlalevels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slas_id = models.PositiveIntegerField()
    execution_time = models.IntegerField()
    is_active = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    match = models.CharField(max_length=10, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevels'


class GlpiSlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    slalevels_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevels_tickets'
        unique_together = (('tickets_id', 'slalevels_id'),)


class GlpiSlas(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    type = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    number_time = models.IntegerField()
    use_ticket_calendar = models.IntegerField()
    calendars_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    definition_time = models.CharField(max_length=255, blank=True, null=True)
    end_of_working_day = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    slms_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_slas'


class GlpiSlms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    use_ticket_calendar = models.IntegerField()
    calendars_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slms'


class GlpiSnmpcredentials(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    snmpversion = models.CharField(max_length=8)
    community = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    authentication = models.CharField(max_length=255, blank=True, null=True)
    auth_passphrase = models.CharField(max_length=255, blank=True, null=True)
    encryption = models.CharField(max_length=255, blank=True, null=True)
    priv_passphrase = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_snmpcredentials'


class GlpiSocketmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_socketmodels'


class GlpiSockets(models.Model):
    position = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    socketmodels_id = models.PositiveIntegerField()
    wiring_side = models.IntegerField(blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    networkports_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_sockets'


class GlpiSoftwarecategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    softwarecategories_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwarecategories'


class GlpiSoftwarelicenses(models.Model):
    softwares_id = models.PositiveIntegerField()
    softwarelicenses_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    number = models.IntegerField()
    softwarelicensetypes_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    softwareversions_id_buy = models.PositiveIntegerField()
    softwareversions_id_use = models.PositiveIntegerField()
    expire = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_valid = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    is_helpdesk_visible = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    states_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    allow_overquota = models.IntegerField()
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwarelicenses'


class GlpiSoftwarelicensetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    softwarelicensetypes_id = models.PositiveIntegerField()
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    completename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwarelicensetypes'


class GlpiSoftwares(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()
    is_update = models.IntegerField()
    softwares_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_helpdesk_visible = models.IntegerField()
    softwarecategories_id = models.PositiveIntegerField()
    is_valid = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwares'


class GlpiSoftwareversions(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    softwares_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    arch = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    operatingsystems_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwareversions'


class GlpiSolutiontemplates(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    solutiontypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_solutiontemplates'


class GlpiSolutiontypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_solutiontypes'


class GlpiSsovariables(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ssovariables'


class GlpiStates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    states_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_visible_computer = models.IntegerField()
    is_visible_monitor = models.IntegerField()
    is_visible_networkequipment = models.IntegerField()
    is_visible_peripheral = models.IntegerField()
    is_visible_phone = models.IntegerField()
    is_visible_printer = models.IntegerField()
    is_visible_softwareversion = models.IntegerField()
    is_visible_softwarelicense = models.IntegerField()
    is_visible_line = models.IntegerField()
    is_visible_certificate = models.IntegerField()
    is_visible_rack = models.IntegerField()
    is_visible_passivedcequipment = models.IntegerField()
    is_visible_enclosure = models.IntegerField()
    is_visible_pdu = models.IntegerField()
    is_visible_cluster = models.IntegerField()
    is_visible_contract = models.IntegerField()
    is_visible_appliance = models.IntegerField()
    is_visible_databaseinstance = models.IntegerField()
    is_visible_cable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_states'
        unique_together = (('states_id', 'name'),)


class GlpiSuppliers(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    suppliertypes_id = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_suppliers'


class GlpiSuppliersTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    suppliers_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_suppliers_tickets'
        unique_together = (('tickets_id', 'type', 'suppliers_id'),)


class GlpiSuppliertypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_suppliertypes'


class GlpiTaskcategories(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    taskcategories_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    is_helpdeskvisible = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    knowbaseitemcategories_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_taskcategories'


class GlpiTasktemplates(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    taskcategories_id = models.PositiveIntegerField()
    actiontime = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    is_private = models.IntegerField()
    users_id_tech = models.PositiveIntegerField()
    groups_id_tech = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tasktemplates'


class GlpiTicketcosts(models.Model):
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
        managed = False
        db_table = 'glpi_ticketcosts'


class GlpiTicketrecurrents(models.Model):
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
        managed = False
        db_table = 'glpi_ticketrecurrents'


class GlpiTickets(models.Model):
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
        managed = False
        db_table = 'glpi_tickets'


class GlpiTicketsContracts(models.Model):
    tickets_id = models.PositiveIntegerField()
    contracts_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickets_contracts'
        unique_together = (('tickets_id', 'contracts_id'),)


class GlpiTicketsTickets(models.Model):
    tickets_id_1 = models.PositiveIntegerField()
    tickets_id_2 = models.PositiveIntegerField()
    link = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickets_tickets'
        unique_together = (('tickets_id_1', 'tickets_id_2'),)


class GlpiTicketsUsers(models.Model):
    tickets_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_tickets_users'
        unique_together = (('tickets_id', 'type', 'users_id', 'alternative_email'),)


class GlpiTicketsatisfactions(models.Model):
    tickets_id = models.PositiveIntegerField(unique=True)
    type = models.IntegerField()
    date_begin = models.DateTimeField(blank=True, null=True)
    date_answered = models.DateTimeField(blank=True, null=True)
    satisfaction = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ticketsatisfactions'


class GlpiTickettasks(models.Model):
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
        managed = False
        db_table = 'glpi_tickettasks'


class GlpiTickettemplatehiddenfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplatehiddenfields'
        unique_together = (('tickettemplates_id', 'num'),)


class GlpiTickettemplatemandatoryfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplatemandatoryfields'
        unique_together = (('tickettemplates_id', 'num'),)


class GlpiTickettemplatepredefinedfields(models.Model):
    tickettemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplatepredefinedfields'


class GlpiTickettemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplates'


class GlpiTicketvalidations(models.Model):
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
        managed = False
        db_table = 'glpi_ticketvalidations'


class GlpiTransfers(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    keep_ticket = models.IntegerField()
    keep_networklink = models.IntegerField()
    keep_reservation = models.IntegerField()
    keep_history = models.IntegerField()
    keep_device = models.IntegerField()
    keep_infocom = models.IntegerField()
    keep_dc_monitor = models.IntegerField()
    clean_dc_monitor = models.IntegerField()
    keep_dc_phone = models.IntegerField()
    clean_dc_phone = models.IntegerField()
    keep_dc_peripheral = models.IntegerField()
    clean_dc_peripheral = models.IntegerField()
    keep_dc_printer = models.IntegerField()
    clean_dc_printer = models.IntegerField()
    keep_supplier = models.IntegerField()
    clean_supplier = models.IntegerField()
    keep_contact = models.IntegerField()
    clean_contact = models.IntegerField()
    keep_contract = models.IntegerField()
    clean_contract = models.IntegerField()
    keep_software = models.IntegerField()
    clean_software = models.IntegerField()
    keep_document = models.IntegerField()
    clean_document = models.IntegerField()
    keep_cartridgeitem = models.IntegerField()
    clean_cartridgeitem = models.IntegerField()
    keep_cartridge = models.IntegerField()
    keep_consumable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    keep_disk = models.IntegerField()
    keep_certificate = models.IntegerField()
    clean_certificate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_transfers'


class GlpiUnmanageds(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations_id = models.PositiveIntegerField()
    networks_id = models.PositiveIntegerField()
    manufacturers_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    states_id = models.PositiveIntegerField()
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    autoupdatesystems_id = models.PositiveIntegerField()
    sysdescr = models.TextField(blank=True, null=True)
    domains_id = models.PositiveIntegerField()
    agents_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    accepted = models.IntegerField()
    hub = models.IntegerField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    snmpcredentials_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_unmanageds'


class GlpiUsbvendors(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    vendorid = models.CharField(max_length=4)
    deviceid = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_usbvendors'
        unique_together = (('vendorid', 'deviceid'),)


class GlpiUsercategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_usercategories'


class GlpiUseremails(models.Model):
    users_id = models.PositiveIntegerField()
    is_default = models.IntegerField()
    is_dynamic = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_useremails'
        unique_together = (('users_id', 'email'),)


class GlpiUsers(models.Model):
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
        managed = False
        db_table = 'glpi_users'
        unique_together = (('name', 'authtype', 'auths_id'),)


class GlpiUsertitles(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_usertitles'


class GlpiVirtualmachinestates(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_virtualmachinestates'


class GlpiVirtualmachinesystems(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_virtualmachinesystems'


class GlpiVirtualmachinetypes(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_virtualmachinetypes'


class GlpiVlans(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    tag = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_vlans'


class GlpiVobjects(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_vobjects'
        unique_together = (('itemtype', 'items_id'),)


class GlpiWifinetworks(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    essid = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_wifinetworks'
