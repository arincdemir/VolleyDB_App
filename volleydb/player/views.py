from django.shortcuts import render
from django.db import connection

# Create your views here.

class Player:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


def playerHome(request):
    username = request.session.get("username")
    # TODO get played with players and average height

    played_with = [Player("John", "Doe"), Player("Jane", "Doe")]
    avg_height = 190
    return render(request, "playerHome.html", {"username": username, "played_with" : played_with , "avg_height": avg_height})
