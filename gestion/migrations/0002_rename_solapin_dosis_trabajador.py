# Generated by Django 4.1.3 on 2022-12-27 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dosis',
            old_name='solapin',
            new_name='trabajador',
        ),
    ]
