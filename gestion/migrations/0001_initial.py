# Generated by Django 4.1.3 on 2022-12-27 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solapin', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_prof', models.FloatField()),
                ('d_piel', models.FloatField()),
                ('d_crist', models.FloatField()),
                ('d_comp', models.FloatField()),
                ('solapin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.trabajador')),
            ],
        ),
    ]
