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