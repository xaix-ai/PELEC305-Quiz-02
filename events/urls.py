from django.urls import path
from .views import register_event, success

urlpatterns = [
    path('register/', register_event, name='register_event'),
    path('success/', success, name='success'),
]