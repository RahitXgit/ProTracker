# Generated by Django 5.1.2 on 2024-10-28 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proTrack_main', '0004_acceptedjobs_delete_accepted_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='RejectedJobs',
            fields=[
                ('job', models.OneToOneField(limit_choices_to={'job_status': 'rejected'}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='proTrack_main.jobs')),
            ],
        ),
    ]