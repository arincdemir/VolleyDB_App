from django.shortcuts import render
from django.db import connection

# Create your views here.

class Player:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


def playerHome(request):
    username = request.session.get("username")
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT P.name, P.surname FROM SessionSquads S, Player P, (SELECT DISTINCT S2.session_ID FROM SessionSquads S2 WHERE S2.played_player_username = %s) AS M WHERE S.session_ID IN (M.session_ID) AND P.username = S.played_player_username", [username])
            played_with = [Player(*row) for row in cursor.fetchall()]
            cursor.execute("SELECT	AVG(P.height) AS he FROM Player P, (SELECT  S.played_player_username, COUNT(*) AS countt FROM SessionSquads S, (SELECT DISTINCT S2.session_ID FROM SessionSquads S2 WHERE S2.played_player_username = %s) AS M WHERE S.session_ID IN (M.session_ID) AND S.played_player_username != %s GROUP BY S.played_player_username) AS TMS, (SELECT MAX(T.countt) AS maxcountt FROM (SELECT  S.played_player_username, COUNT(*) AS countt FROM SessionSquads S, (SELECT DISTINCT S2.session_ID FROM SessionSquads S2 WHERE S2.played_player_username =  %s) AS M WHERE S.session_ID IN (M.session_ID) AND S.played_player_username !=  %s GROUP BY S.played_player_username) AS T ) AS MAXCOUNT WHERE TMS.countt = MAXCOUNT.maxcountt AND TMS.played_player_username = P.username;", [username, username, username, username])
            avg_height = float(cursor.fetchone()[0])
    except Exception as e:
        error_message = str(e)

    return render(request, "playerHome.html", {"username": username, "played_with" : played_with , "avg_height": avg_height, "error_message": error_message})
