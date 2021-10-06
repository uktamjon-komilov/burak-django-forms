# Generated by Django 3.2.7 on 2021-10-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0003_delete_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_type', models.CharField(choices=[('rta', 'RTA'), ('slip-trip', 'Slip/Trip'), ('clinical-negligence', 'Clinical Negligence'), ('works-accident', 'Works Accident'), ('industrial-disease', 'Industrial Disease'), ('hire-only', 'Hire Only')], max_length=50)),
                ('case_status', models.CharField(choices=[('just-started', 'Just started'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('dead-closed', 'Dead/Closed')], max_length=50)),
                ('handler', models.CharField(choices=[('claims-department', 'Claims Department')], max_length=50)),
                ('opened_date', models.DateTimeField(auto_now_add=True, verbose_name='File Opened Date')),
                ('closed_date', models.DateTimeField(verbose_name='File Closed Date')),
                ('opened_by', models.CharField(max_length=255, verbose_name='File Opened by')),
            ],
        ),
    ]