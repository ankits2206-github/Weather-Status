# Generated by Django 3.0 on 2020-07-10 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flight', '0008_auto_20200703_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='date',
            field=models.DateField(default=datetime.date(2020, 7, 10)),
        ),
    ]
