# Generated by Django 4.2.2 on 2023-07-16 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000000)),
                ('user', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 16, 23, 32, 45, 134937))),
                ('room', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
