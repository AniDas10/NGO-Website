# Generated by Django 2.1.5 on 2019-02-08 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0008_auto_20190207_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 14, 22, 9, 519628, tzinfo=utc)),
        ),
    ]