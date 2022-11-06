# Generated by Django 4.0.5 on 2022-11-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peripheralmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('product_number', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.IntegerField()),
                ('required_units', models.IntegerField()),
                ('depth', models.FloatField()),
                ('power_connections', models.IntegerField()),
                ('power_consumption', models.IntegerField()),
                ('is_half_rack', models.IntegerField()),
                ('picture_front', models.TextField(blank=True, null=True)),
                ('picture_rear', models.TextField(blank=True, null=True)),
                ('pictures', models.TextField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'peripheralmodels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Peripherals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entities_id', models.PositiveIntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('users_id_tech', models.PositiveIntegerField()),
                ('groups_id_tech', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('serial', models.CharField(blank=True, max_length=255, null=True)),
                ('otherserial', models.CharField(blank=True, max_length=255, null=True)),
                ('locations_id', models.PositiveIntegerField()),
                ('peripheraltypes_id', models.PositiveIntegerField()),
                ('peripheralmodels_id', models.PositiveIntegerField()),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('manufacturers_id', models.PositiveIntegerField()),
                ('is_global', models.IntegerField()),
                ('is_deleted', models.IntegerField()),
                ('is_template', models.IntegerField()),
                ('template_name', models.CharField(blank=True, max_length=255, null=True)),
                ('users_id', models.PositiveIntegerField()),
                ('groups_id', models.PositiveIntegerField()),
                ('states_id', models.PositiveIntegerField()),
                ('ticket_tco', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('is_dynamic', models.IntegerField()),
                ('autoupdatesystems_id', models.PositiveIntegerField()),
                ('uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
                ('is_recursive', models.IntegerField()),
            ],
            options={
                'db_table': 'peripherals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Peripheraltypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'peripheraltypes',
                'managed': False,
            },
        ),
    ]