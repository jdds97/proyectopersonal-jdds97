"""Core URLs module."""
from django.urls import path
from .views import welcome

urlpatterns = [
    path("", welcome, name="core_welcome"),
]
