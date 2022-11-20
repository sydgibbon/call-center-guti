from django.db import models
from assistance import models as assistanceModels


class Autoupdatesystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'autoupdatesystems'


class Manufacturers(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'manufacturers'


class Operatingsystems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operatingsystems'


class Networks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networks'


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
    group_member_field = models.CharField(
        max_length=255, blank=True, null=True)
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
    registration_number_field = models.CharField(
        max_length=255, blank=True, null=True)
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


class Entities(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='entities_entities')
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    sons_cache = models.TextField(blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    registration_number = models.CharField(
        max_length=255, blank=True, null=True)
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
    noreply_email_name = models.CharField(
        max_length=255, blank=True, null=True)
    replyto_email = models.CharField(max_length=255, blank=True, null=True)
    replyto_email_name = models.CharField(
        max_length=255, blank=True, null=True)
    notification_subject_tag = models.CharField(
        max_length=255, blank=True, null=True)
    ldap_dn = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    authldaps = models.ForeignKey(
        Authldaps, on_delete=models.CASCADE, blank=True, null=True)
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
    calendars = models.ForeignKey(
        assistanceModels.Calendars, on_delete=models.CASCADE, blank=True, null=True)
    auto_assign_mode = models.IntegerField()
    tickettype = models.IntegerField()
    max_closedate = models.DateTimeField(blank=True, null=True)
    inquest_config = models.IntegerField()
    inquest_rate = models.IntegerField()
    inquest_delay = models.IntegerField()
    # Field name made lowercase.
    inquest_url = models.CharField(
        db_column='inquest_URL', max_length=255, blank=True, null=True)
    autofill_warranty_date = models.CharField(max_length=255)
    autofill_use_date = models.CharField(max_length=255)
    autofill_buy_date = models.CharField(max_length=255)
    autofill_delivery_date = models.CharField(max_length=255)
    autofill_order_date = models.CharField(max_length=255)
    tickettemplates_strategy = models.IntegerField()
    tickettemplates = models.ForeignKey(
        assistanceModels.Tickettemplates, on_delete=models.CASCADE, blank=True, null=True)
    changetemplates_strategy = models.IntegerField()
    changetemplates = models.PositiveIntegerField()
    problemtemplates_strategy = models.IntegerField()
    problemtemplates = models.PositiveIntegerField()
    entities_strategy_software = models.IntegerField()
    entities_software = models.PositiveIntegerField()
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
    contracts_default = models.PositiveIntegerField()
    enable_custom_css = models.IntegerField()
    custom_css_code = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    altitude = models.CharField(max_length=255, blank=True, null=True)
    transfers_strategy = models.IntegerField()
    transfers = models.PositiveIntegerField()
    agent_base_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'entities'
        unique_together = (('entities_id', 'name'),)


class Locations(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='locations_locations')
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


class States(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    states = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='states_states')
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


class Softwarecategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    softwarecategories = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='softwarecategories_softwarecategories')
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwarecategories'


class Softwares(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='softwares_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='softwares_groups_tech')
    is_update = models.IntegerField()
    softwares = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='softwares_softwares')
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_helpdesk_visible = models.IntegerField()
    softwarecategories = models.ForeignKey(
        Softwarecategories, on_delete=models.CASCADE, blank=True, null=True)
    is_valid = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwares'


class Networkequipmentmodels(models.Model):
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
        db_table = 'networkequipmentmodels'


class Networkequipmenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkequipmenttypes'


class Networkequipments(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='networkequipments_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='networkequipments_groups_tech')
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True)
    networkequipmenttypes = models.ForeignKey(
        Networkequipmenttypes, on_delete=models.CASCADE, blank=True, null=True)
    networkequipmentmodels = models.ForeignKey(
        Networkequipmentmodels, on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True)
    sysdescr = models.TextField(blank=True, null=True)
    cpu = models.IntegerField()
    uptime = models.CharField(max_length=255)
    last_inventory_update = models.DateTimeField(blank=True, null=True)
    snmpcredentials = models.ForeignKey(
        Snmpcredentials, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkequipments'


class Printermodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'printermodels'


class Printertypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'printertypes'


class Printers(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='printers_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='printers_groups_tech')
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    have_serial = models.IntegerField()
    have_parallel = models.IntegerField()
    have_usb = models.IntegerField()
    have_wifi = models.IntegerField()
    have_ethernet = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    memory_size = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True)
    printertypes = models.ForeignKey(
        Printertypes, on_delete=models.CASCADE, blank=True, null=True)
    printermodels = models.ForeignKey(
        Printermodels, on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    init_pages_counter = models.IntegerField()
    last_pages_counter = models.IntegerField()
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    sysdescr = models.TextField(blank=True, null=True)
    last_inventory_update = models.DateTimeField(blank=True, null=True)
    snmpcredentials = models.ForeignKey(
        Snmpcredentials, on_delete=models.CASCADE, blank=True, null=True)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'printers'


class Cartridgeitems(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    cartridgeitemtypes = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='cartridgeitems_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='cartridgeitems_groups_tech')
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField()
    stock_target = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cartridgeitems'


class Cartridges(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    cartridgeitems = models.ForeignKey(
        Cartridgeitems, on_delete=models.CASCADE, blank=True, null=True)
    printers = models.ForeignKey(
        Printers, on_delete=models.CASCADE, blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    date_use = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    pages = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cartridges'


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
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'racktypes'


class Consumableitemtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'consumableitemtypes'


class Consumableitems(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    consumableitemtypes = models.ForeignKey(
        Consumableitemtypes, on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='consumableitems_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='consumableitems_groups_tech')
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField()
    stock_target = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'consumableitems'


class Consumables(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    consumableitems = models.ForeignKey(
        Consumableitems, on_delete=models.CASCADE, blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items = models.ForeignKey(
        Cartridgeitems, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'consumables'


class Datacenters(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'datacenters'


class Dcrooms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    vis_cols = models.IntegerField(blank=True, null=True)
    vis_rows = models.IntegerField(blank=True, null=True)
    blueprint = models.TextField(blank=True, null=True)
    datacenters = models.ForeignKey(
        Datacenters, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dcrooms'


class Racks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    rackmodels = models.ForeignKey(
        Rackmodels, on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    racktypes = models.ForeignKey(
        Racktypes, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='racks_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='racks_groups_tech')
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    number_units = models.IntegerField(blank=True, null=True)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    dcrooms = models.ForeignKey(
        Dcrooms, on_delete=models.CASCADE, blank=True, null=True)
    room_orientation = models.IntegerField()
    position = models.CharField(max_length=50, blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    max_power = models.IntegerField()
    mesured_power = models.IntegerField()
    max_weight = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'racks'


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


class Enclosures(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    enclosuremodels = models.ForeignKey(
        Enclosuremodels, on_delete=models.CASCADE, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='enclosures_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='enclosures_groups_tech')
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    orientation = models.IntegerField(blank=True, null=True)
    power_supplies = models.IntegerField()
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enclosures'


class Pdutypes(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdutypes'


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


class Pdus(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    pdumodels = models.ForeignKey(
        Pdumodels, on_delete=models.CASCADE, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='pdus_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='pdus_groups_tech')
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    pdutypes = models.ForeignKey(
        Pdutypes, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdus'


class Unmanageds(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_deleted = models.IntegerField()
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True)
    sysdescr = models.TextField(blank=True, null=True)
    domains = models.ForeignKey(
        assistanceModels.Domains, on_delete=models.CASCADE, blank=True, null=True)
    agents = models.ForeignKey(
        assistanceModels.Agents, on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    accepted = models.IntegerField()
    hub = models.IntegerField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    snmpcredentials = models.ForeignKey(
        Snmpcredentials, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'unmanageds'


class Socketmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'socketmodels'


class Networkports(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    logical_number = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    instantiation_type = models.CharField(
        max_length=255, blank=True, null=True)
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


class Sockets(models.Model):
    position = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    socketmodels = models.ForeignKey(
        Socketmodels, on_delete=models.CASCADE, blank=True, null=True)
    wiring_side = models.IntegerField(blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sockets'


class Cablestrands(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cablestrands'


class Cabletypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cabletypes'


class Cables(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    itemtype_endpoint_a = models.CharField(
        max_length=255, blank=True, null=True)
    itemtype_endpoint_b = models.CharField(
        max_length=255, blank=True, null=True)
    items_endpoint_a = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    items_endpoint_b = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='cables_itemsEndpointB')
    socketmodels_endpoint_a = models.ForeignKey(
        Socketmodels, on_delete=models.CASCADE, blank=True, null=True, related_name='cables_socketModelsItemsEndpointA')
    socketmodels_endpoint_b = models.ForeignKey(
        Socketmodels, on_delete=models.CASCADE, blank=True, null=True, related_name='cables_socketModelsItemsEndpointB')
    sockets_endpoint_a = models.ForeignKey(
        Sockets, on_delete=models.CASCADE, blank=True, null=True)
    sockets_endpoint_b = models.ForeignKey(
        Sockets, on_delete=models.CASCADE, blank=True, null=True, related_name='cables_socketItemsEndpointA')
    cablestrands = models.ForeignKey(
        Cablestrands, on_delete=models.CASCADE, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='cables_users_tech')
    cabletypes = models.ForeignKey(
        Cabletypes, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cables'


class Devicesimcardtypes(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesimcardtypes'


class Devicesimcards(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    voltage = models.IntegerField(blank=True, null=True)
    devicesimcardtypes = models.ForeignKey(
        Devicesimcardtypes, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    allow_voip = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'devicesimcards'


class Computermodels(models.Model):
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
        db_table = 'computermodels'


class Computertypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'computertypes'


class Monitormodels(models.Model):
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
        db_table = 'monitormodels'


class Monitortypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'monitortypes'


class Softwarelicensetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    softwarelicensetypes = models.PositiveIntegerField()
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    entities = models.PositiveIntegerField()
    is_recursive = models.IntegerField()
    completename = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwarelicensetypes'


class Softwareversions(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    softwares = models.ForeignKey(
        Softwares, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    arch = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    operatingsystems = models.ForeignKey(
        Operatingsystems, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwareversions'


class Softwarelicenses(models.Model):
    softwares = models.ForeignKey(
        Softwares, on_delete=models.CASCADE, blank=True, null=True)
    softwarelicenses = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='softwarelicenses_softwarelicenses')
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    number = models.IntegerField()
    softwarelicensetypes = models.ForeignKey(
        Softwarelicensetypes, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    softwareversions_buy = models.ForeignKey(
        Softwareversions, on_delete=models.CASCADE, blank=True, null=True, related_name='softwarelicenses_softwareversions_buy')
    softwareversions_use = models.ForeignKey(
        Softwareversions, on_delete=models.CASCADE, blank=True, null=True, related_name='softwarelicenses_softwareversions_use')
    expire = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_valid = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='softwarelicenses_users_tech')
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='softwarelicenses_groups_tech')
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    is_helpdesk_visible = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    allow_overquota = models.IntegerField()
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwarelicenses'


class PrintersCartridgeinfos(models.Model):
    printers = models.ForeignKey(
        Printers, on_delete=models.CASCADE, blank=True, null=True)
    property = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'printers_cartridgeinfos'


class CartridgeitemsPrintermodels(models.Model):
    cartridgeitems = models.ForeignKey(
        Cartridgeitems, on_delete=models.CASCADE, blank=True, null=True)
    printermodels = models.ForeignKey(
        Printermodels, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cartridgeitems_printermodels'
        unique_together = (('printermodels_id', 'cartridgeitems_id'),)


class Cartridgeitemtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cartridgeitemtypes'


class Phonemodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phonemodels'


class Phonepowersupplies(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phonepowersupplies'


class Phonetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phonetypes'


class Phones(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='phones_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='phones_groups_tech')
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    phonetypes = models.ForeignKey(
        Phonetypes, on_delete=models.CASCADE, blank=True, null=True)
    phonemodels = models.ForeignKey(
        Phonemodels, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    phonepowersupplies = models.ForeignKey(
        Phonepowersupplies, on_delete=models.CASCADE, blank=True, null=True)
    number_line = models.CharField(max_length=255, blank=True, null=True)
    have_headset = models.IntegerField()
    have_hp = models.IntegerField()
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()
    last_inventory_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phones'


class ItemsRacks(models.Model):
    racks = models.ForeignKey(
        Racks, on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    position = models.IntegerField()
    orientation = models.IntegerField(blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    hpos = models.IntegerField()
    is_reserved = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_racks'
        unique_together = (('itemtype', 'items_id', 'is_reserved'),)


class ItemsEnclosures(models.Model):
    enclosures = models.ForeignKey(
        Enclosures, on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    position = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_enclosures'
        unique_together = (('itemtype', 'items_id'),)


class Plugs(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plugs'


class PdusPlugs(models.Model):
    plugs = models.ForeignKey(
        Plugs, on_delete=models.CASCADE, blank=True, null=True)
    pdus = models.ForeignKey(
        Pdus, on_delete=models.CASCADE, blank=True, null=True)
    number_plugs = models.IntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdus_plugs'


class PdusRacks(models.Model):
    racks = models.ForeignKey(
        Racks, on_delete=models.CASCADE, blank=True, null=True)
    pdus = models.ForeignKey(
        Pdus, on_delete=models.CASCADE, blank=True, null=True)
    side = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdus_racks'


class Devicebatterytypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicebatterytypes'


class Devicebatterymodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicebatterymodels'


class Devicebatteries(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    voltage = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    devicebatterytypes = models.ForeignKey(
        Devicebatterytypes, on_delete=models.CASCADE, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicebatterymodels = models.ForeignKey(
        Devicebatterymodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicebatteries'


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
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicecameramodels = models.ForeignKey(
        Devicecameramodels, on_delete=models.CASCADE, blank=True, null=True)
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


class Devicecasetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicecasetypes'


class Devicecases(models.Model):  # Hasta aqui - Guty
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicecasetypes = models.ForeignKey(
        Devicecasetypes, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicecasemodels = models.ForeignKey(
        Devicecasemodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicecases'


class Devicecontrolmodels(models.Model):  # hasta aca FRANNNNN
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicecontrolmodels'


class Interfacetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'interfacetypes'


class Devicecontrols(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    is_raid = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    interfacetypes = models.ForeignKey(
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicecontrolmodels = models.ForeignKey(
        Devicecontrolmodels, on_delete=models.CASCADE, blank=True, null=True)
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
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    interfacetypes = models.ForeignKey(
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicedrivemodels = models.ForeignKey(
        Devicedrivemodels, on_delete=models.CASCADE, blank=True, null=True)
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


class Devicefirmwaretypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicefirmwaretypes'


class Devicefirmwares(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwaretypes = models.ForeignKey(
        Devicefirmwaretypes, on_delete=models.CASCADE, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicefirmwaremodels = models.ForeignKey(
        Devicefirmwaremodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicefirmwares'


class Devicegenericmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegenericmodels'


class Devicegenerictypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegenerictypes'


class Devicegenerics(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicegenerictypes = models.ForeignKey(
        Devicegenerictypes, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    devicegenericmodels = models.ForeignKey(
        Devicegenericmodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegenerics'


class Devicegraphiccardmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegraphiccardmodels'


class Devicegraphiccards(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    interfacetypes = models.ForeignKey(
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    memory_default = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicegraphiccardmodels = models.ForeignKey(
        Devicegraphiccardmodels, on_delete=models.CASCADE, blank=True, null=True)
    chipset = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicegraphiccards'


class Deviceharddrivemodels(models.Model):                  # Acá toy
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deviceharddrivemodels'


class Deviceharddrives(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    rpm = models.CharField(max_length=255, blank=True, null=True)
    interfacetypes = models.ForeignKey(
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True)
    cache = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    capacity_default = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    deviceharddrivemodels = models.ForeignKey(
        Deviceharddrivemodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deviceharddrives'


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


class Devicememories(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    frequence = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    size_default = models.IntegerField()
    devicememorytypes = models.ForeignKey(
        Devicememorytypes, on_delete=models.CASCADE, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicememorymodels = models.ForeignKey(
        Devicememorymodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicememories'


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


class Peripheraltypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'peripheraltypes'


class Peripherals(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='peripherals_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='peripherals_groups_tech')
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    peripheraltypes = models.ForeignKey(
        Peripheraltypes, on_delete=models.CASCADE, blank=True, null=True)
    peripheralmodels = models.ForeignKey(
        Peripheralmodels, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'peripherals'


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
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicemotherboardmodels = models.ForeignKey(
        Devicemotherboardmodels, on_delete=models.CASCADE, blank=True, null=True)
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
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    mac_default = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicenetworkcardmodels = models.ForeignKey(
        Devicenetworkcardmodels, on_delete=models.CASCADE, blank=True, null=True)
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
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    devicenetworkcardmodels = models.ForeignKey(
        Devicenetworkcardmodels, on_delete=models.CASCADE, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicepcimodels = models.ForeignKey(
        Devicepcimodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicepcis'


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


class Devicepowersupplies(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    power = models.CharField(max_length=255, blank=True, null=True)
    is_atx = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicepowersupplymodels = models.ForeignKey(
        Devicepowersupplymodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicepowersupplies'


class Deviceprocessors(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    frequence = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    frequency_default = models.IntegerField()
    nbcores_default = models.IntegerField(blank=True, null=True)
    nbthreads_default = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    deviceprocessormodels = models.ForeignKey(
        Deviceprocessormodels, on_delete=models.CASCADE, blank=True, null=True)
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


class Devicesensortypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesensortypes'


class Devicesensors(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicesensortypes = models.ForeignKey(
        Devicesensortypes, on_delete=models.CASCADE, blank=True, null=True)
    devicesensormodels = models.ForeignKey(
        Devicesensormodels, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesensors'


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
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    devicesoundcardmodels = models.ForeignKey(
        Devicesoundcardmodels, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesoundcards'


class ItemsDevicebatteries(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicebatteries = models.ForeignKey(
        Devicebatteries, on_delete=models.CASCADE, blank=True, null=True)
    manufacturing_date = models.DateField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    real_capacity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_devicebatteries'


class ItemsDevicecameras(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecameras = models.ForeignKey(
        Devicecameras, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_devicecameras'


class Imageformats(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
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
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'imageresolutions'


class ItemsDevicecamerasImageformats(models.Model):
    item_devicecameras = models.ForeignKey(
        ItemsDevicecameras, on_delete=models.CASCADE, blank=True, null=True)
    imageformats = models.ForeignKey(
        Imageformats, on_delete=models.CASCADE, blank=True, null=True)
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_devicecameras_imageformats'


class ItemsDevicecamerasImageresolutions(models.Model):
    item_devicecameras = models.ForeignKey(
        ItemsDevicecameras, on_delete=models.CASCADE, blank=True, null=True)
    imageresolutions = models.ForeignKey(
        Imageresolutions, on_delete=models.CASCADE, blank=True, null=True)
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_devicecameras_imageresolutions'


class ItemsDevicecases(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecases = models.ForeignKey(
        Devicecases, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicecases'


class ItemsDevicecontrols(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecontrols = models.ForeignKey(
        Devicecontrols, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicecontrols'


class ItemsDevicedrives(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicedrives = models.ForeignKey(
        Devicedrives, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicedrives'


class ItemsDevicefirmwares(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwares = models.ForeignKey(
        Devicefirmwares, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicefirmwares'


class ItemsDevicegenerics(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegenerics = models.ForeignKey(
        Devicegenerics, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicegenerics'


class ItemsDevicegraphiccards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegraphiccards = models.ForeignKey(
        Devicegraphiccards, on_delete=models.CASCADE, blank=True, null=True)
    memory = models.IntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicegraphiccards'


class ItemsDeviceharddrives(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceharddrives = models.ForeignKey(
        Deviceharddrives, on_delete=models.CASCADE, blank=True, null=True)
    capacity = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_deviceharddrives'


class ItemsDevicememories(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicememories = models.ForeignKey(
        Devicememories, on_delete=models.CASCADE, blank=True, null=True)
    size = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicememories'


class ItemsDevicemotherboards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicemotherboards = models.ForeignKey(
        Devicemotherboards, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicemotherboards'


class ItemsDevicenetworkcards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicenetworkcards = models.ForeignKey(
        Devicenetworkcards, on_delete=models.CASCADE, blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicenetworkcards'


class ItemsDevicepcis(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepcis = models.ForeignKey(
        Devicepcis, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicepcis'


class ItemsDevicepowersupplies(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepowersupplies = models.ForeignKey(
        Devicepowersupplies, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicepowersupplies'


class ItemsDeviceprocessors(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceprocessors = models.ForeignKey(
        Deviceprocessors, on_delete=models.CASCADE, blank=True, null=True)
    frequency = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    nbcores = models.IntegerField(blank=True, null=True)
    nbthreads = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_deviceprocessors'


class ItemsDevicesensors(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesensors = models.ForeignKey(
        Devicesensors, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicesensors'


class Linetypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'linetypes'


class Lineoperators(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    mcc = models.IntegerField(blank=True, null=True)
    mnc = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lineoperators'
        unique_together = (('mcc', 'mnc'),)


class Lines(models.Model):
    name = models.CharField(max_length=255)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    caller_num = models.CharField(max_length=255)
    caller_name = models.CharField(max_length=255)
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    lineoperators = models.ForeignKey(
        Lineoperators, on_delete=models.CASCADE, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    linetypes = models.ForeignKey(
        Linetypes, on_delete=models.CASCADE, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lines'


class ItemsDevicesimcards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    devicesimcards = models.ForeignKey(
        Devicesimcards, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    lines = models.ForeignKey(
        Lines, on_delete=models.CASCADE, blank=True, null=True)
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    pin = models.CharField(max_length=255)
    pin2 = models.CharField(max_length=255)
    puk = models.CharField(max_length=255)
    puk2 = models.CharField(max_length=255)
    msin = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'items_devicesimcards'


class ItemsDevicesoundcards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesoundcards = models.ForeignKey(
        Devicesoundcards, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_devicesoundcards'


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


class Passivedcequipmenttypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'passivedcequipmenttypes'


class Passivedcequipments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    passivedcequipmentmodels = models.ForeignKey(
        Passivedcequipmentmodels, on_delete=models.CASCADE, blank=True, null=True)
    passivedcequipmenttypes = models.ForeignKey(
        Passivedcequipmenttypes, on_delete=models.CASCADE, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='passivedcequipments_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='passivedcequipments_groups_tech')
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'passivedcequipments'


class EntitiesKnowbaseitems(models.Model):
    knowbaseitems = models.PositiveIntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'entities_knowbaseitems'


class EntitiesReminders(models.Model):
    reminders = models.PositiveIntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'entities_reminders'


class EntitiesRssfeeds(models.Model):
    rssfeeds = models.PositiveIntegerField()
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'entities_rssfeeds'


class Fqdns(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdn = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fqdns'


class Networknames(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    fqdns = models.ForeignKey(
        Fqdns, on_delete=models.CASCADE, blank=True, null=True)
    ipnetworks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networknames'


class Networkaliases(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    networknames = models.ForeignKey(
        Networknames, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdns = models.ForeignKey(
        Fqdns, on_delete=models.CASCADE, blank=True, null=True)
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


class Networkportaggregates(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    networkports_list = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportaggregates'


class Networkportaliases(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    networkports_alias = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportaliases'


class Networkportconnectionlogs(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    connected = models.IntegerField()
    networkports_source = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    networkports_destination = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, related_name='networkportconnectionlogs_networkports_destination')

    class Meta:
        managed = True
        db_table = 'networkportconnectionlogs'


class Networkportdialups(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportdialups'


class Networkportethernets(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    items_devicenetworkcards = models.ForeignKey(
        ItemsDevicenetworkcards, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportethernets'


class Networkportfiberchanneltypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportfiberchanneltypes'


class Networkportfiberchannels(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    items_devicenetworkcards = models.ForeignKey(
        ItemsDevicenetworkcards, on_delete=models.CASCADE, blank=True, null=True)
    networkportfiberchanneltypes = models.ForeignKey(
        Networkportfiberchanneltypes, on_delete=models.CASCADE, blank=True, null=True)
    wwn = models.CharField(max_length=16, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportfiberchannels'


class Networkportlocals(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
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
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportmetrics'
        unique_together = (('networkports_id', 'date'),)


class NetworkportsNetworkports(models.Model):
    networkports_1 = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, related_name='networkportsnetworkports_networkports_1')
    networkports_2 = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, related_name='networkportsnetworkports_networkports_2')

    class Meta:
        managed = True
        db_table = 'networkports_networkports'
        unique_together = (('networkports_1', 'networkports_2'),)


class Vlans(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    tag = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vlans'


class NetworkportsVlans(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    vlans = models.ForeignKey(
        Vlans, on_delete=models.CASCADE, blank=True, null=True)
    tagged = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'networkports_vlans'
        unique_together = (('networkports_id', 'vlans_id'),)


class Networkporttypes(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    is_recursive = models.IntegerField()
    value_decimal = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_importable = models.IntegerField()
    instantiation_type = models.CharField(
        max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkporttypes'


class Networkportwifis(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True)
    items_devicenetworkcards = models.ForeignKey(
        ItemsDevicenetworkcards, on_delete=models.CASCADE, blank=True, null=True)
    wifinetworks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True)
    networkportwifis = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='networkportwifis_networkportwifis')
    version = models.CharField(max_length=20, blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportwifis'


class Computers(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='computers_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='computers_groups_tech')
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True)
    computermodels = models.ForeignKey(
        Computermodels, on_delete=models.CASCADE, blank=True, null=True)
    computertypes = models.ForeignKey(
        Computertypes, on_delete=models.CASCADE, blank=True, null=True)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()
    last_inventory_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'computers'


class Monitors(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True, related_name='monitors_users_tech')
    groups_tech = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True, related_name='monitors_groups_tech')
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
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True)
    monitortypes = models.ForeignKey(
        Monitortypes, on_delete=models.CASCADE, blank=True, null=True)
    monitormodels = models.ForeignKey(
        Monitormodels, on_delete=models.CASCADE, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        assistanceModels.Users, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ForeignKey(
        assistanceModels.Groups, on_delete=models.CASCADE, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'monitors'


class ComputersItems(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    computers = models.ForeignKey(
        Computers, on_delete=models.CASCADE, blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'computers_items'
