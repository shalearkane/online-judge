from django.urls import path
from . import views

urlpatterns = [
    path("submit", views.compile_run, name="submit"),
]
