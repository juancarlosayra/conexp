# Generated by Django 4.1.4 on 2023-01-20 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_rename_solapin_dosis_trabajador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dosis',
            options={'permissions': (('can_mark_returned', 'Trabajador modificado'),)},
        ),
    ]
