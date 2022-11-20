from django.db import models

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

