# Generated by Django 4.2.8 on 2024-01-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0027_rename_custom_user_id_task_custom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=True),
        ),
    ]
