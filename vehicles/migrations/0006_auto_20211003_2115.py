# Generated by Django 3.2.7 on 2021-10-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_auto_20211003_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='agreement_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='contact_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='fax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='lease_miles_remaining',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='lease_return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='lease_return_miles',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='length_of_agreement',
            field=models.IntegerField(blank=True, help_text='Mths', null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='postcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='purchase_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='purchase_price',
            field=models.FloatField(blank=True, help_text='in ??', null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='purchase_price_vat',
            field=models.FloatField(blank=True, help_text='in ??', null=True, verbose_name='Purchase price VAT'),
        ),
        migrations.AlterField(
            model_name='finance',
            name='tel_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='telephone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='claim_type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='claims_case_reference',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='claims_case_reference_2',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Claims case reference'),
        ),
        migrations.AlterField(
            model_name='hire',
            name='client_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='date_reserved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='hire_vehicle_back_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='hire_vehicle_out_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='postcode',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='tel_main',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hire',
            name='username',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='contact_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='date_file_closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='date_file_opened',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='email_main',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='E-mail main'),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='fax',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='miscellaneous_notes',
            field=models.TextField(blank=True, null=True, verbose_name='Miscellaneous Notes'),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Licensing Authority'),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='opened_by',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='tel_contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='licensingauthority',
            name='tel_main',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='contact_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_sold',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='fax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='forename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='guid_price',
            field=models.FloatField(blank=True, help_text='in ??', null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='mileage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='postcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sale_price',
            field=models.FloatField(blank=True, help_text='in ??', null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='surname_or_company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Surname/Company'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='tel_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='telephone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='last_mot',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='last_service',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='last_service_miles',
            field=models.FloatField(default=0.0, help_text='in miles', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='misc_details',
            field=models.TextField(blank=True, help_text='20K service. Rear Indicator Bulb replacement', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='next_mot_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='next_service_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='supplier_name',
            field=models.CharField(blank=True, help_text='Garage, shop etc.', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='fax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='first_registration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='postcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='purchase_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='purchase_price',
            field=models.FloatField(blank=True, help_text='in ??', null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='purchase_price_vat',
            field=models.FloatField(blank=True, help_text='in ??', null=True, verbose_name='Purchase price VAT'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='tel_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='telephone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
