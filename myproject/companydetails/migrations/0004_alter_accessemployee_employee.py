# Generated by Django 5.1.8 on 2025-04-03 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companydetails', '0003_rename_hr_assigned_candidate_assigned_hr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessemployee',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_role', to='companydetails.companyemployee'),
        ),
    ]
