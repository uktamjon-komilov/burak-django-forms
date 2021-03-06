# Generated by Django 3.2.7 on 2021-10-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20211003_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claims_case_reference', models.CharField(max_length=128)),
                ('claim_type', models.CharField(max_length=128)),
                ('client_name', models.CharField(max_length=128)),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=128)),
                ('tel_main', models.CharField(max_length=128)),
                ('hire_vehicle_out_date', models.DateTimeField()),
                ('hire_vehicle_back_date', models.DateTimeField()),
                ('reserved', models.BooleanField()),
                ('claims_case_reference_2', models.CharField(max_length=128, verbose_name='Claims case reference')),
                ('username', models.CharField(max_length=128)),
                ('date_reserved', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_mot', models.DateTimeField()),
                ('next_mot_due', models.DateTimeField()),
                ('last_service', models.DateTimeField()),
                ('last_service_miles', models.FloatField(default=0.0, help_text='in miles')),
                ('next_service_due', models.DateTimeField()),
                ('next_service_due_miles', models.FloatField(default=0.0, help_text='in miles')),
                ('next_service_due_in', models.FloatField(default=0.0)),
                ('vehicle_cost_to_date', models.FloatField(default=0.0, help_text='in £. Note: All servicing, repair and misc vehicle costs should be entered using this screen. Entries can be added with a Zero cost if necessary to maintain a detailed summary.')),
                ('date', models.DateTimeField()),
                ('service_type', models.CharField(blank=True, choices=[('servicing', 'Servicing'), ('oil', 'Oil'), ('professional-valet', 'Professional Valet'), ('miscellenaous', 'Miscellenaous'), ('tyres', 'Tyres'), ('windscreen', 'Windscreen'), ('body-work-repairs', 'Body Work Repairs'), ('mechanical-repair', 'Mechanical Repairs'), ('wiper-blades', 'Wiper Blades'), ('bulb-replacement', 'Bulb replacement'), ('keys', 'Keys')], max_length=50, null=True, verbose_name='Type')),
                ('invoice_no', models.CharField(blank=True, help_text='If applicable', max_length=128, null=True)),
                ('vat', models.FloatField(blank=True, default=0.0, help_text='in £', null=True)),
                ('amount', models.FloatField(default=0.0, help_text='in £')),
                ('supplier_name', models.CharField(help_text='Garage, shop etc.', max_length=128)),
                ('misc_details', models.TextField(help_text='20K service. Rear Indicator Bulb replacement')),
            ],
        ),
    ]
