# Generated by Django 4.2.8 on 2024-01-10 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_alter_customuser_user_id_alter_task_custom_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.ForeignKey(default=uuid.UUID('d22ac456-afd9-11ee-8aef-bbf3cce9e176'), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='custom_user_id',
            field=models.ForeignKey(default=uuid.UUID('d22ac457-afd9-11ee-8aef-bbf3cce9e176'), on_delete=django.db.models.deletion.CASCADE, to='tasks.customuser'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(default=uuid.UUID('d22ac458-afd9-11ee-8aef-bbf3cce9e176'), max_length=50),
        ),
    ]