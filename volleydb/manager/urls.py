from django.urls import path
from . import views

urlpatterns = [
    path("", views.managerHome, name="managerHome"),
    path("addCoach", views.addCoach, name="addCoach"),
    path("addJury", views.addJury, name="addJury"),
    path("addPlayer", views.addPlayer, name="addPlayer"),
    path("updateStadiumName", views.updateStadiumName, name="updateStadiumName")
]