# Generated by Django 5.1.2 on 2024-10-28 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proTrack_main', '0003_accepted_jobs_alter_jobs_job_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedJobs',
            fields=[
                ('job', models.OneToOneField(limit_choices_to={'job_status': 'accepted'}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='proTrack_main.jobs')),
            ],
        ),
        migrations.DeleteModel(
            name='accepted_jobs',
        ),
    ]
