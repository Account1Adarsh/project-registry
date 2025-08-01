# Generated by Django 5.1.2 on 2025-07-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_batch_remove_project_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='batch',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='level',
            field=models.CharField(blank=True, choices=[('minor', 'Minor'), ('major', 'Major')], max_length=10),
        ),
    ]
