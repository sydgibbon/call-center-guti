# Generated by Django 4.0.5 on 2023-09-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_alter_authldaps_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkequipments',
            name='uptime',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
