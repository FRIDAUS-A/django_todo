# Generated by Django 4.2.8 on 2024-01-12 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_remove_task_custom_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]
