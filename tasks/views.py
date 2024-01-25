from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import generic
from .forms import TaskForm, LoginForm
from .models import Task
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import uuid
from .models import CustomUser
import re
# Create your views here.

@csrf_exempt
def createTask(request, user_uid):
	template = loader.get_template('tasks/lists.html')
	tasks = Task.objects.all()
	form = TaskForm()
	context = {'tasks': tasks, 'form': form}
	if request.method == 'POST':
		customuser = CustomUser.objects.get(user_uid=str(user_uid))
		text  = request.POST.get('text')
		task = Task(title=text)
		task.custom_user = customuser
		task.task_id = uuid.uuid1()
		task.save()
		#url = 'create_tasks/' + user_uid + '/'
		return redirect('create', user_uid=user_uid)
	return HttpResponse(template.render(context, request))


@csrf_exempt
def updateTask(request, user_uid, task_id):
	task = Task.objects.get(task_id=task_id)
	#task = get_object_or_404(Task, pk=int(task_id))
	form = TaskForm(instance=task)
	if request.method == 'POST':
		if 'update' in request.POST:
			task.title = request.POST['title']
			task.complete = request.POST.get('complete') == 'on'
			task.save()
		return HttpResponseRedirect(reverse('create', args=(user_uid, )))
	context = {'form': form, 'task': task} 
	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, user_uid, task_id):
	task = get_object_or_404(Task, task_id=task_id)
	if request.method == 'POST':
		user = task.custom_user
		task.delete()
		return redirect('create', user.user_uid)
	context = {}
	context['task'] = task
	return render(request, 'tasks/delete_task.html', context)


@csrf_exempt
def signupUser(request):
	context = {}
	if request.method == 'GET':
		template = loader.get_template('tasks/signup.html')
		return HttpResponse(template.render(context, request))
	username = request.POST['username']
	passwd_1 = request.POST['password']
	passwd_2 = request.POST.get('confirm_password')
	email = request.POST.get('email')
	if '@' not in passwd_2:
		messages.error(request, 'password should contain @')
		return redirect('signup')
	if passwd_1 != passwd_2:
		messages.info(request, 'The password is not the same')
		return HttpResponseRedirect(reverse('signup'))
	else:
		users = User.objects.all()
		for user in users:
			if user.username == username:
				messages.info(request, 'Username Exists')
				return redirect('signup')
			elif user.email == email:
				messages.info(request, 'Email Exists')
				return redirect('signup')
		user = User(username=username, email=email)
		user.set_password(passwd_1)
		#user.uuid = uuid.uuid1()
		user.save()
		user_uid = user.customuser_set.create(user_uid=uuid.uuid1())
		return redirect('/')

@csrf_exempt
def loginUser(request):	
	if request.method == 'GET':
		return render(request, 'tasks/login.html')
	else:
		username = request.POST.get('username_login')
		password = request.POST.get('password_login')
		user = authenticate(request, username=username, password=password)
		if user is not None:
				login(request, user)
				input = user.customuser_set.all()
				return redirect(reverse('create', args=(input[0].user_uid,  )))
		else:
				messages.info(request, 'Invalid username or password')
				return HttpResponseRedirect(reverse('login'), {'user': user})
		
@login_required
def logOut(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/')
	else:
		return render(request, 'tasks/logout.html')