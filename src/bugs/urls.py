from django.urls import path, include
from .views import new_bug, edit_bug, view_all, view_one


urlpatterns = [
    path('', view_all, name='view_all_bugs'),
    path('new/', new_bug, name='new_bug'),
    path('edit/', edit_bug, name='edit_bug'),
    path('<int:pk>/', view_one, name='view_one'),
]