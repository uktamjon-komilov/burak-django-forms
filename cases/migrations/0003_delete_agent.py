# Generated by Django 3.2.7 on 2021-10-02 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_rename_emial_agent_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agent',
        ),
    ]
