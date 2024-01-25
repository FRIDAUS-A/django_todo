from django.urls import path
from . import views

urlpatterns = [
	path('create_tasks/<str:user_uid>/', views.createTask, name="create"),
	path('update_tasks/<str:user_uid>/<str:task_id>/', views.updateTask, name="update"),
	path('delete_tasks/<str:user_uid>/<str:task_id>', views.deleteTask, name="delete"),
	path('signup/', views.signupUser, name='signup'),
	path('', views.loginUser, name="login"),
	path('logout/', views.logOut, name="log_out")
]