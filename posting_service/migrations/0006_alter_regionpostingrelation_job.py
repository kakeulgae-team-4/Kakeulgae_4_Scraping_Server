# Generated by Django 5.0.2 on 2024-03-18 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0005_remove_jobposting_job_jobdetailpostingrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionpostingrelation',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_posting_relations', to='posting.jobposting'),
        ),
    ]