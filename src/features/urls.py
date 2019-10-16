from django.urls import path
from .views import (
    new_feature, 
    edit_feature, 
    view_all, 
    view_one, 
    delete_feature,
    )


urlpatterns = [
    path('', view_all, name='view_all_features'),
    path('new/', new_feature, name='new_feature'),
    path('<int:pk>/edit/', edit_feature, name='edit_feature'),
    path('<int:pk>/', view_one, name='view_one'),
    path('<int:pk>/delete/', delete_feature, name='delete_feature'),
]