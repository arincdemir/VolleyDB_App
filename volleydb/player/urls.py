from django.urls import path
from . import views

urlpatterns = [
    path("", views.playerHome, name="playerHome"),
]