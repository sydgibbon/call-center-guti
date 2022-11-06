from django.db import models

class Computers(models.Model):
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
        managed = True
        db_table = 'computers'


class Monitors(models.Model):
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
        managed = True
        db_table = 'monitors'


class Softwares(models.Model):
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
        managed = True
        db_table = 'softwares'   


class Networkequipments(models.Model):
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
        managed = True
        db_table = 'networkequipments'


class Printers(models.Model):
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
        managed = True
        db_table = 'printers'


class Cartridges(models.Model):
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
        managed = True
        db_table = 'cartridges'


class Consumables(models.Model):
    entities_id = models.PositiveIntegerField()
    consumableitems_id = models.PositiveIntegerField()
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.PositiveIntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'consumables'


class Phones(models.Model):
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
        managed = True
        db_table = 'phones'


class Racks(models.Model):
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
        managed = True
        db_table = 'racks'


class Enclosures(models.Model):
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
        managed = True
        db_table = 'enclosures'


class Pdus(models.Model):
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
        managed = True
        db_table = 'pdus'


class Unmanageds(models.Model):
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
        managed = True
        db_table = 'unmanageds'


class Cables(models.Model):
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
        managed = True
        db_table = 'cables'


class Devicesimcards(models.Model):
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


class ComputersItems(models.Model):
    items_id = models.PositiveIntegerField()
    computers_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=100)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'computers_items'


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


class Softwarecategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    softwarecategories_id = models.PositiveIntegerField()
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'softwarecategories'



class Softwarelicenses(models.Model):
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
        managed = True
        db_table = 'softwarelicenses'


class Softwareversions(models.Model):
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
        managed = True
        db_table = 'softwareversions'


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


class PrintersCartridgeinfos(models.Model):
    printers_id = models.PositiveIntegerField()
    property = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'printers_cartridgeinfos'


class Cartridgeitems(models.Model):
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
        managed = True
        db_table = 'cartridgeitems'


class CartridgeitemsPrintermodels(models.Model):
    cartridgeitems_id = models.PositiveIntegerField()
    printermodels_id = models.PositiveIntegerField()

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


class Consumableitems(models.Model):
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
        managed = True
        db_table = 'consumableitems'


class Consumableitemtypes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'consumableitemtypes'


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


class ItemsRacks(models.Model):
    racks_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255)
    items_id = models.PositiveIntegerField()
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
    enclosures_id = models.PositiveIntegerField()
    itemtype = models.CharField(max_length=255)
    items_id = models.PositiveIntegerField()
    position = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'items_enclosures'
        unique_together = (('itemtype', 'items_id'),)


class PdusPlugs(models.Model):
    plugs_id = models.PositiveIntegerField()
    pdus_id = models.PositiveIntegerField()
    number_plugs = models.IntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdus_plugs'


class PdusRacks(models.Model):
    racks_id = models.PositiveIntegerField()
    pdus_id = models.PositiveIntegerField()
    side = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pdus_racks'


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


class Devicesimcardtypes(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'devicesimcardtypes'


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

class Devicecases(models.Model): # Hasta aqui - Guty
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

class Devicecontrolmodels(models.Model): #hasta aca FRANNNNN
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