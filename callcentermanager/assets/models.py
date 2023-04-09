from django.db import models
from assistance import models as assistanceModels
from django.contrib.auth.models import AbstractUser, Group


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
    snmpversion = models.CharField(max_length=8, blank=True, null=True)
    community = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    authentication = models.CharField(max_length=255, blank=True, null=True)
    auth_passphrase = models.CharField(max_length=255, blank=True, null=True)
    encryption = models.CharField(max_length=255, blank=True, null=True)
    priv_passphrase = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'snmpcredentials'


class Authldaps(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    basedn = models.CharField(max_length=255, blank=True, null=True)
    rootdn = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField(default=0)
    condition = models.TextField(blank=True, null=True)
    login_field = models.CharField(max_length=255, blank=True, null=True)
    sync_field = models.CharField(max_length=255, blank=True, null=True)
    use_tls = models.IntegerField(default=0)
    group_field = models.CharField(max_length=255, blank=True, null=True)
    group_condition = models.TextField(blank=True, null=True)
    group_search_type = models.IntegerField(default=0)
    group_member_field = models.CharField(
        max_length=255, blank=True, null=True)
    email1_field = models.CharField(max_length=255, blank=True, null=True)
    realname_field = models.CharField(max_length=255, blank=True, null=True)
    firstname_field = models.CharField(max_length=255, blank=True, null=True)
    phone_field = models.CharField(max_length=255, blank=True, null=True)
    phone2_field = models.CharField(max_length=255, blank=True, null=True)
    mobile_field = models.CharField(max_length=255, blank=True, null=True)
    comment_field = models.CharField(max_length=255, blank=True, null=True)
    use_dn = models.IntegerField(default=0)
    time_offset = models.IntegerField(default=0)
    deref_option = models.IntegerField(default=0)
    title_field = models.CharField(max_length=255, blank=True, null=True)
    category_field = models.CharField(max_length=255, blank=True, null=True)
    language_field = models.CharField(max_length=255, blank=True, null=True)
    entity_field = models.CharField(max_length=255, blank=True, null=True)
    entity_condition = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_default = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    rootdn_passwd = models.CharField(max_length=255, blank=True, null=True)
    registration_number_field = models.CharField(
        max_length=255, blank=True, null=True)
    email2_field = models.CharField(max_length=255, blank=True, null=True)
    email3_field = models.CharField(max_length=255, blank=True, null=True)
    email4_field = models.CharField(max_length=255, blank=True, null=True)
    location_field = models.CharField(max_length=255, blank=True, null=True)
    responsible_field = models.CharField(max_length=255, blank=True, null=True)
    pagesize = models.IntegerField(default=0)
    ldap_maxlimit = models.IntegerField(default=0)
    can_support_pagesize = models.IntegerField(default=0)
    picture_field = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    inventory_domain = models.CharField(max_length=255, blank=True, null=True)
    tls_certfile = models.TextField(blank=True, null=True)
    tls_keyfile = models.TextField(blank=True, null=True)
    use_bind = models.IntegerField(default=0)
    timeout = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'authldaps'


class Entities(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='entities_entities')
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
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
        Authldaps, on_delete=models.CASCADE, blank=True, null=True, default=None)
    mail_domain = models.CharField(max_length=255, blank=True, null=True)
    entity_ldapfilter = models.TextField(blank=True, null=True)
    mailing_signature = models.TextField(blank=True, null=True)
    cartridges_alert_repeat = models.IntegerField(default=0)
    consumables_alert_repeat = models.IntegerField(default=0)
    use_licenses_alert = models.IntegerField(default=0)
    send_licenses_alert_before_delay = models.IntegerField(default=0)
    use_certificates_alert = models.IntegerField(default=0)
    send_certificates_alert_before_delay = models.IntegerField(default=0)
    certificates_alert_repeat_interval = models.IntegerField(default=0)
    use_contracts_alert = models.IntegerField(default=0)
    send_contracts_alert_before_delay = models.IntegerField(default=0)
    use_infocoms_alert = models.IntegerField(default=0)
    send_infocoms_alert_before_delay = models.IntegerField(default=0)
    use_reservations_alert = models.IntegerField(default=0)
    use_domains_alert = models.IntegerField(default=0)
    send_domains_alert_close_expiries_delay = models.IntegerField(default=0)
    send_domains_alert_expired_delay = models.IntegerField(default=0)
    autoclose_delay = models.IntegerField(default=0)
    autopurge_delay = models.IntegerField(default=0)
    notclosed_delay = models.IntegerField(default=0)
    calendars_strategy = models.IntegerField(default=0)
    calendars = models.ForeignKey(
        assistanceModels.Calendars, on_delete=models.CASCADE, blank=True, null=True, default=None)
    auto_assign_mode = models.IntegerField(default=0)
    tickettype = models.IntegerField(default=0)
    max_closedate = models.DateTimeField(blank=True, null=True)
    inquest_config = models.IntegerField(default=0)
    inquest_rate = models.IntegerField(default=0)
    inquest_delay = models.IntegerField(default=0)
    # Field name made lowercase.
    inquest_url = models.CharField(
        db_column='inquest_URL', max_length=255, blank=True, null=True)
    autofill_warranty_date = models.CharField(max_length=255)
    autofill_use_date = models.CharField(max_length=255)
    autofill_buy_date = models.CharField(max_length=255)
    autofill_delivery_date = models.CharField(max_length=255)
    autofill_order_date = models.CharField(max_length=255)
    tickettemplates_strategy = models.IntegerField(default=0)
    tickettemplates = models.ForeignKey(
        assistanceModels.Tickettemplates, on_delete=models.CASCADE, blank=True, null=True, default=None)
    changetemplates_strategy = models.IntegerField(default=0)
    changetemplates = models.PositiveIntegerField(blank=True, null=True)
    problemtemplates_strategy = models.IntegerField(default=0)
    problemtemplates = models.PositiveIntegerField(blank=True, null=True)
    entities_strategy_software = models.IntegerField(default=0)
    entities_software = models.PositiveIntegerField(blank=True, null=True)
    default_contract_alert = models.IntegerField(default=0)
    default_infocom_alert = models.IntegerField(default=0)
    default_cartridges_alarm_threshold = models.IntegerField(default=0)
    default_consumables_alarm_threshold = models.IntegerField(default=0)
    delay_send_emails = models.IntegerField(default=0)
    is_notif_enable_default = models.IntegerField(default=0)
    inquest_duration = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    autofill_decommission_date = models.CharField(max_length=255)
    suppliers_as_private = models.IntegerField(default=0)
    anonymize_support_agents = models.IntegerField(default=0)
    display_users_initials = models.IntegerField(default=0)
    contracts_strategy_default = models.IntegerField(default=0)
    contracts_default = models.PositiveIntegerField(blank=True, null=True)
    enable_custom_css = models.IntegerField(default=0)
    custom_css_code = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    altitude = models.CharField(max_length=255, blank=True, null=True)
    transfers_strategy = models.IntegerField(default=0)
    transfers = models.PositiveIntegerField(blank=True, null=True)
    agent_base_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'entities'
        unique_together = (('entities_id', 'name'),)


class Locations(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='locations_locations')
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
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



class Groups(Group):
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    ldap_field = models.CharField(max_length=255, blank=True, null=True)
    ldap_value = models.TextField(blank=True, null=True)
    ldap_group_dn = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_requester = models.IntegerField(blank=True, null=True)
    is_watcher = models.IntegerField(blank=True, null=True)
    is_assign = models.IntegerField(blank=True, null=True)
    is_task = models.IntegerField(blank=True, null=True)
    is_notify = models.IntegerField(blank=True, null=True)
    is_itemgroup = models.IntegerField(blank=True, null=True)
    is_usergroup = models.IntegerField(blank=True, null=True)
    is_manager = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'groups'


class Users(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    password_last_update = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    language = models.CharField(max_length=10, blank=True, null=True)
    use_mode = models.IntegerField(blank=True, null=True)
    list_limit = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    auths_id = models.PositiveIntegerField(blank=True, null=True)
    authtype = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_sync = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    profiles_id = models.PositiveIntegerField(blank=True, null=True)
    entities_id = models.PositiveIntegerField(blank=True, null=True)
    usertitles_id = models.PositiveIntegerField(blank=True, null=True)
    usercategories_id = models.PositiveIntegerField(blank=True, null=True)
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
    default_requesttypes_id = models.PositiveIntegerField(
        blank=True, null=True)
    password_forget_token = models.CharField(
        max_length=40, blank=True, null=True)
    password_forget_token_date = models.DateTimeField(blank=True, null=True)
    user_dn = models.TextField(blank=True, null=True)
    registration_number = models.CharField(
        max_length=255, blank=True, null=True)
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
    duedatewarning_color = models.CharField(
        max_length=255, blank=True, null=True)
    duedatecritical_color = models.CharField(
        max_length=255, blank=True, null=True)
    duedatewarning_less = models.IntegerField(blank=True, null=True)
    duedatecritical_less = models.IntegerField(blank=True, null=True)
    duedatewarning_unit = models.CharField(
        max_length=255, blank=True, null=True)
    duedatecritical_unit = models.CharField(
        max_length=255, blank=True, null=True)
    display_options = models.TextField(blank=True, null=True)
    is_deleted_ldap = models.IntegerField(blank=True, null=True)
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
    groups_id = models.PositiveIntegerField(blank=True, null=True)
    users_id_supervisor = models.PositiveIntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True, null=True)
    default_dashboard_central = models.CharField(
        max_length=100, blank=True, null=True)
    default_dashboard_assets = models.CharField(
        max_length=100, blank=True, null=True)
    default_dashboard_helpdesk = models.CharField(
        max_length=100, blank=True, null=True)
    default_dashboard_mini_ticket = models.CharField(
        max_length=100, blank=True, null=True)
    default_central_tab = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'
        unique_together = (('name', 'authtype', 'auths_id'),)



class States(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    states = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='states_states')
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_visible_computer = models.IntegerField(default=0)
    is_visible_monitor = models.IntegerField(default=0)
    is_visible_networkequipment = models.IntegerField(default=0)
    is_visible_peripheral = models.IntegerField(default=0)
    is_visible_phone = models.IntegerField(default=0)
    is_visible_printer = models.IntegerField(default=0)
    is_visible_softwareversion = models.IntegerField(default=0)
    is_visible_softwarelicense = models.IntegerField(default=0)
    is_visible_line = models.IntegerField(default=0)
    is_visible_certificate = models.IntegerField(default=0)
    is_visible_rack = models.IntegerField(default=0)
    is_visible_passivedcequipment = models.IntegerField(default=0)
    is_visible_enclosure = models.IntegerField(default=0)
    is_visible_pdu = models.IntegerField(default=0)
    is_visible_cluster = models.IntegerField(default=0)
    is_visible_contract = models.IntegerField(default=0)
    is_visible_appliance = models.IntegerField(default=0)
    is_visible_databaseinstance = models.IntegerField(default=0)
    is_visible_cable = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'states'
        unique_together = (('states_id', 'name'),)


class Softwarecategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    softwarecategories = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwarecategories_softwarecategories')
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwarecategories'


class Softwares(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwares_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwares_groups_tech')
    is_update = models.IntegerField(default=0)
    softwares = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwares_softwares')
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_helpdesk_visible = models.IntegerField(default=0)
    softwarecategories = models.ForeignKey(
        Softwarecategories, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_valid = models.IntegerField(default=0)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwares'


class Networkequipmentmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)
    required_units = models.IntegerField(default=0)
    depth = models.FloatField()
    power_connections = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    is_half_rack = models.IntegerField(default=0)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='networkequipments_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='networkequipments_groups_tech')
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkequipmenttypes = models.ForeignKey(
        Networkequipmenttypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkequipmentmodels = models.ForeignKey(
        Networkequipmentmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField(default=0)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    sysdescr = models.TextField(blank=True, null=True)
    cpu = models.IntegerField(default=0)
    uptime = models.CharField(max_length=255)
    last_inventory_update = models.DateTimeField(blank=True, null=True)
    snmpcredentials = models.ForeignKey(
        Snmpcredentials, on_delete=models.CASCADE, blank=True, null=True, default=None)

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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='printers_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='printers_groups_tech')
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    have_serial = models.IntegerField(default=0)
    have_parallel = models.IntegerField(default=0)
    have_usb = models.IntegerField(default=0)
    have_wifi = models.IntegerField(default=0)
    have_ethernet = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    memory_size = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    printertypes = models.ForeignKey(
        Printertypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    printermodels = models.ForeignKey(
        Printermodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_global = models.IntegerField(default=0)
    is_deleted = models.IntegerField(default=0)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    init_pages_counter = models.IntegerField(default=0)
    last_pages_counter = models.IntegerField(default=0)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField(default=0)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    sysdescr = models.TextField(blank=True, null=True)
    last_inventory_update = models.DateTimeField(blank=True, null=True)
    snmpcredentials = models.ForeignKey(
        Snmpcredentials, on_delete=models.CASCADE, blank=True, null=True, default=None)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'printers'


class Cartridgeitemtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cartridgeitemtypes'
class Cartridgeitems(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    cartridgeitemtypes = models.ForeignKey(
        Cartridgeitemtypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='cartridgeitems_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='cartridgeitems_groups_tech')
    is_deleted = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField(default=0)
    stock_target = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cartridgeitems'


class Cartridges(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    cartridgeitems = models.ForeignKey(
        Cartridgeitems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    printers = models.ForeignKey(
        Printers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_in = models.DateField(blank=True, null=True)
    date_use = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    pages = models.IntegerField(default=0)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    consumableitemtypes = models.ForeignKey(
        Consumableitemtypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='consumableitems_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='consumableitems_groups_tech')
    is_deleted = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField(default=0)
    stock_target = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'consumableitems'


class Consumables(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    consumableitems = models.ForeignKey(
        Consumableitems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items = models.ForeignKey(
        Cartridgeitems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'consumables'


class Datacenters(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'datacenters'


class Dcrooms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    vis_cols = models.IntegerField(blank=True, null=True)
    vis_rows = models.IntegerField(blank=True, null=True)
    blueprint = models.TextField(blank=True, null=True)
    datacenters = models.ForeignKey(
        Datacenters, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dcrooms'


class Racks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    rackmodels = models.ForeignKey(
        Rackmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    racktypes = models.ForeignKey(
        Racktypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='racks_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='racks_groups_tech')
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    number_units = models.IntegerField(blank=True, null=True)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    dcrooms = models.ForeignKey(
        Dcrooms, on_delete=models.CASCADE, blank=True, null=True, default=None)
    room_orientation = models.IntegerField(default=0)
    position = models.CharField(max_length=50, blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    max_power = models.IntegerField(default=0)
    mesured_power = models.IntegerField(default=0)
    max_weight = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'racks'


class Enclosuremodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)
    required_units = models.IntegerField(default=0)
    depth = models.FloatField()
    power_connections = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    is_half_rack = models.IntegerField(default=0)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    enclosuremodels = models.ForeignKey(
        Enclosuremodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='enclosures_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='enclosures_groups_tech')
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    orientation = models.IntegerField(blank=True, null=True)
    power_supplies = models.IntegerField(default=0)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enclosures'


class Pdutypes(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
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
    weight = models.IntegerField(default=0)
    required_units = models.IntegerField(default=0)
    depth = models.FloatField()
    power_connections = models.IntegerField(default=0)
    max_power = models.IntegerField(default=0)
    is_half_rack = models.IntegerField(default=0)
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    is_rackable = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdumodels'


class Pdus(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    pdumodels = models.ForeignKey(
        Pdumodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='pdus_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='pdus_groups_tech')
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    pdutypes = models.ForeignKey(
        Pdutypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdus'


class Unmanageds(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_dynamic = models.IntegerField(default=0)
    date_creation = models.DateTimeField(blank=True, null=True)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    sysdescr = models.TextField(blank=True, null=True)
    domains = models.ForeignKey(
        assistanceModels.Domains, on_delete=models.CASCADE, blank=True, null=True, default=None)
    agents = models.ForeignKey(
        assistanceModels.Agents, on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    accepted = models.IntegerField(default=0)
    hub = models.IntegerField(default=0)
    ip = models.CharField(max_length=255, blank=True, null=True)
    snmpcredentials = models.ForeignKey(
        Snmpcredentials, on_delete=models.CASCADE, blank=True, null=True, default=None)

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
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=100)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    logical_number = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    instantiation_type = models.CharField(
        max_length=255, blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    ifmtu = models.IntegerField(default=0)
    ifspeed = models.BigIntegerField(blank=True, null=True)
    ifinternalstatus = models.CharField(max_length=255, blank=True, null=True)
    ifconnectionstatus = models.IntegerField(default=0)
    iflastchange = models.CharField(max_length=255, blank=True, null=True)
    ifinbytes = models.BigIntegerField(blank=True, null=True)
    ifinerrors = models.BigIntegerField(blank=True, null=True)
    ifoutbytes = models.BigIntegerField(blank=True, null=True)
    ifouterrors = models.BigIntegerField(blank=True, null=True)
    ifstatus = models.CharField(max_length=255, blank=True, null=True)
    ifdescr = models.CharField(max_length=255, blank=True, null=True)
    ifalias = models.CharField(max_length=255, blank=True, null=True)
    portduplex = models.CharField(max_length=255, blank=True, null=True)
    trunk = models.IntegerField(default=0)
    lastup = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkports'


class Sockets(models.Model):
    position = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    socketmodels = models.ForeignKey(
        Socketmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    wiring_side = models.IntegerField(blank=True, null=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    itemtype_endpoint_a = models.CharField(
        max_length=255, blank=True, null=True)
    itemtype_endpoint_b = models.CharField(
        max_length=255, blank=True, null=True)
    items_endpoint_a = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    items_endpoint_b = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='cables_itemsEndpointB')
    socketmodels_endpoint_a = models.ForeignKey(
        Socketmodels, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='cables_socketModelsItemsEndpointA')
    socketmodels_endpoint_b = models.ForeignKey(
        Socketmodels, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='cables_socketModelsItemsEndpointB')
    sockets_endpoint_a = models.ForeignKey(
        Sockets, on_delete=models.CASCADE, blank=True, null=True, default=None)
    sockets_endpoint_b = models.ForeignKey(
        Sockets, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='cables_socketItemsEndpointA')
    cablestrands = models.ForeignKey(
        Cablestrands, on_delete=models.CASCADE, blank=True, null=True, default=None)
    color = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='cables_users_tech')
    cabletypes = models.ForeignKey(
        Cabletypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    voltage = models.IntegerField(blank=True, null=True)
    devicesimcardtypes = models.ForeignKey(
        Devicesimcardtypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    allow_voip = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'devicesimcards'


class Computermodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)
    required_units = models.IntegerField(default=0)
    depth = models.FloatField()
    power_connections = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    is_half_rack = models.IntegerField(default=0)
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
    weight = models.IntegerField(default=0)
    required_units = models.IntegerField(default=0)
    depth = models.FloatField()
    power_connections = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    is_half_rack = models.IntegerField(default=0)
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
    softwarelicensetypes = models.PositiveIntegerField(blank=True, null=True)
    level = models.IntegerField(default=0)
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    entities = models.PositiveIntegerField(blank=True, null=True)
    is_recursive = models.IntegerField(default=0)
    completename = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwarelicensetypes'


class Softwareversions(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    softwares = models.ForeignKey(
        Softwares, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    arch = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    operatingsystems = models.ForeignKey(
        Operatingsystems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwareversions'


class Softwarelicenses(models.Model):
    softwares = models.ForeignKey(
        Softwares, on_delete=models.CASCADE, blank=True, null=True, default=None)
    softwarelicenses = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwarelicenses_softwarelicenses')
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    softwarelicensetypes = models.ForeignKey(
        Softwarelicensetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    softwareversions_buy = models.ForeignKey(
        Softwareversions, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwarelicenses_softwareversions_buy')
    softwareversions_use = models.ForeignKey(
        Softwareversions, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwarelicenses_softwareversions_use')
    expire = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_valid = models.IntegerField(default=0)
    date_creation = models.DateTimeField(blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwarelicenses_users_tech')
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='softwarelicenses_groups_tech')
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_helpdesk_visible = models.IntegerField(default=0)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    allow_overquota = models.IntegerField(default=0)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwarelicenses'


class PrintersCartridgeinfos(models.Model):
    printers = models.ForeignKey(
        Printers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    property = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'printers_cartridgeinfos'


class CartridgeitemsPrintermodels(models.Model):
    cartridgeitems = models.ForeignKey(
        Cartridgeitems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    printermodels = models.ForeignKey(
        Printermodels, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'cartridgeitems_printermodels'
        unique_together = (('printermodels_id', 'cartridgeitems_id'),)


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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='phones_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='phones_groups_tech')
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    phonetypes = models.ForeignKey(
        Phonetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    phonemodels = models.ForeignKey(
        Phonemodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    brand = models.CharField(max_length=255, blank=True, null=True)
    phonepowersupplies = models.ForeignKey(
        Phonepowersupplies, on_delete=models.CASCADE, blank=True, null=True, default=None)
    number_line = models.CharField(max_length=255, blank=True, null=True)
    have_headset = models.IntegerField(default=0)
    have_hp = models.IntegerField(default=0)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_global = models.IntegerField(default=0)
    is_deleted = models.IntegerField(default=0)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField(default=0)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField(default=0)
    last_inventory_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phones'


class ItemsRacks(models.Model):
    racks = models.ForeignKey(
        Racks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    position = models.IntegerField(default=0)
    orientation = models.IntegerField(blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    hpos = models.IntegerField(default=0)
    is_reserved = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'items_racks'
        unique_together = (('itemtype', 'items_id', 'is_reserved'),)


class ItemsEnclosures(models.Model):
    enclosures = models.ForeignKey(
        Enclosures, on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    position = models.IntegerField(default=0)

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
        Plugs, on_delete=models.CASCADE, blank=True, null=True, default=None)
    pdus = models.ForeignKey(
        Pdus, on_delete=models.CASCADE, blank=True, null=True, default=None)
    number_plugs = models.IntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdus_plugs'


class PdusRacks(models.Model):
    racks = models.ForeignKey(
        Racks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    pdus = models.ForeignKey(
        Pdus, on_delete=models.CASCADE, blank=True, null=True, default=None)
    side = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(default=0)
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
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    voltage = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    devicebatterytypes = models.ForeignKey(
        Devicebatterytypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicebatterymodels = models.ForeignKey(
        Devicebatterymodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
    flashunit = models.IntegerField(default=0)
    lensfacing = models.CharField(max_length=255, blank=True, null=True)
    orientation = models.CharField(max_length=255, blank=True, null=True)
    focallength = models.CharField(max_length=255, blank=True, null=True)
    sensorsize = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicecameramodels = models.ForeignKey(
        Devicecameramodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Devicecasetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicecasemodels = models.ForeignKey(
        Devicecasemodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
    is_raid = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    interfacetypes = models.ForeignKey(
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicecontrolmodels = models.ForeignKey(
        Devicecontrolmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
    is_writer = models.IntegerField(default=0)
    speed = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    interfacetypes = models.ForeignKey(
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicedrivemodels = models.ForeignKey(
        Devicedrivemodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwaretypes = models.ForeignKey(
        Devicefirmwaretypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicefirmwaremodels = models.ForeignKey(
        Devicefirmwaremodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Devicegenerictypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    devicegenericmodels = models.ForeignKey(
        Devicegenericmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    memory_default = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicegraphiccardmodels = models.ForeignKey(
        Devicegraphiccardmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Interfacetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    cache = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    capacity_default = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    deviceharddrivemodels = models.ForeignKey(
        Deviceharddrivemodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    size_default = models.IntegerField(default=0)
    devicememorytypes = models.ForeignKey(
        Devicememorytypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicememorymodels = models.ForeignKey(
        Devicememorymodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicememories'


class Peripheralmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)
    required_units = models.IntegerField(default=0)
    depth = models.FloatField()
    power_connections = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    is_half_rack = models.IntegerField(default=0)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='peripherals_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='peripherals_groups_tech')
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    peripheraltypes = models.ForeignKey(
        Peripheraltypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    peripheralmodels = models.ForeignKey(
        Peripheralmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    brand = models.CharField(max_length=255, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_global = models.IntegerField(default=0)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField(default=0)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField(default=0)

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
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicemotherboardmodels = models.ForeignKey(
        Devicemotherboardmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    mac_default = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicenetworkcardmodels = models.ForeignKey(
        Devicenetworkcardmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    devicenetworkcardmodels = models.ForeignKey(
        Devicenetworkcardmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicepcimodels = models.ForeignKey(
        Devicepcimodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
    is_atx = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicepowersupplymodels = models.ForeignKey(
        Devicepowersupplymodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicepowersupplies'


class Deviceprocessors(models.Model):
    designation = models.CharField(max_length=255, blank=True, null=True)
    frequence = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    frequency_default = models.IntegerField(default=0)
    nbcores_default = models.IntegerField(blank=True, null=True)
    nbthreads_default = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    deviceprocessormodels = models.ForeignKey(
        Deviceprocessormodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Devicesensortypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    devicesensormodels = models.ForeignKey(
        Devicesensormodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    devicesoundcardmodels = models.ForeignKey(
        Devicesoundcardmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesoundcards'


class ItemsDevicebatteries(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicebatteries = models.ForeignKey(
        Devicebatteries, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturing_date = models.DateField(blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    real_capacity = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'items_devicebatteries'


class ItemsDevicecameras(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecameras = models.ForeignKey(
        Devicecameras, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'items_devicecameras'


class Imageformats(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'imageformats'


class Imageresolutions(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    is_video = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'imageresolutions'


class ItemsDevicecamerasImageformats(models.Model):
    item_devicecameras = models.ForeignKey(
        ItemsDevicecameras, on_delete=models.CASCADE, blank=True, null=True, default=None)
    imageformats = models.ForeignKey(
        Imageformats, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_dynamic = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'items_devicecameras_imageformats'


class ItemsDevicecamerasImageresolutions(models.Model):
    item_devicecameras = models.ForeignKey(
        ItemsDevicecameras, on_delete=models.CASCADE, blank=True, null=True, default=None)
    imageresolutions = models.ForeignKey(
        Imageresolutions, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_dynamic = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'items_devicecameras_imageresolutions'


class ItemsDevicecases(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecases = models.ForeignKey(
        Devicecases, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicecases'


class ItemsDevicecontrols(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecontrols = models.ForeignKey(
        Devicecontrols, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicecontrols'


class ItemsDevicedrives(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicedrives = models.ForeignKey(
        Devicedrives, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicedrives'


class ItemsDevicefirmwares(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwares = models.ForeignKey(
        Devicefirmwares, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicefirmwares'


class ItemsDevicegenerics(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegenerics = models.ForeignKey(
        Devicegenerics, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicegenerics'


class ItemsDevicegraphiccards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegraphiccards = models.ForeignKey(
        Devicegraphiccards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    memory = models.IntegerField(default=0)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicegraphiccards'


class ItemsDeviceharddrives(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceharddrives = models.ForeignKey(
        Deviceharddrives, on_delete=models.CASCADE, blank=True, null=True, default=None)
    capacity = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_deviceharddrives'


class ItemsDevicememories(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicememories = models.ForeignKey(
        Devicememories, on_delete=models.CASCADE, blank=True, null=True, default=None)
    size = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicememories'


class ItemsDevicemotherboards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicemotherboards = models.ForeignKey(
        Devicemotherboards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicemotherboards'


class ItemsDevicenetworkcards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicenetworkcards = models.ForeignKey(
        Devicenetworkcards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    mac = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicenetworkcards'


class ItemsDevicepcis(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepcis = models.ForeignKey(
        Devicepcis, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicepcis'


class ItemsDevicepowersupplies(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepowersupplies = models.ForeignKey(
        Devicepowersupplies, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicepowersupplies'


class ItemsDeviceprocessors(models.Model):
    items_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceprocessors = models.ForeignKey(
        Deviceprocessors, on_delete=models.CASCADE, blank=True, null=True, default=None)
    frequency = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    nbcores = models.IntegerField(blank=True, null=True)
    nbthreads = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_deviceprocessors'


class ItemsDevicesensors(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesensors = models.ForeignKey(
        Devicesensors, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lineoperators'
        unique_together = (('mcc', 'mnc'),)


class Lines(models.Model):
    name = models.CharField(max_length=255)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    is_deleted = models.IntegerField(default=0)
    caller_num = models.CharField(max_length=255)
    caller_name = models.CharField(max_length=255)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    lineoperators = models.ForeignKey(
        Lineoperators, on_delete=models.CASCADE, blank=True, null=True, default=None)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    linetypes = models.ForeignKey(
        Linetypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lines'


class ItemsDevicesimcards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=100)
    devicesimcards = models.ForeignKey(
        Devicesimcards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    lines = models.ForeignKey(
        Lines, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    pin = models.CharField(max_length=255)
    pin2 = models.CharField(max_length=255)
    puk = models.CharField(max_length=255)
    puk2 = models.CharField(max_length=255)
    msin = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'items_devicesimcards'


class ItemsDevicesoundcards(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesoundcards = models.ForeignKey(
        Devicesoundcards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    serial = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    busid = models.CharField(
        db_column='busID', max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'items_devicesoundcards'


class Passivedcequipmentmodels(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(default=0)
    required_units = models.IntegerField(default=0)
    depth = models.FloatField()
    power_connections = models.IntegerField(default=0)
    power_consumption = models.IntegerField(default=0)
    is_half_rack = models.IntegerField(default=0)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    passivedcequipmentmodels = models.ForeignKey(
        Passivedcequipmentmodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    passivedcequipmenttypes = models.ForeignKey(
        Passivedcequipmenttypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='passivedcequipments_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='passivedcequipments_groups_tech')
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'passivedcequipments'


class EntitiesKnowbaseitems(models.Model):
    knowbaseitems = models.PositiveIntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'entities_knowbaseitems'


class EntitiesReminders(models.Model):
    reminders = models.PositiveIntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'entities_reminders'


class EntitiesRssfeeds(models.Model):
    rssfeeds = models.PositiveIntegerField(blank=True, null=True)
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'entities_rssfeeds'


class Fqdns(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
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
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    fqdns = models.ForeignKey(
        Fqdns, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ipnetworks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networknames'


class Networkaliases(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networknames = models.ForeignKey(
        Networknames, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdns = models.ForeignKey(
        Fqdns, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkports_list = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportaggregates'


class Networkportaliases(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkports_alias = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportaliases'


class Networkportconnectionlogs(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    connected = models.IntegerField(default=0)
    networkports_source = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkports_destination = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='networkportconnectionlogs_networkports_destination')

    class Meta:
        managed = True
        db_table = 'networkportconnectionlogs'


class Networkportdialups(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportdialups'


class Networkportethernets(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    items_devicenetworkcards = models.ForeignKey(
        ItemsDevicenetworkcards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    type = models.CharField(max_length=10, blank=True, null=True)
    speed = models.IntegerField(default=0)
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
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    items_devicenetworkcards = models.ForeignKey(
        ItemsDevicenetworkcards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkportfiberchanneltypes = models.ForeignKey(
        Networkportfiberchanneltypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    wwn = models.CharField(max_length=16, blank=True, null=True)
    speed = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportfiberchannels'


class Networkportlocals(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportlocals'


class Networkportmetrics(models.Model):
    date = models.DateField(blank=True, null=True)
    ifinbytes = models.BigIntegerField(blank=True, null=True)
    ifinerrors = models.BigIntegerField(blank=True, null=True)
    ifoutbytes = models.BigIntegerField(blank=True, null=True)
    ifouterrors = models.BigIntegerField(blank=True, null=True)
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportmetrics'
        unique_together = (('networkports_id', 'date'),)


class NetworkportsNetworkports(models.Model):
    networkports_1 = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='networkportsnetworkports_networkports_1')
    networkports_2 = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='networkportsnetworkports_networkports_2')

    class Meta:
        managed = True
        db_table = 'networkports_networkports'
        unique_together = (('networkports_1', 'networkports_2'),)


class Vlans(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    tag = models.IntegerField(default=0)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vlans'


class NetworkportsVlans(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    vlans = models.ForeignKey(
        Vlans, on_delete=models.CASCADE, blank=True, null=True, default=None)
    tagged = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'networkports_vlans'
        unique_together = (('networkports_id', 'vlans_id'),)


class Networkporttypes(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_recursive = models.IntegerField(default=0)
    value_decimal = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_importable = models.IntegerField(default=0)
    instantiation_type = models.CharField(
        max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkporttypes'


class Networkportwifis(models.Model):
    networkports = models.ForeignKey(
        Networkports, on_delete=models.CASCADE, blank=True, null=True, default=None)
    items_devicenetworkcards = models.ForeignKey(
        ItemsDevicenetworkcards, on_delete=models.CASCADE, blank=True, null=True, default=None)
    wifinetworks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networkportwifis = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='networkportwifis_networkportwifis')
    version = models.CharField(max_length=20, blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'networkportwifis'


class Computers(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='computers_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='computers_groups_tech')
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    networks = models.ForeignKey(
        Networks, on_delete=models.CASCADE, blank=True, null=True, default=None)
    computermodels = models.ForeignKey(
        Computermodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    computertypes = models.ForeignKey(
        Computertypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField(default=0)
    last_inventory_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'computers'


class Monitors(models.Model):
    entities = models.ForeignKey(
        Entities, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_tech = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='monitors_users_tech')
    groups_tech = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='monitors_groups_tech')
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    size = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    have_micro = models.IntegerField(default=0)
    have_speaker = models.IntegerField(default=0)
    have_subd = models.IntegerField(default=0)
    have_bnc = models.IntegerField(default=0)
    have_dvi = models.IntegerField(default=0)
    have_pivot = models.IntegerField(default=0)
    have_hdmi = models.IntegerField(default=0)
    have_displayport = models.IntegerField(default=0)
    locations = models.ForeignKey(
        Locations, on_delete=models.CASCADE, blank=True, null=True, default=None)
    monitortypes = models.ForeignKey(
        Monitortypes, on_delete=models.CASCADE, blank=True, null=True, default=None)
    monitormodels = models.ForeignKey(
        Monitormodels, on_delete=models.CASCADE, blank=True, null=True, default=None)
    manufacturers = models.ForeignKey(
        Manufacturers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_deleted = models.IntegerField(default=0)
    is_global = models.IntegerField(default=0)
    is_template = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True, default=None)
    groups = models.ForeignKey(
        Groups, on_delete=models.CASCADE, blank=True, null=True, default=None)
    states = models.ForeignKey(
        States, on_delete=models.CASCADE, blank=True, null=True, default=None)
    ticket_tco = models.DecimalField(
        max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField(default=0)
    autoupdatesystems = models.ForeignKey(
        Autoupdatesystems, on_delete=models.CASCADE, blank=True, null=True, default=None)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'monitors'


class ComputersItems(models.Model):
    items = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    computers = models.ForeignKey(
        Computers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    is_dynamic = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'computers_items'

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
    date_install = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'items_softwareversions'
        unique_together = (('itemtype', 'items_id', 'softwareversions_id'),)