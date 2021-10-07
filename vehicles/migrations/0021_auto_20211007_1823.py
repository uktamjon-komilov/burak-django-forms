# Generated by Django 3.2.7 on 2021-10-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0020_alter_vehicle_depot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='as_at',
            field=models.DateField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='insurance_group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='last_recorded_mileage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='number_of_doors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='radio_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='VIN'),
        ),
    ]
