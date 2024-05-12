from django.urls import path
from . import views

urlpatterns = [
    path('', views.coachHome, name='coachHome'),
    path('deleteMatch', views.deleteMatch, name='deleteMatch'),
    path('addMatch', views.addMatch, name='addMatch'),
    path('createSquad', views.createSquad, name='createSquad')
]