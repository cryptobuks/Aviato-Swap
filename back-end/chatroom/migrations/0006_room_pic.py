# Generated by Django 4.0 on 2022-06-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0005_remove_room_message_room_message_alter_room_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
