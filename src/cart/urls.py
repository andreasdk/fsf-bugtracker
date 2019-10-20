from django.urls import path
from .views import view_cart, add_to_cart, delete_item

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<int:id>', add_to_cart, name='add_to_cart'),
    path('delete/<int:id>', delete_item, name='delete_item'),
]