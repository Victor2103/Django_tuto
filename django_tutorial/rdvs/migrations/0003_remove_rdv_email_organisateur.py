# Generated by Django 3.2.13 on 2022-05-16 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rdvs', '0002_remove_rdv_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdv',
            name='email_organisateur',
        ),
    ]
