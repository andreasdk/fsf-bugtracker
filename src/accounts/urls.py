from django.urls import path, include
from accounts.views import login, register, profile, logout
from . import urls_reset


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('password-reset/', include(urls_reset)),
]