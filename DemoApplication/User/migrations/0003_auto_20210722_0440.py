# Generated by Django 3.2.1 on 2021-07-21 23:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20210722_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 4, 40, 55, 646620)),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 4, 40, 55, 646620)),
        ),
    ]
