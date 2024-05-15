import random
from django.db import connection
from django.shortcuts import redirect, render

# Create your views here.

class Stadium:
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country

class Match:
    def __init__(self, id, teamID, stadiumID, timeSlot, date, jury, rating):
        self.id = id
        self.teamID = teamID
        self.date = date
        self.stadiumID = stadiumID
        self.timeSlot = timeSlot
        self.jury = jury
        self.rating = rating

def coachHome(request):
    username = request.session.get('username')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Stadium")
        stadiums = [Stadium(*row) for row in cursor.fetchall()]
    return render(request, 'coachHome.html', {'username': username, "stadiums": stadiums})

def deleteMatch(request):
    error_message = None
    try:
        if request.method == 'POST':
            matchId = request.POST.get('matchId')
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM MatchSession WHERE session_ID = %s", [matchId])    
        with connection.cursor() as cursor:
            cursor.execute("SELECT M.* FROM MatchSession M, Team T WHERE M.team_ID = T.team_ID and T.coach_username = %s", [request.session.get('username')])
            matches = [Match(*row) for row in cursor.fetchall()]
    except Exception as e:
        error_message = str(e)
    return render(request, 'deleteMatch.html', {'matches': matches, 'error_message': error_message})
    
def addMatch(request):
    error_message = None
    if request.method == 'POST':
        try:
            stadiumID = request.POST.get('stadiumID')
            date = request.POST.get('date')
            timeSlot = request.POST.get('timeSlot')
            juryName = request.POST.get('juryName')
            jurySurname = request.POST.get('jurySurname')
            sessionID = random.randint(1000, 9999999)

            with connection.cursor() as cursor:
                cursor.execute("SELECT username FROM Jury WHERE name = %s and surname = %s", [juryName, jurySurname])
                juryUsername = cursor.fetchone()[0]
                cursor.execute("SELECT team_ID FROM Team WHERE coach_username = %s", [request.session.get('username')])
                teamID = cursor.fetchone()[0]
                cursor.execute("INSERT INTO MatchSession (session_ID, team_ID, stadium_ID, time_slot, date, assigned_jury_username, rating) VALUES (%s, %s, %s, %s, %s, %s, NULL)", [sessionID, teamID, stadiumID, timeSlot, date, juryUsername])
                request.session['matchId'] = sessionID
            return redirect(coachHome)
        except Exception as e:
            error_message = str(e)
    
    return render(request, 'addMatch.html', {'error_message': error_message})

def createSquad(request):
    error_message = None
    if request.method == 'POST':
        try:
            matchId = request.session.get('matchId')
            playerNames = request.POST.getlist('name[]')
            playerSurnames = request.POST.getlist('surname[]')
            positionIDs = request.POST.getlist('position[]')
            squadID = random.randint(1000, 9999999)
            print(matchId, playerNames, playerSurnames, positionIDs, squadID)
            with connection.cursor() as cursor:
                cursor.execute("SELECT team_ID FROM MatchSession WHERE session_ID = %s", [matchId])
                teamID = cursor.fetchone()[0]
                for i in range(len(playerNames)):
                    print(playerNames[i], playerSurnames[i], positionIDs[i])
                    cursor.execute("SELECT username FROM Player WHERE name = %s and surname = %s", [playerNames[i], playerSurnames[i]])
                    res = cursor.fetchone()
                    if res is None:
                        raise Exception("Player not found!")
                    playerUsername = res[0]
                    cursor.execute("SELECT T.team_ID  FROM PlayerTeams T WHERE T.username = %s and T.team_ID = %s", [playerUsername, teamID])
                    if cursor.fetchone() is None:
                        raise Exception("Player is not in the team!")
                    cursor.execute("INSERT INTO SessionSquads (squad_ID, session_ID, played_player_username, position_ID) VALUES (%s, %s, %s, %s)", [squadID, matchId, playerUsername, positionIDs[i]])
            return redirect(coachHome)
        except Exception as e:
            error_message = str(e)
    return render(request, 'createSquad.html', {'matchId': request.session.get('matchId'), 'error_message': error_message})
