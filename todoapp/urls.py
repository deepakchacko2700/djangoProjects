from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    path('', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.ToDoListView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete')
]