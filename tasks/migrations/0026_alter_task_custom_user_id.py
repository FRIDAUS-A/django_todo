# Generated by Django 4.2.8 on 2024-01-12 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0025_alter_task_custom_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='custom_user_id',
            field=models.ForeignKey(default=8000, on_delete=django.db.models.deletion.CASCADE, to='tasks.customuser'),
        ),
    ]