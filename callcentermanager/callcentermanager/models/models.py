from django.db import models

class Agents(models.Model):
    agenttypes_id = models.IntegerField(max_length=10, null=False)
    device_id = models.CharField(max_length=255, default= None, null=False)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    items_id = models.IntegerField(max_length=10, null=False)
    name = models.CharField(max_length=255, default= None, null=True)
    itemtype = models.CharField(max_length=100, null=False)

    last_contact = models.DateTimeField(auto_now_add=True)
    locked = models.SmallIntegerField(max_length=4, default= 0, null=False)
    port = models.CharField(max_length=6, default= None, null=True)
    tag = models.CharField(max_length=255, default= None, null=True)
    threads_networkdiscovery = models.IntegerField(max_length=11, default=1, null=False)
    threads_networkinventory = models.IntegerField(max_length=11, default=1, null=False)
    timeout_networkdiscovery = models.IntegerField(max_length=11, default=0, null=False)
    timeout_networkinventory = models.IntegerField(max_length=11, default=0, null=False)
    useragent = models.CharField(max_length=255, default= None, null=True)
    version = models.CharField(max_length=255, default= None, null=True)

class AgentTypes(models.Model):
    name = models.CharField(max_length=255, default= None, null=True)

class Alerts(models.Model):
    name = models.CharField(max_length=255, default= None, null=True)
    itemtype = models.CharField(max_length=100, null=False)
    items_id = models.IntegerField(max_length=10, null=False)
    type = models.IntegerField(max_length=11, default=0, null=False)
    date = models.DateTimeField(auto_now_add=True)

class ApiClients(models.Model):
    entities_id = models.IntegerField(max_length=10, default=0, null=False) #para tablas tipo INT
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False) #para tablas tipo TINY INT
    name = models.CharField(max_length=255, default= None, null=True) #para tablas tipo VARCHAR
    date_mod = models.DateTimeField(default = None, null= True)
    date_creation = models.DateTimeField(default = None, null= True) #para tablas tipo TIMESTAMP
    is_active = models.SmallIntegerField(max_length=4, default= 0, null=False)
    ipv4_range_start = models.BigIntegerField(max_length=20, default= None, null=True)
    ipv4_range_end = models.BigIntegerField(max_length=20, default= None, null=True) #para tablas tipo BIG INT
    ipv6 = models.CharField(max_length=255, default= None, null=True)
    app_token = models.CharField(max_length=255, default= None, null=True)
    app_token_date = models.DateTimeField(default = None, null= True)
    dolog_method = models.SmallIntegerField(max_length=4, default= 0, null=False)
    comment = models.TextField(default= None, null=True) #para tablas tipo TEXT

class ApplianceEnvironments(models.Model):
    name = models.CharField(max_length=255, default= None, null=True)
    comment = models.TextField(default= None, null=True)

class Appliances(models.model):
    entities_id = models.IntegerField(max_length=10, default=0, null=False) #para tablas tipo INT
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    name = models.CharField(max_length=255, default= None, null=True) #para tablas tipo VARCHAR
    is_deleted = models.SmallIntegerField(max_length=4, default= 0, null=False)
    appliancetypes_id = models.IntegerField(max_length=10, default=0, null=False)
    comment = models.TextField(default= None, null=True)
    locations_id = models.IntegerField(max_length=10, default=0, null=False)
    manufacturers_id = models.IntegerField(max_length=10, default=0, null=False)
    applianceenvironments_id = models.IntegerField(max_length=10, default=0, null=False)
    users_id = models.IntegerField(max_length=10, default=0, null=False)
    users_id_tech = models.IntegerField(max_length=10, default=0, null=False)
    groups_id = models.IntegerField(max_length=10, default=0, null=False)
    groups_id_tech = models.IntegerField(max_length=10, default=0, null=False)
    date_mod = models.DateTimeField(default = None, null= True)
    date_creation = models.DateTimeField(default = None, null= True)
    states_id = models.IntegerField(max_length=10, default=0, null=False)
    externalidentifier = models.CharField(max_length=255, default= None, null=True)
    serial = models.CharField(max_length=255, default= None, null=True)
    otherserial = models.CharField(max_length=255, default= None, null=True)
    is_helpdesk_visible = models.SmallIntegerField(max_length=4, default= 0, null=False)
    pictures = models.TextField(default= None, null=True)

class AppliancesItems(models.model):
    appliances_id = models.IntegerField(max_length=10, default=0, null=False)
    items_id = models.IntegerField(max_length=10, default=0, null=False)
    itemtype = models.CharField(max_length=100, null=False)

class AppliancesItemsRelations(models.model):
    appliances_items_id = models.IntegerField(max_length=10, default=0, null=False)
    itemtype = models.CharField(max_length=100, null=False)
    items_id = models.IntegerField(max_length=10, default=0, null=False)

class ApplianceTypes(models.model):
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    name = models.CharField(max_length=255, null=False)
    comment = models.TextField(default= None, null=True) #para tablas tipo TEXT
    externalidentifier = models.CharField(max_length=255, default= None, null=True)

class AuthLDAPReplicates(models.model):
    authldaps_id = models.IntegerField(max_length=10, default=0, null=False)
    host = models.CharField(max_length=255, default=None, null=True)
    port = models.IntegerField(max_length=11, default=389, null=False)
    name = models.CharField(max_length=255, default=False, null=True)
    timeout = models.IntegerField(max_length=11, default=10, null=False)

class AuthLDAPs(models.model):
    name = models.CharField(max_length=255, default=False, null=True)
    host = models.CharField(max_length=255, default=False, null=True)
    basedn = models.CharField(max_length=255, default=False, null=True)
    rootdn = models.CharField(max_length=255, default=False, null=True)
    port = models.IntegerField(max_length=11, default=389, null=False)
    condition = models.TextField(default= None, null=True)
    login_field = models.CharField(max_length=255, default=False, null=True)
    sync_field = models.CharField(max_length=255, default=False, null=True)
    use_tls = models.SmallIntegerField(max_length=4, default= 0, null=False)
    group_field = models.CharField(max_length=255, default=False, null=True)
    group_condition = models.TextField(default= None, null=True)
    group_search_type = models.IntegerField(max_length=11, default=0, null=False)
    group_member_field = models.CharField(max_length=255, default=False, null=True)
    email1_field = models.CharField(max_length=255, default=False, null=True)
    realname_field = models.CharField(max_length=255, default=False, null=True)
    phone_field = models.CharField(max_length=255, default=False, null=True)
    phone2_field = models.CharField(max_length=255, default=False, null=True)
    mobile_field = models.CharField(max_length=255, default=False, null=True)
    comment_field = models.CharField(max_length=255, default=False, null=True)
    use_dn = models.SmallIntegerField(max_length=4, default= 1, null=False)
    time_offset = models.IntegerField(max_length=11, default=0, null=False)
    deref_option = models.IntegerField(max_length=11, default=0, null=False)
    title_field = models.CharField(max_length=255, default=False, null=True)
    category_field = models.CharField(max_length=255, default=False, null=True)
    language_field = models.CharField(max_length=255, default=False, null=True)
    entity_field = models.CharField(max_length=255, default=False, null=True)
    entity_condition = models.TextField(default= None, null=True)
    date_mod = models.DateTimeField(default = None, null= True)
    comment = models.TextField(default= None, null=True)
    is_default = models.SmallIntegerField(max_length=4, default= 0, null=False)
    is_active = models.SmallIntegerField(max_length=4, default= 0, null=False)
    rootdn_passwd = models.CharField(max_length=255, default=False, null=True)
    registration_number_field = models.CharField(max_length=255, default=False, null=True)
    email2_field = models.CharField(max_length=255, default=False, null=True)
    email3_field = models.CharField(max_length=255, default=False, null=True)
    email4_field = models.CharField(max_length=255, default=False, null=True)
    location_field = models.CharField(max_length=255, default=False, null=True)
    responsible_field = models.CharField(max_length=255, default=False, null=True)
    pagesize = models.IntegerField(max_length=11, default=0, null=False)
    ldap_maxlimit = models.IntegerField(max_length=11, default=0, null=False)
    can_support_pagesize = models.SmallIntegerField(max_length=4, default= 0, null=False)
    picture_field = models.CharField(max_length=255, default=False, null=True)
    date_creation = models.DateTimeField(default = None, null= True)
    inventory_domain = models.CharField(max_length=255, default=False, null=True)
    tls_certfile = models.TextField(default= None, null=True)
    tls_keyfile = models.TextField(default= None, null=True)
    use_bind = models.SmallIntegerField(max_length=4, default= 0, null=False)
    timeout = models.IntegerField(max_length=11, default=10, null=False)

class AuthMails(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)
    connect_string = models.CharField(max_length=255, default=None, null=True)
    host = models.CharField(max_length=255, default=None,null=True)
    date_mod= models.TimeField(default=None, null=True)
    date_creation = models.TimeField(default=None, null=True)
    comment = models.TextField(null=True, default=None)
    is_active = models.SmallIntegerField(max_length=4, null=False, default=0)

class AutoUpdateSystems(models.Model):
    name = models.CharField(max_length=255, null=True, default= None)
    comment = models.TextField(null=True, default=None)

class BlacklistedMailContents(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    content = models.TextField(null=True, default=None)
    comment = models.TextField(null=True, default=None)
    date_mod = models.TimeField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)

class Blacklists(models.Model):
    type = models.IntegerField(max_length=11, null=False, default=0)
    name = models.CharField(max_length=255, null=True, default=None)
    value = models.CharField(max_length=255, null=True, default=None)
    text = models.TextField(null=True, default=None)
    date_mod = models.TimeField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)

class Budgets(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    comment = models.TextField(default= None, null=True) #para tablas tipo TEXT
    is_deleted = models.SmallIntegerField(max_length=4, default= 0, null=False)
    begin_date = models.DateField(null=True, default=None)
    end_date = models.DateField(null=True, default=None)
    value = models.DecimalField(max_digits=20, decimal_places=4, null=False, default=0.0000)
    is_template = models.SmallIntegerField(max_length=4, default= 0, null=False)
    template_name = models.CharField(max_length=255, null=True, default=None)
    date_mod = models.TimeField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)
    locations_id = models.IntegerField(max_length=10, default=0, null=False)
    budgettypes_id = models.IntegerField(max_length=10, default=0, null=False)

class BusinessCriticities(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    comment = models.TextField(default= None, null=True) #para tablas tipo TEXT
    date_mod = models.TimeField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)
    businesscriticities_id = models.IntegerField(max_length=10, default=0, null=False)
    completename = models.TextField(default= None, null=True) #para tablas tipo TEXT
    level = models.IntegerField(max_length=11, default=0, null=False)
    ancestors_cache = models.TextField(null=True,default=None)
    sons_cache = models.TextField(null=True,default=None)

class Cables(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    itemtype_endpoint_a = models.CharField(max_length=255, null=True, default=None)
    itemtype_endpoint_b = models.CharField(max_length=255, null=True, default=None)
    items_id_endpoint_a = models.IntegerField(max_length=10, default=0, null=False)
    items_id_endpoint_b = models.IntegerField(max_length=10, default=0, null=False)
    socketmodels_id_endpoint_a = models.IntegerField(max_length=10, default=0, null=False)
    socketmodels_id_endpoint_b = models.IntegerField(max_length=10, default=0, null=False)
    sockets_id_endpoint_a = models.IntegerField(max_length=10, default=0, null=False)
    sockets_id_endpoint_b = models.IntegerField(max_length=10, default=0, null=False)
    cablestrands_id = models.IntegerField(max_length=10, default=0, null=False)
    color = models.CharField(max_length=255, null=True, default=None)
    otherserial = models.CharField(max_length=255, null=True, default=None)
    states_id = models.IntegerField(max_length=10, default=0, null=False)
    users_id_tech = models.IntegerField(max_length=10, default=0, null=False)
    cabletypes_id = models.IntegerField(max_length=10, default=0, null=False)
    comment = models.TextField(null=True, default=None)
    date_mod = models.TimeField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)

class CableStrands(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    comment = models.TextField(null=True, default=None)
    date_mod = models.TimeField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)

class CableTypes(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    comment = models.TextField(null=True, default=None)
    date_mod = models.TimeField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)

class Calendars(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    comment = models.TextField(null=True, default=None)
    date_mod = models.TimeField(null=True, default=None)
    cache_duration = models.TextField(null=True, default=None)
    date_creation = models.TimeField(null=True, default=None)

class CalendarSegments(models.Model):
    calendars_id = models.IntegerField(max_length=10, default=0, null=False)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    day = models.SmallIntegerField(max_length=4, default= 0, null=False)
    begin = models.TimeField(null=True, default=None)
    end = models.TimeField(null=True, default=None)

class CalendarsHolidays(models.Model):
    calendars_id = models.IntegerField(max_length=10, default=0, null=False)
    holidays_id = models.IntegerField(max_length=10, default=0, null=False)

class CartridgeItems(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    ref = models.CharField(max_length=255, null=True, default=None)
    locations_id = models.IntegerField(max_length=10, default=0, null=False)
    cartridgeitemtypes_id = models.IntegerField(max_length=10, default=0, null=False)
    manufacturers_id = models.IntegerField(max_length=10, default=0, null=False)
    users_id_tech = models.IntegerField(max_length=10, default=0, null=False)

class CartridgeItemsPrinterModels(models.Model):
    cartridgeitems_id = models.IntegerField(max_length=10, default=0, null=False)
    printermodels_id = models.IntegerField(max_length=10, default=0, null=False)

#Hasta aca la mitad de la base de datos -Syd

    






