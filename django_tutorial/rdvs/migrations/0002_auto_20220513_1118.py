# Generated by Django 3.2.13 on 2022-05-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdvs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rdv',
            name='date',
            field=models.DateField(default='2022-05-13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rdv',
            name='email_organisateur',
            field=models.EmailField(default='test@test.fr', max_length=254),
            preserve_default=False,
        ),
    ]