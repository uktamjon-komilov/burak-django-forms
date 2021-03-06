# Generated by Django 3.2.7 on 2021-10-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0009_auto_20211004_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='mot_status',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='licensing_authority',
            field=models.ManyToManyField(blank=True, related_name='vehicle', to='vehicles.LicensingAuthority'),
        ),
    ]
