# Generated by Django 4.2.8 on 2024-01-12 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_alter_task_custom_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='custom_user_id',
            new_name='custom_user',
        ),
    ]
