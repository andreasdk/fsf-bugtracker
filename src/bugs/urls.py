from django.urls import path, include
from .views import (
    new_bug, 
    edit_bug, 
    view_all, 
    view_bug, 
    delete_bug,
    vote,
    )


urlpatterns = [
    path('', view_all, name='view_all_bugs'),
    path('new/', new_bug, name='new_bug'),
    path('<int:pk>/edit/', edit_bug, name='edit_bug'),
    path('<int:pk>/', view_bug, name='view_bug'),
    path('<int:pk>/delete/', delete_bug, name='delete_bug'),
    path('vote/<int:pk>', vote, name='vote'),
]