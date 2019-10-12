from django.urls import path, include
from .views import (
    new_bug, 
    edit_bug, 
    view_all, 
    view_one, 
    delete_bug,
    vote,
    )


urlpatterns = [
    path('', view_all, name='view_all_bugs'),
    path('new/', new_bug, name='new_bug'),
    path('<int:pk>/edit/', edit_bug, name='edit_bug'),
    path('<int:pk>/', view_one, name='view_one'),
    path('<int:pk>/delete/', delete_bug, name='delete_bug'),
    path('vote/<int:pk>', vote, name='vote'),
]