# Generated by Django 4.1 on 2022-08-31 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entities_id', models.PositiveIntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('serial', models.CharField(blank=True, max_length=255, null=True)),
                ('otherserial', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('users_id_tech', models.PositiveIntegerField()),
                ('groups_id_tech', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('autoupdatesystems_id', models.PositiveIntegerField()),
                ('locations_id', models.PositiveIntegerField()),
                ('networks_id', models.PositiveIntegerField()),
                ('computermodels_id', models.PositiveIntegerField()),
                ('computertypes_id', models.PositiveIntegerField()),
                ('is_template', models.IntegerField()),
                ('template_name', models.CharField(blank=True, max_length=255, null=True)),
                ('manufacturers_id', models.PositiveIntegerField()),
                ('is_deleted', models.IntegerField()),
                ('is_dynamic', models.IntegerField()),
                ('users_id', models.PositiveIntegerField()),
                ('groups_id', models.PositiveIntegerField()),
                ('states_id', models.PositiveIntegerField()),
                ('ticket_tco', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
                ('is_recursive', models.IntegerField()),
                ('last_inventory_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'computers',
                'managed': True,
            },
        ),
    ]
