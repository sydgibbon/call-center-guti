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

class CartridgeItemTypes(models.Model):
    cartridgetype_id = models.IntegerField(max_length=10, null=False)
    name = models.CharField(max_length=255, null=True, default=None)
    comment = models.TextField(null=True, default=None)
    date_mod = models.DateTimeField(default=None, null=True)
    date_creation = models.DateTimeField(default=None, null=True)

class Cartridges(models.Model):
    cartridge_id = models.IntegerField(max_length=10, null=False)
    entities_id = models.IntegerField(max_length=10, default=0, null=False)
    cartridgeitems_id = models.IntegerField(max_length=10, default=0, null=False)
    printers_id = models.IntegerField(max_length=10, default=0, null=False)
    date_in = models.DateField(default=None, null=True) #Consultar tipo de dato "DATE" por "DateField" o "DateTimeField"
    date_use = models.DateField(default=None, null=True)
    date_out = models.DateField(default=None, null=True)
    pages = models.IntegerField(max_length=11, null=False)
    date_mod = models.DateTimeField(default=None, null=True) #hace falta el artibuto "default"
    date_creation = models.DateTimeField(default=None, null=True) #hace falta el artibuto "default"

class Certificates(models.Model):
    certificates_id = models.IntegerField(max_length= 10, null=False)
    name = models.CharField(max_length= 255, null=True, default=None)
    serial = models.CharField(max_length= 255, null=True, default=None)
    otherserial = models.CharField(max_length= 255, null=True, default=None)
    entities_id = models.IntegerField(max_length= 10, null=False)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    comment = models.TextField(default= None, null=True)
    is_deleted = models.SmallIntegerField(max_length=4, default= 0, null=False)
    is_template = models.SmallIntegerField(max_length=4, default= 0, null=False)
    template_name = models.CharField(max_length= 255, null=True, default=None)
    certificatetypes_id = models.IntegerField(max_length= 10, null=False)
    dns_name = models.CharField(max_length= 255, null=True, default=None)
    dns_suffix = models.CharField(max_length= 255, null=True, default=None)
    users_id_tech = models.IntegerField(max_length= 10, null=False, default=0)
    groups_id_tech = models.IntegerField(max_length= 10, null=False, default=0)
    locations_id = models.IntegerField(max_length= 10, null=False, default=0)
    manufacturers_id = models.IntegerField(max_length= 10, null=False, default=0)
    contact = models.CharField(max_length= 255, null=True, default=None)
    contact_num = models.CharField(max_length= 255, null=True, default=None)
    users_id = models.IntegerField(max_length= 10, null=False)
    groups_id = models.IntegerField(max_length= 10, null=False)
    is_autosign = models.SmallIntegerField(max_length=4, default= 0, null=False)
    date_expiration = models.DateField(default=None, null=True)
    states_id = models.IntegerField(max_length= 10, null=False, default=0)
    command = models.TextField(default= None, null=True)
    certificate_request = models.TextField(default= None, null=True)
    certificate_item = models.TextField(default= None, null=True)
    date_creation = models.DateTimeField(default=None, null=True)
    date_mod = models.DateTimeField(default=None, null=True)

class CertificatesItems(models.Model):
    certificatesitems_id = models.IntegerField(max_length= 10, null=False)
    certificates_id = models.IntegerField(max_length= 10, null=False, default=0)
    items_id = models.IntegerField(max_length= 10, null=False, default=0) #RELATION to various tables, according to itemtype (id)
    itemtype = models.CharField(max_length= 100, null=True, default=None) #see .class.php file
    date_creation = models.DateTimeField(default=None, null=True)
    date_mod = models.DateTimeField(default=None, null=True)

class CertificatesTypes(models.Model):
    certificatestypes_id = models.IntegerField(max_length= 10, null=False)
    entities_id = models.IntegerField(max_length= 10, null=False, default=0)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    name = models.CharField(max_length= 255, null=True, default=None)
    comment = models.TextField(default= None, null=True)
    date_creation = models.DateTimeField(default=None, null=True)
    date_mod = models.DateTimeField(default=None, null=True)

class ChangeCosts(models.Model):
    changecosts_id = models.IntegerField(max_length= 10, null=False)
    changes_id = models.IntegerField(max_length= 10, null=False, default=0)
    name = models.CharField(max_length= 255, null=True, default=None)
    comment = models.TextField(default= None, null=True)
    begin_date = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)
    actiontime = models.IntegerField(max_length= 11, null=False, default=0)
    cost_time = models.DecimalField(max_digits=24, decimal_places=4, null=False, default=0.0000) #Revisar con Syd
    cost_fixed = models.DecimalField(max_digits=24, decimal_places=4, null=False, default=0.0000) #Revisar con Syd
    cost_material = models.DecimalField(max_digits=24, decimal_places=4, null=False, default=0.0000) #Revisar con Syd
    budgets_id = models.IntegerField(max_length= 10, null=False, default=0)
    entities_id = models.IntegerField(max_length= 10, null=False, default=0)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)

class Changes(models.Model):
    changes_id = models.IntegerField(max_length= 10, null=False)
    name = models.CharField(max_length= 255, null=True, default=None)
    entities_id = models.IntegerField(max_length= 10, null=False, default=0)
    is_recursive = models.SmallIntegerField(max_length=4, default= 0, null=False)
    is_deleted = models.SmallIntegerField(max_length=4, default= 0, null=False)
    status = models.IntegerField(max_length= 11, null=False, default=1)
    content = models.TextField(default= None, null=True) #tipo de campo "LONGTEXT"
    date_mod = models.DateTimeField(default=None, null=True)
    date = models.DateTimeField(default=None, null=True)
    solvedate = models.DateTimeField(default=None, null=True)
    closedate = models.DateTimeField(default=None, null=True)
    time_to_resolve = models.DateTimeField(default=None, null=True)
    users_id_recipient = models.IntegerField(max_length= 10, null=False, default=0)
    users_id_lastupdater = models.IntegerField(max_length= 10, null=False, default=0)
    urgency = models.IntegerField(max_length=11, null=False, default=1)
    impact = models.IntegerField(max_length=11, null=False, default=1)
    priority = models.IntegerField(max_length=11, null=False, default=1)
    itilcategories_id = models.IntegerField(max_length=10, null=False, default=0)
    impactcontent = models.TextField(null=True, default=None)
    controlistcontent = models.TextField(null=True, default=None)
    rolloutplancontent = models.TextField(null=True, default=None)
    backoutplancontent = models.TextField(null=True, default=None)
    checklistcontent = models.TextField(null=True, default=None)
    global_validation = models.IntegerField(max_length=11, null=False, default=1)
    validation_percent = models.IntegerField(max_length=11, null=False, default=0)
    actiontime = models.IntegerField(max_length=11, null=False, default=0)
    begin_waiting_date = models.DateTimeField(null=True, default=None)
    waiting_duration = models.IntegerField(max_length=11, null=False, default=0)
    close_delay_stat = models.IntegerField(max_length=11, null=False, default=0)
    solve_delay_stat = models.IntegerField(max_length=11, null=False, default=0)
    date_creation = models.DateTimeField(null=True, default=None)
    
# Termino la parte de guti, empieza nata desde ChangesGroups

class ChangesGroups(models.Model):
    changes_id = models.IntegerField(max_length=10, null=0, default=0)
    groups_id = models.IntegerField(max_length=10, null=0, default=0)
    type = models.IntegerField(max_length=11, null=0, default=1)

class ChangesItems(models.Model):
    changes_id = models.IntegerField(max_length=10, null=False, default=0)
    itemtype = models.CharField(max_length=100, null=True, default=None)
    items_id = models.IntegerField(max_length=10, null=False, default=0)

class ChangesProblems(models.Model):
    changes_id = models.IntegerField(max_length=10, null=False, default=0)
    problems_id = models.IntegerField(max_length=10, null=False, default=0)

class ChangesSuppliers(models.Model):
    changes_id = models.IntegerField(max_length=10, null=False, default=0)
    suppliers_id = models.IntegerField(max_length=10, null=False, default=0)
    type = models.IntegerField(max_length=11, null=False, default=1)
    use_notification = models.SmallIntegerField(max_length=4, null=False, default=0)
    alternative_email = models.CharField(max_length= 255, null=True, default=None)

class ChangesTickets(models.Model):
    changes_id = models.IntegerField(max_length=10, null=False)
    tickets_id = models.IntegerField(max_length=10, null=False, default=0)

class ChangesUsers(models.Model):
    changes_id = models.IntegerField(max_length=10, null=False, default=0)
    users_id = models.IntegerField(max_length=10, null=False, default=0)
    type = models.IntegerField(max_length=11, null=False, default=1)
    use_notification = models.SmallIntegerField(max_length=4, null=False, default=0)
    alternative_email = models.CharField(max_length= 255, null=True, default=None)

class Changetasks(models.Model):
    uuid = models.CharField(max_length= 255, null=True, default=None)
    changes_id = models.IntegerField(max_length=10, null=False, default=0)
    taskcategories_id = models.IntegerField(max_length=10, null=False, default=0)
    state = models.IntegerField(max_length=11, null=False, default=0)
    date = models.DateTimeField(null=True, default=None)  
    begin = models.DateTimeField(null=True, default=None)  
    end = models.DateTimeField(null=True, default=None)
    users_id = models.IntegerField(max_length=10, null=False, default=0)
    users_id_editor = models.IntegerField(max_length=10, null=False, default=0)
    users_id_tech = models.IntegerField(max_length=10, null=False, default=0)
    groups_id_tech = models.IntegerField(max_length=10, null=False, default=0)
    content = models.TextField(null=True, default=None)
    actiontime = models.IntegerField(max_length=11, null=False, default=0)
    date_mod = models.DateTimeField(null=True, default=None)
    date_creation = models.DateTimeField(null=True, default=None)
    tasktemplates_id = models.IntegerField(max_length=10, null=False, default=0)
    timeline_position = models.SmallIntegerField(max_length=4, null=False, default=0)
    is_private = models.SmallIntegerField(max_length=4, null=False, default=0)

class Changetemplatehiddenfields(models.Model):
    changetemplates_id = models.IntegerField(max_length=10, null=False, default=0)
    num = models.IntegerField(max_length=11, null=False, default=0)

class Changetemplatemandatoryfields(models.Model):
    changetemplates_id = models.IntegerField(max_length=10, null=False, default=0)
    num = models.IntegerField(max_length=11, null=False, default=0)

class Changetemplatepredefinedfields(models.Model):
    changetemplates_id = models.IntegerField(max_length=10, null=False, default=0)
    num = models.IntegerField(max_length=11, null=False, default=0)
    value = models.TextField(null=True, default= None)

class Changetemplates(models.Model):
    name = models.CharField(max_length= 255, null=True, default=None)
    entities_id = models.IntegerField(max_length=10, null=False, default=0)
    is_recursive = models.SmallIntegerField(max_length=4, null=False, default=0)
    comment = models.TextField(null=True, default=None)

class Changevalidations(models.Model):
    entities_id = models.IntegerField(max_length=10, null=False, default=0)
    is_recursive = models.SmallIntegerField(max_length=4, null=False, default=0)
    users_id = models.IntegerField(max_length=10, null=False, default=0)
    changes_id = models.IntegerField(max_length=10, null=False, default=0)
    users_id_validate = models.IntegerField(max_length=10, null=False, default=0)
    comment_submission = models.TextField(null=True, default=None)
    comment_validation = models.TextField(null=True, default=None)
    status = models.IntegerField(max_length=11, null=False, default=2)
    submission_date = models.DateTimeField(null=True, default=None)
    validation_date = models.DateTimeField(null=True, default=None)
    timeline_position = models.SmallIntegerField(max_length=4, null=False, default=0)

class Clusters(models.Model):
    entities_id = models.IntegerField(max_length=10, null=False, default=0)
    is_recursive = models.SmallIntegerField(max_length=4, null=False, default=0)
    name = models.CharField(max_length=255, null=True, default= None)
    uuid = models.CharField(max_length= 255, null=True, default=None)
    version = models.CharField(max_length=255, null=True, default= None)
    users_id_tech = models.IntegerField(max_length=10, null=False, default=0)
    groups_id_tech = models.IntegerField(max_length=10, null=False, default=0)
    is_deleted = models.SmallIntegerField(max_length=4, null=False, default= 0)
    states_id = models.IntegerField(max_length=10, null=False, default=0)
    comment = models.TextField(null=True, default= None)
    clustertypes_id = models.IntegerField(max_length=10, null=False, default=0)
    autoupdatesystems_id = models.IntegerField(max_length=10, null=False, default=0)
    date_mod = models.DateTimeField(default = None, null= True)
    date_creation = models.DateTimeField(default = None, null= True)

class Clusterstype(models.Model):
    entities_id = models.IntegerField(max_length=10, null=False, default=0)
    is_recursive = models.SmallIntegerField(max_length=4, null=False, default=0)
    name = models.CharField(max_length=255, null=True, default= None)
    comment = models.TextField(null=True, default=None)
    date_creation = models.DateTimeField(default=None, null=True)
    date_mod = models.DateTimeField(default=None, null=True)

class Computerantiviruses(models.Model):
    computers_id = models.IntegerField(max_length=10, null=False, default=0)
    name = models.CharField(max_length=255, null=True, default= None)
    manufacturers_id = models.IntegerField(max_length=10, default=0, null=False)
    antivirus_version = models.CharField(max_length=255, null=True, default= None)
    signature_version = models.CharField(max_length=255, null=True, default= None)
    is_active = models.SmallIntegerField(max_length=4, default= 0, null=False)
    is_deleted = models.SmallIntegerField(max_length=4, default= 0, null=False)
    is_uptodate = models.SmallIntegerField(max_length=4, default= 0, null=False)
    is_dynamic = models.SmallIntegerField(max_length=4, default= 0, null=False)
    date_expiration = models.DateField(default=None, null=True)
    date_mod = models.DateTimeField(default = None, null= True)
    date_creation = models.DateTimeField(default = None, null= True)

class Computermodels(models.Model):
    name = models.CharField(max_length=255, null=True, default= None)
    comment = models.TextField(null=True, default= None)
    product_number = models.CharField(max_length=255, null=True, default=None)
    weight = models.IntegerField(max_length=11, default=0, null=False)
    required_units = models.IntegerField(max_length=11, default=1, null=False)
    depth = models.DecimalField(decimal_places=4, null=False, default=1)
    power_connections = models.IntegerField(max_length=11, default=0, null=False)
    power_consumption = models.IntegerField(max_length=11, default=0, null=False)
    is_half_rack = models.SmallIntegerField(max_length=4, default= 0, null=False)
    picture_front = models.TextField(null=True, default= None)
    picture_rear = models.TextField(null=True, default= None)
    pictures = models.TextField(null=True, default= None)
    date_mod = models.DateTimeField(default = None, null=True)
    date_creation = models.DateTimeField(default = None, null=True)