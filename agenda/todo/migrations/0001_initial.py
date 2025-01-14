# Generated by Django 4.2 on 2024-07-21 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('fin_fecha', models.DateField(blank=True, null=True)),
                ('prioridad', models.IntegerField(default=3)),
            ],
        ),
    ]
