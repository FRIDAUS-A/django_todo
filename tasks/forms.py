from django import forms
from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User
class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = "__all__"

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email']