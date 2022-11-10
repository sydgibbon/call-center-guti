# Generated by Django 4.0.5 on 2022-11-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_passivedcequipmentmodels_passivedcequipments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autoupdatesystems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'autoupdatesystems',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EntitiesKnowbaseitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowbaseitems_id', models.PositiveIntegerField()),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
            ],
            options={
                'db_table': 'entities_knowbaseitems',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EntitiesReminders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminders_id', models.PositiveIntegerField()),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
            ],
            options={
                'db_table': 'entities_reminders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EntitiesRssfeeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rssfeeds_id', models.PositiveIntegerField()),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
            ],
            options={
                'db_table': 'entities_rssfeeds',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'manufacturers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkaliases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entities_id', models.PositiveIntegerField()),
                ('networknames_id', models.PositiveIntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('fqdns_id', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkaliases',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkinterfaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkinterfaces',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networknames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entities_id', models.PositiveIntegerField()),
                ('items_id', models.PositiveIntegerField()),
                ('itemtype', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('fqdns_id', models.PositiveIntegerField()),
                ('ipnetworks_id', models.PositiveIntegerField()),
                ('is_deleted', models.IntegerField()),
                ('is_dynamic', models.IntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networknames',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportaggregates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField(unique=True)),
                ('networkports_id_list', models.TextField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportaggregates',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportaliases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField(unique=True)),
                ('networkports_id_alias', models.PositiveIntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportaliases',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportconnectionlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('connected', models.IntegerField()),
                ('networkports_id_source', models.PositiveIntegerField()),
                ('networkports_id_destination', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'networkportconnectionlogs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportdialups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField(unique=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportdialups',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportethernets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField(unique=True)),
                ('items_devicenetworkcards_id', models.PositiveIntegerField()),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('speed', models.IntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportethernets',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportfiberchannels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField(unique=True)),
                ('items_devicenetworkcards_id', models.PositiveIntegerField()),
                ('networkportfiberchanneltypes_id', models.PositiveIntegerField()),
                ('wwn', models.CharField(blank=True, max_length=16, null=True)),
                ('speed', models.IntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportfiberchannels',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportfiberchanneltypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportfiberchanneltypes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportlocals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField(unique=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportlocals',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.PositiveIntegerField()),
                ('itemtype', models.CharField(max_length=100)),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
                ('logical_number', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('instantiation_type', models.CharField(blank=True, max_length=255, null=True)),
                ('mac', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('is_deleted', models.IntegerField()),
                ('is_dynamic', models.IntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
                ('ifmtu', models.IntegerField()),
                ('ifspeed', models.BigIntegerField()),
                ('ifinternalstatus', models.CharField(blank=True, max_length=255, null=True)),
                ('ifconnectionstatus', models.IntegerField()),
                ('iflastchange', models.CharField(blank=True, max_length=255, null=True)),
                ('ifinbytes', models.BigIntegerField()),
                ('ifinerrors', models.BigIntegerField()),
                ('ifoutbytes', models.BigIntegerField()),
                ('ifouterrors', models.BigIntegerField()),
                ('ifstatus', models.CharField(blank=True, max_length=255, null=True)),
                ('ifdescr', models.CharField(blank=True, max_length=255, null=True)),
                ('ifalias', models.CharField(blank=True, max_length=255, null=True)),
                ('portduplex', models.CharField(blank=True, max_length=255, null=True)),
                ('trunk', models.IntegerField()),
                ('lastup', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkports',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkporttypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
                ('value_decimal', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('is_importable', models.IntegerField()),
                ('instantiation_type', models.CharField(blank=True, max_length=255, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkporttypes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networkportwifis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField(unique=True)),
                ('items_devicenetworkcards_id', models.PositiveIntegerField()),
                ('wifinetworks_id', models.PositiveIntegerField()),
                ('networkportwifis_id', models.PositiveIntegerField()),
                ('version', models.CharField(blank=True, max_length=20, null=True)),
                ('mode', models.CharField(blank=True, max_length=20, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportwifis',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Networks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('states_id', models.PositiveIntegerField()),
                ('completename', models.TextField(blank=True, null=True)),
                ('level', models.IntegerField()),
                ('ancestors_cache', models.TextField(blank=True, null=True)),
                ('sons_cache', models.TextField(blank=True, null=True)),
                ('is_visible_computer', models.IntegerField()),
                ('is_visible_monitor', models.IntegerField()),
                ('is_visible_networkequipment', models.IntegerField()),
                ('is_visible_peripheral', models.IntegerField()),
                ('is_visible_phone', models.IntegerField()),
                ('is_visible_printer', models.IntegerField()),
                ('is_visible_softwareversion', models.IntegerField()),
                ('is_visible_softwarelicense', models.IntegerField()),
                ('is_visible_line', models.IntegerField()),
                ('is_visible_certificate', models.IntegerField()),
                ('is_visible_rack', models.IntegerField()),
                ('is_visible_passivedcequipment', models.IntegerField()),
                ('is_visible_enclosure', models.IntegerField()),
                ('is_visible_pdu', models.IntegerField()),
                ('is_visible_cluster', models.IntegerField()),
                ('is_visible_contract', models.IntegerField()),
                ('is_visible_appliance', models.IntegerField()),
                ('is_visible_databaseinstance', models.IntegerField()),
                ('is_visible_cable', models.IntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'states',
                'managed': True,
                'unique_together': {('states_id', 'name')},
            },
        ),
        migrations.CreateModel(
            name='NetworkportsVlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id', models.PositiveIntegerField()),
                ('vlans_id', models.PositiveIntegerField()),
                ('tagged', models.IntegerField()),
            ],
            options={
                'db_table': 'networkports_vlans',
                'managed': True,
                'unique_together': {('networkports_id', 'vlans_id')},
            },
        ),
        migrations.CreateModel(
            name='NetworkportsNetworkports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkports_id_1', models.PositiveIntegerField()),
                ('networkports_id_2', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'networkports_networkports',
                'managed': True,
                'unique_together': {('networkports_id_1', 'networkports_id_2')},
            },
        ),
        migrations.CreateModel(
            name='Networkportmetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('ifinbytes', models.BigIntegerField()),
                ('ifinerrors', models.BigIntegerField()),
                ('ifoutbytes', models.BigIntegerField()),
                ('ifouterrors', models.BigIntegerField()),
                ('networkports_id', models.PositiveIntegerField()),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'networkportmetrics',
                'managed': True,
                'unique_together': {('networkports_id', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('locations_id', models.PositiveIntegerField()),
                ('completename', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('level', models.IntegerField()),
                ('ancestors_cache', models.TextField(blank=True, null=True)),
                ('sons_cache', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('town', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('building', models.CharField(blank=True, max_length=255, null=True)),
                ('room', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('altitude', models.CharField(blank=True, max_length=255, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'locations',
                'managed': True,
                'unique_together': {('entities_id', 'locations_id', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Entities',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('entities_id', models.PositiveIntegerField(blank=True, null=True)),
                ('completename', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('level', models.IntegerField()),
                ('sons_cache', models.TextField(blank=True, null=True)),
                ('ancestors_cache', models.TextField(blank=True, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('town', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=255, null=True)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_email', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_email_name', models.CharField(blank=True, max_length=255, null=True)),
                ('from_email', models.CharField(blank=True, max_length=255, null=True)),
                ('from_email_name', models.CharField(blank=True, max_length=255, null=True)),
                ('noreply_email', models.CharField(blank=True, max_length=255, null=True)),
                ('noreply_email_name', models.CharField(blank=True, max_length=255, null=True)),
                ('replyto_email', models.CharField(blank=True, max_length=255, null=True)),
                ('replyto_email_name', models.CharField(blank=True, max_length=255, null=True)),
                ('notification_subject_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('ldap_dn', models.CharField(blank=True, max_length=255, null=True)),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('authldaps_id', models.PositiveIntegerField()),
                ('mail_domain', models.CharField(blank=True, max_length=255, null=True)),
                ('entity_ldapfilter', models.TextField(blank=True, null=True)),
                ('mailing_signature', models.TextField(blank=True, null=True)),
                ('cartridges_alert_repeat', models.IntegerField()),
                ('consumables_alert_repeat', models.IntegerField()),
                ('use_licenses_alert', models.IntegerField()),
                ('send_licenses_alert_before_delay', models.IntegerField()),
                ('use_certificates_alert', models.IntegerField()),
                ('send_certificates_alert_before_delay', models.IntegerField()),
                ('certificates_alert_repeat_interval', models.IntegerField()),
                ('use_contracts_alert', models.IntegerField()),
                ('send_contracts_alert_before_delay', models.IntegerField()),
                ('use_infocoms_alert', models.IntegerField()),
                ('send_infocoms_alert_before_delay', models.IntegerField()),
                ('use_reservations_alert', models.IntegerField()),
                ('use_domains_alert', models.IntegerField()),
                ('send_domains_alert_close_expiries_delay', models.IntegerField()),
                ('send_domains_alert_expired_delay', models.IntegerField()),
                ('autoclose_delay', models.IntegerField()),
                ('autopurge_delay', models.IntegerField()),
                ('notclosed_delay', models.IntegerField()),
                ('calendars_strategy', models.IntegerField()),
                ('calendars_id', models.PositiveIntegerField()),
                ('auto_assign_mode', models.IntegerField()),
                ('tickettype', models.IntegerField()),
                ('max_closedate', models.DateTimeField(blank=True, null=True)),
                ('inquest_config', models.IntegerField()),
                ('inquest_rate', models.IntegerField()),
                ('inquest_delay', models.IntegerField()),
                ('inquest_url', models.CharField(blank=True, db_column='inquest_URL', max_length=255, null=True)),
                ('autofill_warranty_date', models.CharField(max_length=255)),
                ('autofill_use_date', models.CharField(max_length=255)),
                ('autofill_buy_date', models.CharField(max_length=255)),
                ('autofill_delivery_date', models.CharField(max_length=255)),
                ('autofill_order_date', models.CharField(max_length=255)),
                ('tickettemplates_strategy', models.IntegerField()),
                ('tickettemplates_id', models.PositiveIntegerField()),
                ('changetemplates_strategy', models.IntegerField()),
                ('changetemplates_id', models.PositiveIntegerField()),
                ('problemtemplates_strategy', models.IntegerField()),
                ('problemtemplates_id', models.PositiveIntegerField()),
                ('entities_strategy_software', models.IntegerField()),
                ('entities_id_software', models.PositiveIntegerField()),
                ('default_contract_alert', models.IntegerField()),
                ('default_infocom_alert', models.IntegerField()),
                ('default_cartridges_alarm_threshold', models.IntegerField()),
                ('default_consumables_alarm_threshold', models.IntegerField()),
                ('delay_send_emails', models.IntegerField()),
                ('is_notif_enable_default', models.IntegerField()),
                ('inquest_duration', models.IntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
                ('autofill_decommission_date', models.CharField(max_length=255)),
                ('suppliers_as_private', models.IntegerField()),
                ('anonymize_support_agents', models.IntegerField()),
                ('display_users_initials', models.IntegerField()),
                ('contracts_strategy_default', models.IntegerField()),
                ('contracts_id_default', models.PositiveIntegerField()),
                ('enable_custom_css', models.IntegerField()),
                ('custom_css_code', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('altitude', models.CharField(blank=True, max_length=255, null=True)),
                ('transfers_strategy', models.IntegerField()),
                ('transfers_id', models.PositiveIntegerField()),
                ('agent_base_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'entities',
                'managed': True,
                'unique_together': {('entities_id', 'name')},
            },
        ),
    ]