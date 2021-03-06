# Generated by Django 3.2.7 on 2021-10-03 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicensingAuthority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Licensing Authority')),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=20)),
                ('tel_main', models.CharField(max_length=20)),
                ('tel_contact', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('email_main', models.CharField(max_length=128, verbose_name='E-mail main')),
                ('contact_name', models.CharField(max_length=128)),
                ('miscellaneous_notes', models.TextField(verbose_name='Miscellaneous Notes')),
                ('date_file_opened', models.DateTimeField(auto_now_add=True)),
                ('date_file_closed', models.DateTimeField()),
                ('opened_by', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='is_licensed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='licensing_authority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.licensingauthority'),
        ),
    ]
