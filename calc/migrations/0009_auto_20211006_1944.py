# Generated by Django 3.2.7 on 2021-10-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_rename_events_participant_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.TextField(default='', null=True),
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]