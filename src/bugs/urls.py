from django.urls import path, include
from .views import new_bug


urlpatterns = [
    path('new/', new_bug, name='new_bug'),
]