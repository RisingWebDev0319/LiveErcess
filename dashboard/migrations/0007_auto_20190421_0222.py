# Generated by Django 2.1.5 on 2019-04-21 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20190421_0206'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='statusonchannel',
            table='event_status_on_channel',
        ),
    ]