# Generated by Django 4.0 on 2022-06-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swap', '0002_remove_wallet_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prifile_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]