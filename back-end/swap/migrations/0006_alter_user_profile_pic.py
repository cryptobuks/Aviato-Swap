# Generated by Django 4.0 on 2022-06-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swap', '0005_alter_user_blocked_user_alter_user_ip_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]