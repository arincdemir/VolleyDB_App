from django.urls import path
from . import views

urlpatterns = [
    path("manager", views.managerLogin, name='managerLogin'),
    path("coach", views.coachLogin, name='coachLogin'),
    path("jury", views.juryLogin, name='juryLogin'),
    path("player", views.playerLogin, name='playerLogin'),
]