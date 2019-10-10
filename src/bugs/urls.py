from django.urls import path, include
from .views import new_bug, edit_bug, view_all


urlpatterns = [
    path('', view_all, name='view_all_bugs'),
    path('new/', new_bug, name='new_bug'),
    path('edit/', edit_bug, name='edit_bug')
]