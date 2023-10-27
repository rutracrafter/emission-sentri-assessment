# Generated by Django 4.2.6 on 2023-10-26 22:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('accounting_period', models.CharField(max_length=500)),
                ('scope1', models.IntegerField(null=True)),
                ('scope2', models.IntegerField(null=True)),
                ('scope3', models.IntegerField(null=True)),
            ],
        ),
    ]