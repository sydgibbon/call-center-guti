from django.db import models

class Agents(models.Model):
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
        managed = True
        db_table = 'agents'


class Agenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'agenttypes'


class Alerts(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    type = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'alerts'
        unique_together = (('itemtype', 'items_id', 'type'),)


class Apiclients(models.Model):
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
        managed = True
        db_table = 'apiclients'


class Applianceenvironments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'applianceenvironments'


class Appliances(models.Model):
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
        managed = True
        db_table = 'appliances'


class AppliancesItems(models.Model):
    appliances_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'appliances_items'
        unique_together = (('appliances_id', 'items_id', 'itemtype'),)


class AppliancesItemsRelations(models.Model):
    appliances_items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'appliances_items_relations'


class Appliancetypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    externalidentifier = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'appliancetypes'


class Authldapreplicates(models.Model):
    authldaps_id = models.PositiveIntegerField()
    host = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    timeout = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'authldapreplicates'


class Authldaps(models.Model):
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
        managed = True
        db_table = 'authldaps'


class Authmails(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    connect_string = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'authmails'


class Autoupdatesystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'autoupdatesystems'


class Blacklistedmailcontents(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'blacklistedmailcontents'


class Blacklists(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'blacklists'


class Budgets(models.Model):
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
        managed = True
        db_table = 'budgets'


class Budgettypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'budgettypes'


class Businesscriticities(models.Model):
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
        managed = True
        db_table = 'businesscriticities'
        unique_together = (('businesscriticities_id', 'name'),)





class Calendars(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    cache_duration = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendars'


class CalendarsHolidays(models.Model):
    calendars_id = models.PositiveIntegerField()
    holidays_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'calendars_holidays'
        unique_together = (('calendars_id', 'holidays_id'),)


class Calendarsegments(models.Model):
    calendars_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    day = models.IntegerField()
    begin = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendarsegments'


class Certificates(models.Model):
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
        managed = True
        db_table = 'certificates'


class CertificatesItems(models.Model):
    certificates_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'certificates_items'
        unique_together = (('certificates_id', 'itemtype', 'items_id'),)


class Certificatetypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'certificatetypes'


class Changecosts(models.Model):
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
        managed = True
        db_table = 'changecosts'


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


class ChangesGroups(models.Model):
    changes_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'changes_groups'
        unique_together = (('changes_id', 'type', 'groups_id'),)


class ChangesItems(models.Model):
    changes_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'changes_items'
        unique_together = (('changes_id', 'itemtype', 'items_id'),)


class ChangesProblems(models.Model):
    changes_id = models.PositiveIntegerField()
    problems_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'changes_problems'
        unique_together = (('changes_id', 'problems_id'),)


class ChangesSuppliers(models.Model):
    changes_id = models.PositiveIntegerField()
    suppliers_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'changes_suppliers'
        unique_together = (('changes_id', 'type', 'suppliers_id'),)


class ChangesTickets(models.Model):
    changes_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'changes_tickets'
        unique_together = (('changes_id', 'tickets_id'),)


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


class Changetasks(models.Model):
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
        managed = True
        db_table = 'changetasks'


class Changetemplatehiddenfields(models.Model):
    changetemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'changetemplatehiddenfields'
        unique_together = (('changetemplates_id', 'num'),)


class Changetemplatemandatoryfields(models.Model):
    changetemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'changetemplatemandatoryfields'
        unique_together = (('changetemplates_id', 'num'),)


class Changetemplatepredefinedfields(models.Model):
    changetemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'changetemplatepredefinedfields'


class Changetemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'changetemplates'


class Changevalidations(models.Model):
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
        managed = True
        db_table = 'changevalidations'


class Clusters(models.Model):
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
        managed = True
        db_table = 'clusters'


class Clustertypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clustertypes'


class Computerantiviruses(models.Model):
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
        managed = True
        db_table = 'computerantiviruses'



class Computervirtualmachines(models.Model):
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
        managed = True
        db_table = 'computervirtualmachines'


class Configs(models.Model):
    context = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'configs'
        unique_together = (('context', 'name'),)





class Contacts(models.Model):
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
        managed = True
        db_table = 'contacts'


class ContactsSuppliers(models.Model):
    suppliers_id = models.PositiveIntegerField()
    contacts_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'contacts_suppliers'
        unique_together = (('suppliers_id', 'contacts_id'),)


class Contacttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contacttypes'


class Contractcosts(models.Model):
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
        managed = True
        db_table = 'contractcosts'


class Contracts(models.Model):
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
        managed = True
        db_table = 'contracts'


class ContractsItems(models.Model):
    contracts_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'contracts_items'
        unique_together = (('contracts_id', 'itemtype', 'items_id'),)


class ContractsSuppliers(models.Model):
    suppliers_id = models.PositiveIntegerField()
    contracts_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'contracts_suppliers'
        unique_together = (('suppliers_id', 'contracts_id'),)


class Contracttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contracttypes'


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


class DashboardsDashboards(models.Model):
    key = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'dashboards_dashboards'


class DashboardsFilters(models.Model):
    dashboards_dashboards_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    filter = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dashboards_filters'


class DashboardsItems(models.Model):
    dashboards_dashboards_id = models.PositiveIntegerField()
    gridstack_id = models.CharField(max_length=100)
    card_id = models.CharField(max_length=100)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    card_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dashboards_items'


class DashboardsRights(models.Model):
    dashboards_dashboards_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'dashboards_rights'
        unique_together = (('dashboards_dashboards_id', 'itemtype', 'items_id'),)


class Databaseinstancecategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'databaseinstancecategories'


class Databaseinstances(models.Model):
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
        managed = True
        db_table = 'databaseinstances'


class Databaseinstancetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'databaseinstancetypes'


class Databases(models.Model):
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
        managed = True
        db_table = 'databases'


class Datacenters(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    locations_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'datacenters'


class Dcrooms(models.Model):
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
        managed = True
        db_table = 'dcrooms'


class Devicebatteries(models.Model):
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
        managed = True
        db_table = 'devicebatteries'


class Devicebatterymodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicebatterymodels'


class Devicebatterytypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicebatterytypes'


class Devicecameramodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicecameramodels'


class Devicecameras(models.Model):
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
        managed = True
        db_table = 'devicecameras'


class Devicecasemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicecasemodels'


class Devicecases(models.Model):
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
        managed = True
        db_table = 'devicecases'


class Devicecasetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicecasetypes'


class Devicecontrolmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicecontrolmodels'


class Devicecontrols(models.Model):
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
        managed = True
        db_table = 'devicecontrols'


class Devicedrivemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicedrivemodels'


class Devicedrives(models.Model):
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
        managed = True
        db_table = 'devicedrives'


class Devicefirmwaremodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicefirmwaremodels'


class Devicefirmwares(models.Model):
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
        managed = True
        db_table = 'devicefirmwares'


class Devicefirmwaretypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicefirmwaretypes'


class Devicegenericmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegenericmodels'


class Devicegenerics(models.Model):
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
        managed = True
        db_table = 'devicegenerics'


class Devicegenerictypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegenerictypes'


class Devicegraphiccardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegraphiccardmodels'


class Devicegraphiccards(models.Model):
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
        managed = True
        db_table = 'devicegraphiccards'


class Deviceharddrivemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deviceharddrivemodels'


class Deviceharddrives(models.Model):
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
        managed = True
        db_table = 'deviceharddrives'


class Devicememories(models.Model):
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
        managed = True
        db_table = 'devicememories'


class Devicememorymodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicememorymodels'


class Devicememorytypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicememorytypes'


class Devicemotherboardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicemotherboardmodels'


class Devicemotherboards(models.Model):
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
        managed = True
        db_table = 'devicemotherboards'


class Devicenetworkcardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicenetworkcardmodels'


class Devicenetworkcards(models.Model):
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
        managed = True
        db_table = 'devicenetworkcards'


class Devicepcimodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicepcimodels'


class Devicepcis(models.Model):
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
        managed = True
        db_table = 'devicepcis'


class Devicepowersupplies(models.Model):
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
        managed = True
        db_table = 'devicepowersupplies'


class Devicepowersupplymodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicepowersupplymodels'


class Deviceprocessormodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deviceprocessormodels'


class Deviceprocessors(models.Model):
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
        managed = True
        db_table = 'deviceprocessors'


class Devicesensormodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesensormodels'


class Devicesensors(models.Model):
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
        managed = True
        db_table = 'devicesensors'


class Devicesensortypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesensortypes'



class Devicesoundcardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesoundcardmodels'


class Devicesoundcards(models.Model):
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
        managed = True
        db_table = 'devicesoundcards'


class Displaypreferences(models.Model):
    itemtype = models.CharField(max_length=100)
    num = models.IntegerField()
    rank = models.IntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'displaypreferences'
        unique_together = (('users_id', 'itemtype', 'num'),)


class Documentcategories(models.Model):
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
        managed = True
        db_table = 'documentcategories'
        unique_together = (('documentcategories_id', 'name'),)


class Documents(models.Model):
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
        managed = True
        db_table = 'documents'


class DocumentsItems(models.Model):
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
        managed = True
        db_table = 'documents_items'
        unique_together = (('documents_id', 'itemtype', 'items_id', 'timeline_position'),)


class Documenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ext = models.CharField(unique=True, max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    mime = models.CharField(max_length=255, blank=True, null=True)
    is_uploadable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'documenttypes'


class Domainrecords(models.Model):
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
        managed = True
        db_table = 'domainrecords'


class Domainrecordtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    fields = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'domainrecordtypes'


class Domainrelations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'domainrelations'


class Domains(models.Model):
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
        managed = True
        db_table = 'domains'


class DomainsItems(models.Model):
    domains_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    domainrelations_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'domains_items'
        unique_together = (('domains_id', 'itemtype', 'items_id'),)


class Domaintypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'domaintypes'


class Dropdowntranslations(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dropdowntranslations'
        unique_together = (('itemtype', 'items_id', 'language', 'field'),)


class Enclosuremodels(models.Model):
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
        managed = True
        db_table = 'enclosuremodels'



class Entities(models.Model):
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
        managed = True
        db_table = 'entities'
        unique_together = (('entities_id', 'name'),)


class EntitiesKnowbaseitems(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'entities_knowbaseitems'


class EntitiesReminders(models.Model):
    reminders_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'entities_reminders'


class EntitiesRssfeeds(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'entities_rssfeeds'


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


class Fieldblacklists(models.Model):
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
        managed = True
        db_table = 'fieldblacklists'


class Fieldunicities(models.Model):
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
        managed = True
        db_table = 'fieldunicities'


class Filesystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'filesystems'


class Fqdns(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdn = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fqdns'


class Groups(models.Model):
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
        managed = True
        db_table = 'groups'


class GroupsKnowbaseitems(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_knowbaseitems'


class GroupsProblems(models.Model):
    problems_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_problems'
        unique_together = (('problems_id', 'type', 'groups_id'),)


class GroupsReminders(models.Model):
    reminders_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_reminders'


class GroupsRssfeeds(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_rssfeeds'


class GroupsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_tickets'
        unique_together = (('tickets_id', 'type', 'groups_id'),)


class GroupsUsers(models.Model):
    users_id = models.PositiveIntegerField()
    groups_id = models.PositiveIntegerField()
    is_dynamic = models.IntegerField()
    is_manager = models.IntegerField()
    is_userdelegate = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'groups_users'
        unique_together = (('users_id', 'groups_id'),)


class Holidays(models.Model):
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
        managed = True
        db_table = 'holidays'


class Imageformats(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'imageformats'


class Imageresolutions(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    is_video = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'imageresolutions'


class Impactcompounds(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'impactcompounds'


class Impactcontexts(models.Model):
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
        managed = True
        db_table = 'impactcontexts'


class Impactitems(models.Model):
    itemtype = models.CharField(max_length=255)
    items_id = models.PositiveIntegerField()
    parent_id = models.PositiveIntegerField()
    impactcontexts_id = models.PositiveIntegerField()
    is_slave = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'impactitems'
        unique_together = (('itemtype', 'items_id'),)


class Impactrelations(models.Model):
    itemtype_source = models.CharField(max_length=255)
    items_id_source = models.PositiveIntegerField()
    itemtype_impacted = models.CharField(max_length=255)
    items_id_impacted = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'impactrelations'
        unique_together = (('itemtype_source', 'items_id_source', 'itemtype_impacted', 'items_id_impacted'),)


class Infocoms(models.Model):
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
        managed = True
        db_table = 'infocoms'
        unique_together = (('itemtype', 'items_id'),)


class Interfacetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'interfacetypes'


class Ipaddresses(models.Model):
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
        managed = True
        db_table = 'ipaddresses'


class IpaddressesIpnetworks(models.Model):
    ipaddresses_id = models.PositiveIntegerField()
    ipnetworks_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'ipaddresses_ipnetworks'
        unique_together = (('ipaddresses_id', 'ipnetworks_id'),)


class Ipnetworks(models.Model):
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
        managed = True
        db_table = 'ipnetworks'


class IpnetworksVlans(models.Model):
    ipnetworks_id = models.PositiveIntegerField()
    vlans_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'ipnetworks_vlans'
        unique_together = (('ipnetworks_id', 'vlans_id'),)


class ItemsClusters(models.Model):
    clusters_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'items_clusters'
        unique_together = (('clusters_id', 'itemtype', 'items_id'),)


class ItemsDevicebatteries(models.Model):
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
        managed = True
        db_table = 'items_devicebatteries'


class ItemsDevicecameras(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecameras_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_devicecameras'


class ItemsDevicecamerasImageformats(models.Model):
    item_devicecameras_id = models.PositiveIntegerField()
    imageformats_id = models.PositiveIntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_devicecameras_imageformats'


class ItemsDevicecamerasImageresolutions(models.Model):
    item_devicecameras_id = models.PositiveIntegerField()
    imageresolutions_id = models.PositiveIntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_devicecameras_imageresolutions'


class ItemsDevicecases(models.Model):
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
        managed = True
        db_table = 'items_devicecases'


class ItemsDevicecontrols(models.Model):
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
        managed = True
        db_table = 'items_devicecontrols'


class ItemsDevicedrives(models.Model):
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
        managed = True
        db_table = 'items_devicedrives'


class ItemsDevicefirmwares(models.Model):
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
        managed = True
        db_table = 'items_devicefirmwares'


class ItemsDevicegenerics(models.Model):
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
        managed = True
        db_table = 'items_devicegenerics'


class ItemsDevicegraphiccards(models.Model):
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
        managed = True
        db_table = 'items_devicegraphiccards'


class ItemsDeviceharddrives(models.Model):
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
        managed = True
        db_table = 'items_deviceharddrives'


class ItemsDevicememories(models.Model):
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
        managed = True
        db_table = 'items_devicememories'


class ItemsDevicemotherboards(models.Model):
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
        managed = True
        db_table = 'items_devicemotherboards'


class ItemsDevicenetworkcards(models.Model):
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
        managed = True
        db_table = 'items_devicenetworkcards'


class ItemsDevicepcis(models.Model):
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
        managed = True
        db_table = 'items_devicepcis'


class ItemsDevicepowersupplies(models.Model):
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
        managed = True
        db_table = 'items_devicepowersupplies'


class ItemsDeviceprocessors(models.Model):
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
        managed = True
        db_table = 'items_deviceprocessors'


class ItemsDevicesensors(models.Model):
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
        managed = True
        db_table = 'items_devicesensors'


class ItemsDevicesimcards(models.Model):
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
        managed = True
        db_table = 'items_devicesimcards'


class ItemsDevicesoundcards(models.Model):
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
        managed = True
        db_table = 'items_devicesoundcards'


class ItemsDisks(models.Model):
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
        managed = True
        db_table = 'items_disks'



class ItemsKanbans(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    state = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_kanbans'
        unique_together = (('itemtype', 'items_id', 'users_id'),)


class ItemsOperatingsystems(models.Model):
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
        managed = True
        db_table = 'items_operatingsystems'
        unique_together = (('items_id', 'itemtype', 'operatingsystems_id', 'operatingsystemarchitectures_id'),)


class ItemsProblems(models.Model):
    problems_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'items_problems'
        unique_together = (('problems_id', 'itemtype', 'items_id'),)


class ItemsProjects(models.Model):
    projects_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'items_projects'
        unique_together = (('projects_id', 'itemtype', 'items_id'),)



class ItemsRemotemanagements(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    remoteid = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_remotemanagements'


class ItemsSoftwarelicenses(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    softwarelicenses_id = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_softwarelicenses'


class ItemsSoftwareversions(models.Model):
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
        managed = True
        db_table = 'items_softwareversions'
        unique_together = (('itemtype', 'items_id', 'softwareversions_id'),)


class ItemsTickets(models.Model):
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'items_tickets'
        unique_together = (('itemtype', 'items_id', 'tickets_id'),)


class Itilcategories(models.Model):
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
        managed = True
        db_table = 'itilcategories'


class Itilfollowups(models.Model):
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
        managed = True
        db_table = 'itilfollowups'


class Itilfollowuptemplates(models.Model):
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
        managed = True
        db_table = 'itilfollowuptemplates'


class ItilsProjects(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    projects_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'itils_projects'
        unique_together = (('itemtype', 'items_id', 'projects_id'),)


class Itilsolutions(models.Model):
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
        managed = True
        db_table = 'itilsolutions'


class Knowbaseitemcategories(models.Model):
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
        managed = True
        db_table = 'knowbaseitemcategories'
        unique_together = (('entities_id', 'knowbaseitemcategories_id', 'name'),)


class Knowbaseitems(models.Model):
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
        managed = True
        db_table = 'knowbaseitems'


class KnowbaseitemsComments(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    parent_comment_id = models.PositiveIntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'knowbaseitems_comments'


class KnowbaseitemsItems(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'knowbaseitems_items'
        unique_together = (('itemtype', 'items_id', 'knowbaseitems_id'),)


class KnowbaseitemsKnowbaseitemcategories(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    knowbaseitemcategories_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'knowbaseitems_knowbaseitemcategories'


class KnowbaseitemsProfiles(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'knowbaseitems_profiles'


class KnowbaseitemsRevisions(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    revision = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    users_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'knowbaseitems_revisions'
        unique_together = (('knowbaseitems_id', 'revision', 'language'),)


class KnowbaseitemsUsers(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'knowbaseitems_users'


class Knowbaseitemtranslations(models.Model):
    knowbaseitems_id = models.PositiveIntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'knowbaseitemtranslations'


class Lineoperators(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    mcc = models.IntegerField(blank=True, null=True)
    mnc = models.IntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lineoperators'
        unique_together = (('mcc', 'mnc'),)


class Lines(models.Model):
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
        managed = True
        db_table = 'lines'


class Linetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'linetypes'


class Links(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    open_window = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'links'


class LinksItemtypes(models.Model):
    links_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'links_itemtypes'
        unique_together = (('itemtype', 'links_id'),)


class Locations(models.Model):
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
        managed = True
        db_table = 'locations'
        unique_together = (('entities_id', 'locations_id', 'name'),)


class Lockedfields(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    field = models.CharField(max_length=50)
    value = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_global = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'lockedfields'
        unique_together = (('itemtype', 'items_id', 'field'),)


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


class Mailcollectors(models.Model):
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
        managed = True
        db_table = 'mailcollectors'


class Manuallinks(models.Model):
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
        managed = True
        db_table = 'manuallinks'


class Manufacturers(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'manufacturers'


class Networkaliases(models.Model):
    entities_id = models.PositiveIntegerField()
    networknames_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdns_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkaliases'



class Networkinterfaces(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkinterfaces'


class Networknames(models.Model):
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
        managed = True
        db_table = 'networknames'


class Networkportaggregates(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    networkports_id_list = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportaggregates'


class Networkportaliases(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    networkports_id_alias = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportaliases'


class Networkportconnectionlogs(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    connected = models.IntegerField()
    networkports_id_source = models.PositiveIntegerField()
    networkports_id_destination = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'networkportconnectionlogs'


class Networkportdialups(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportdialups'


class Networkportethernets(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    items_devicenetworkcards_id = models.PositiveIntegerField()
    type = models.CharField(max_length=10, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportethernets'


class Networkportfiberchannels(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    items_devicenetworkcards_id = models.PositiveIntegerField()
    networkportfiberchanneltypes_id = models.PositiveIntegerField()
    wwn = models.CharField(max_length=16, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportfiberchannels'


class Networkportfiberchanneltypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportfiberchanneltypes'


class Networkportlocals(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportlocals'


class Networkportmetrics(models.Model):
    date = models.DateField(blank=True, null=True)
    ifinbytes = models.BigIntegerField()
    ifinerrors = models.BigIntegerField()
    ifoutbytes = models.BigIntegerField()
    ifouterrors = models.BigIntegerField()
    networkports_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportmetrics'
        unique_together = (('networkports_id', 'date'),)


class Networkports(models.Model):
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
        managed = True
        db_table = 'networkports'


class NetworkportsNetworkports(models.Model):
    networkports_id_1 = models.PositiveIntegerField()
    networkports_id_2 = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'networkports_networkports'
        unique_together = (('networkports_id_1', 'networkports_id_2'),)


class NetworkportsVlans(models.Model):
    networkports_id = models.PositiveIntegerField()
    vlans_id = models.PositiveIntegerField()
    tagged = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'networkports_vlans'
        unique_together = (('networkports_id', 'vlans_id'),)


class Networkporttypes(models.Model):
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
        managed = True
        db_table = 'networkporttypes'


class Networkportwifis(models.Model):
    networkports_id = models.PositiveIntegerField(unique=True)
    items_devicenetworkcards_id = models.PositiveIntegerField()
    wifinetworks_id = models.PositiveIntegerField()
    networkportwifis_id = models.PositiveIntegerField()
    version = models.CharField(max_length=20, blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportwifis'


class Networks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networks'


class Notepads(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    users_id_lastupdater = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notepads'


class Notifications(models.Model):
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
        managed = True
        db_table = 'notifications'


class NotificationsNotificationtemplates(models.Model):
    notifications_id = models.PositiveIntegerField()
    mode = models.CharField(max_length=20)
    notificationtemplates_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'notifications_notificationtemplates'
        unique_together = (('notifications_id', 'mode', 'notificationtemplates_id'),)


class Notificationtargets(models.Model):
    items_id = models.PositiveIntegerField()
    type = models.IntegerField()
    notifications_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'notificationtargets'


class Notificationtemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notificationtemplates'


class Notificationtemplatetranslations(models.Model):
    notificationtemplates_id = models.PositiveIntegerField()
    language = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    content_text = models.TextField(blank=True, null=True)
    content_html = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notificationtemplatetranslations'


class Notimportedemails(models.Model):
    from_field = models.CharField(db_column='from', max_length=255)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=255)
    mailcollectors_id = models.PositiveIntegerField()
    date = models.DateTimeField()
    subject = models.TextField(blank=True, null=True)
    messageid = models.CharField(max_length=255)
    reason = models.IntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'notimportedemails'


class Objectlocks(models.Model):
    itemtype = models.CharField(max_length=100)
    items_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'objectlocks'
        unique_together = (('itemtype', 'items_id'),)


class Olalevelactions(models.Model):
    olalevels_id = models.PositiveIntegerField()
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'olalevelactions'


class Olalevelcriterias(models.Model):
    olalevels_id = models.PositiveIntegerField()
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'olalevelcriterias'


class Olalevels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    olas_id = models.PositiveIntegerField()
    execution_time = models.IntegerField()
    is_active = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    match = models.CharField(max_length=10, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'olalevels'


class OlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    olalevels_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'olalevels_tickets'
        unique_together = (('tickets_id', 'olalevels_id'),)


class Olas(models.Model):
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
        managed = True
        db_table = 'olas'


class Operatingsystemarchitectures(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystemarchitectures'


class Operatingsystemeditions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystemeditions'


class Operatingsystemkernels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystemkernels'


class Operatingsystemkernelversions(models.Model):
    operatingsystemkernels_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystemkernelversions'


class Operatingsystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystems'


class Operatingsystemservicepacks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystemservicepacks'


class Operatingsystemversions(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystemversions'


class Passivedcequipmentmodels(models.Model):
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
        managed = True
        db_table = 'passivedcequipmentmodels'


class Passivedcequipments(models.Model):
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
        managed = True
        db_table = 'passivedcequipments'


class Passivedcequipmenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'passivedcequipmenttypes'


class Pcivendors(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    vendorid = models.CharField(max_length=4)
    deviceid = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pcivendors'
        unique_together = (('vendorid', 'deviceid'),)


class Pdumodels(models.Model):
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
        managed = True
        db_table = 'pdumodels'





class Pdutypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdutypes'


class Pendingreasons(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    followup_frequency = models.IntegerField()
    followups_before_resolution = models.IntegerField()
    itilfollowuptemplates_id = models.PositiveIntegerField()
    solutiontemplates_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pendingreasons'


class PendingreasonsItems(models.Model):
    pendingreasons_id = models.PositiveIntegerField()
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    followup_frequency = models.IntegerField()
    followups_before_resolution = models.IntegerField()
    bump_count = models.IntegerField()
    last_bump_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pendingreasons_items'
        unique_together = (('items_id', 'itemtype'),)


class Peripheralmodels(models.Model):
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
        managed = True
        db_table = 'peripheralmodels'


class Peripherals(models.Model):
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
        managed = True
        db_table = 'peripherals'


class Peripheraltypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'peripheraltypes'






class Planningeventcategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planningeventcategories'


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


class Plugins(models.Model):
    directory = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    state = models.IntegerField()
    author = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plugins'


class Plugs(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plugs'


class Printerlogs(models.Model):
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
        managed = True
        db_table = 'printerlogs'
        unique_together = (('printers_id', 'date'),)



class Problemcosts(models.Model):
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
        managed = True
        db_table = 'problemcosts'


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


class ProblemsSuppliers(models.Model):
    problems_id = models.PositiveIntegerField()
    suppliers_id = models.PositiveIntegerField()
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problems_suppliers'
        unique_together = (('problems_id', 'type', 'suppliers_id'),)


class ProblemsTickets(models.Model):
    problems_id = models.PositiveIntegerField()
    tickets_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'problems_tickets'
        unique_together = (('problems_id', 'tickets_id'),)


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


class Problemtasks(models.Model):
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
        managed = True
        db_table = 'problemtasks'


class Problemtemplatehiddenfields(models.Model):
    problemtemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'problemtemplatehiddenfields'
        unique_together = (('problemtemplates_id', 'num'),)


class Problemtemplatemandatoryfields(models.Model):
    problemtemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'problemtemplatemandatoryfields'
        unique_together = (('problemtemplates_id', 'num'),)


class Problemtemplatepredefinedfields(models.Model):
    problemtemplates_id = models.PositiveIntegerField()
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problemtemplatepredefinedfields'


class Problemtemplates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problemtemplates'


class Profilerights(models.Model):
    profiles_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    rights = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'profilerights'
        unique_together = (('profiles_id', 'name'),)


class Profiles(models.Model):
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
        managed = True
        db_table = 'profiles'


class ProfilesReminders(models.Model):
    reminders_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'profiles_reminders'


class ProfilesRssfeeds(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField()
    no_entity_restriction = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'profiles_rssfeeds'


class ProfilesUsers(models.Model):
    users_id = models.PositiveIntegerField()
    profiles_id = models.PositiveIntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    is_dynamic = models.IntegerField()
    is_default_profile = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'profiles_users'


class Projectcosts(models.Model):
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
        managed = True
        db_table = 'projectcosts'


class Projects(models.Model):
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
        managed = True
        db_table = 'projects'


class Projectstates(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    is_finished = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projectstates'


class Projecttasklinks(models.Model):
    projecttasks_id_source = models.PositiveIntegerField()
    source_uuid = models.CharField(max_length=255)
    projecttasks_id_target = models.PositiveIntegerField()
    target_uuid = models.CharField(max_length=255)
    type = models.IntegerField()
    lag = models.SmallIntegerField(blank=True, null=True)
    lead = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projecttasklinks'


class Projecttasks(models.Model):
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
        managed = True
        db_table = 'projecttasks'


class ProjecttasksTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    projecttasks_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'projecttasks_tickets'
        unique_together = (('tickets_id', 'projecttasks_id'),)


class Projecttaskteams(models.Model):
    projecttasks_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'projecttaskteams'
        unique_together = (('projecttasks_id', 'itemtype', 'items_id'),)


class Projecttasktemplates(models.Model):
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
        managed = True
        db_table = 'projecttasktemplates'


class Projecttasktypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projecttasktypes'


class Projectteams(models.Model):
    projects_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'projectteams'
        unique_together = (('projects_id', 'itemtype', 'items_id'),)


class Projecttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projecttypes'


class Queuednotifications(models.Model):
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
        managed = True
        db_table = 'queuednotifications'


class Rackmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rackmodels'



class Racktypes(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'racktypes'


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


class Refusedequipments(models.Model):
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
        managed = True
        db_table = 'refusedequipments'


class Registeredids(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'registeredids'


class Reminders(models.Model):
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
        managed = True
        db_table = 'reminders'


class RemindersUsers(models.Model):
    reminders_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'reminders_users'


class Remindertranslations(models.Model):
    reminders_id = models.PositiveIntegerField()
    language = models.CharField(max_length=5, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'remindertranslations'


class Requesttypes(models.Model):
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
        managed = True
        db_table = 'requesttypes'


class Reservationitems(models.Model):
    itemtype = models.CharField(max_length=100)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    items_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'reservationitems'
        unique_together = (('itemtype', 'items_id'),)


class Reservations(models.Model):
    reservationitems_id = models.PositiveIntegerField()
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    group = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'reservations'


class Rssfeeds(models.Model):
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
        managed = True
        db_table = 'rssfeeds'


class RssfeedsUsers(models.Model):
    rssfeeds_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'rssfeeds_users'


class Ruleactions(models.Model):
    rules_id = models.PositiveIntegerField()
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ruleactions'


class Rulecriterias(models.Model):
    rules_id = models.PositiveIntegerField()
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rulecriterias'


class Rulematchedlogs(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    rules_id = models.PositiveIntegerField(blank=True, null=True)
    agents_id = models.PositiveIntegerField()
    method = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rulematchedlogs'


class Rulerightparameters(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rulerightparameters'


class Rules(models.Model):
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
        managed = True
        db_table = 'rules'


class Savedsearches(models.Model):
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
        managed = True
        db_table = 'savedsearches'


class SavedsearchesAlerts(models.Model):
    savedsearches_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    operator = models.IntegerField()
    value = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    frequency = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'savedsearches_alerts'
        unique_together = (('savedsearches_id', 'operator', 'value'),)


class SavedsearchesUsers(models.Model):
    users_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    savedsearches_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'savedsearches_users'
        unique_together = (('users_id', 'itemtype'),)


class Slalevelactions(models.Model):
    slalevels_id = models.PositiveIntegerField()
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slalevelactions'


class Slalevelcriterias(models.Model):
    slalevels_id = models.PositiveIntegerField()
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slalevelcriterias'


class Slalevels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slas_id = models.PositiveIntegerField()
    execution_time = models.IntegerField()
    is_active = models.IntegerField()
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    match = models.CharField(max_length=10, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slalevels'


class SlalevelsTickets(models.Model):
    tickets_id = models.PositiveIntegerField()
    slalevels_id = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slalevels_tickets'
        unique_together = (('tickets_id', 'slalevels_id'),)


class Slas(models.Model):
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
        managed = True
        db_table = 'slas'


class Slms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    use_ticket_calendar = models.IntegerField()
    calendars_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slms'


class Snmpcredentials(models.Model):
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
        managed = True
        db_table = 'snmpcredentials'


class Socketmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'socketmodels'


class Sockets(models.Model):
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
        managed = True
        db_table = 'sockets'



class Softwarelicensetypes(models.Model):
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
        managed = True
        db_table = 'softwarelicensetypes'



class Solutiontemplates(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    solutiontypes_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'solutiontemplates'


class Solutiontypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'solutiontypes'


class Ssovariables(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ssovariables'


class States(models.Model):
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
        managed = True
        db_table = 'states'
        unique_together = (('states_id', 'name'),)


class Suppliers(models.Model):
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
        managed = True
        db_table = 'suppliers'


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


class Suppliertypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suppliertypes'


class Taskcategories(models.Model):
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
        managed = True
        db_table = 'taskcategories'


class Tasktemplates(models.Model):
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
        managed = True
        db_table = 'tasktemplates'


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


class Transfers(models.Model):
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
        managed = True
        db_table = 'transfers'



class Usbvendors(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    vendorid = models.CharField(max_length=4)
    deviceid = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usbvendors'
        unique_together = (('vendorid', 'deviceid'),)


class Usercategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usercategories'


class Useremails(models.Model):
    users_id = models.PositiveIntegerField()
    is_default = models.IntegerField()
    is_dynamic = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'useremails'
        unique_together = (('users_id', 'email'),)


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


class Usertitles(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usertitles'


class Virtualmachinestates(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'virtualmachinestates'


class Virtualmachinesystems(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'virtualmachinesystems'


class Virtualmachinetypes(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'virtualmachinetypes'


class Vlans(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    tag = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vlans'


class Vobjects(models.Model):
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vobjects'
        unique_together = (('itemtype', 'items_id'),)


class Wifinetworks(models.Model):
    entities_id = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    essid = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wifinetworks'
