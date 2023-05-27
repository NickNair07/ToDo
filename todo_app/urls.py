from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Add task
    path('add-task/', views.addTask, name='addtask'),
    # Mark as done
    path('mark-as-done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as undone
    path('mark-as-undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit task feature
    path('edit-task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete task feature
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
]
