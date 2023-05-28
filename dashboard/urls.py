from django.urls import path
from . import views

urlpatterns = [
    path("", views.git_test, name="git_test")
]