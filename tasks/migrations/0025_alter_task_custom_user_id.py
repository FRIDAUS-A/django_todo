# Generated by Django 4.2.8 on 2024-01-12 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_rename_task_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='custom_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.customuser'),
        ),
    ]