# Generated by Django 2.1.3 on 2019-02-06 13:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20190206_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 2, 6, 13, 54, 2, 335148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='revenueadded',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 2, 6, 13, 54, 2, 336485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='revenuespent',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 2, 6, 13, 54, 2, 336940, tzinfo=utc)),
        ),
    ]