from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
class CustomUser(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	user_uid = models.CharField(max_length=50)


# Create your models here.
class Task(models.Model):
	custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=8000)
	title =  models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now=True)
	task_id = models.CharField(max_length=50, default='default')

	def str(self):
		"""string representation of the object"""
		return self.__title