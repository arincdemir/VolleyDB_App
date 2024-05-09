from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("managerLogin/", views.databaseManagerLogin, name='managerLogin'),
    path("login2/", views.login2, name='login2'),
    path("manager/", views.manager, name='manager'),
]