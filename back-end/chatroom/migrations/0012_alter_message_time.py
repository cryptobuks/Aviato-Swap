# Generated by Django 4.0.6 on 2022-08-12 03:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0011_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 12, 3, 41, 57, 130837, tzinfo=utc), null=True),
        ),
    ]
