from django.urls import path

from . import views

urlpatterns = [
    #add task functionality
    path('addTask/', views.addTask, name='addTask'),
    
    #Mark as done task functionality

    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    
    #Marks as undone task functionality

    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    
    #edit/update task functionality

    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    
    #Delete task functionality
    path('delete_task/<int:pk>/',views.delete_task , name='delete_task'),

]
