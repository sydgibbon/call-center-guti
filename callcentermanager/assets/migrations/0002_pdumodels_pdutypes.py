# Generated by Django 4.0.5 on 2022-11-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdumodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('product_number', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.IntegerField()),
                ('required_units', models.IntegerField()),
                ('depth', models.FloatField()),
                ('power_connections', models.IntegerField()),
                ('max_power', models.IntegerField()),
                ('is_half_rack', models.IntegerField()),
                ('picture_front', models.TextField(blank=True, null=True)),
                ('picture_rear', models.TextField(blank=True, null=True)),
                ('pictures', models.TextField(blank=True, null=True)),
                ('is_rackable', models.IntegerField()),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pdumodels',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pdutypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entities_id', models.PositiveIntegerField()),
                ('is_recursive', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(blank=True, null=True)),
                ('date_mod', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pdutypes',
                'managed': True,
            },
        ),
    ]
