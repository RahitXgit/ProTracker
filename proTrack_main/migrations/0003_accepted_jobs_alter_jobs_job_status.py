# Generated by Django 5.1.2 on 2024-10-28 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proTrack_main', '0002_alter_jobs_job_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='accepted_jobs',
            fields=[
                ('job', models.OneToOneField(limit_choices_to={'job_status': 'accepted'}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='proTrack_main.jobs')),
                ('job_application_date', models.DateField(verbose_name='Application Date')),
                ('job_title', models.CharField(max_length=100, verbose_name='Role')),
                ('job_type', models.CharField(choices=[('internship', 'Internship'), ('job', 'Job')], max_length=10, verbose_name='Job Type')),
                ('company_name', models.CharField(max_length=100, verbose_name='Company Name')),
                ('applied_link', models.URLField(verbose_name='Application Link')),
                ('job_posted_date', models.DateField(verbose_name='Job Posted Date')),
            ],
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_status',
            field=models.CharField(blank=True, choices=[('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10, verbose_name='Status'),
        ),
    ]
