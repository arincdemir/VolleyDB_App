from django.db import connection
from django.shortcuts import render

# Create your views here.

class MatchSession:
    def __init__(self, sessionID, teamID, stadiumID, timeSlot, date, assignedJuryUsername, rating):
        self.session_ID	= sessionID
        self.team_ID = teamID
        self.stadium_ID = stadiumID,
        self.time_slot = timeSlot
        self.date = date
        self.assigned_jury_username	= assignedJuryUsername
        self.rating	= rating

def juryHome(request):
    username = request.session.get("username")

    with connection.cursor() as cursor:
        cursor.execute("SELECT AVG(rating) FROM MatchSession WHERE assigned_jury_username = %s;", [username])
        avg_rating = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(rating) FROM MatchSession WHERE assigned_jury_username = %s;", [username])
        total_rates = cursor.fetchone()[0]
        cursor.execute("SELECT * FROM MatchSession WHERE assigned_jury_username = %s;", [username])
        assigned_matches = [MatchSession(*row) for row in cursor.fetchall()]

    if request.method == "POST":
        match_id = request.POST.get("session_ID")
        rating = request.POST.get("rating")
        
        with connection.cursor() as cursor:
            cursor.execute("UPDATE MatchSession SET rating = %s WHERE session_ID = %s;", [rating, match_id])

    return render(request, "juryHome.html", {"username": username, "avg_rating": avg_rating, "total_rates": total_rates, "assigned_matches": assigned_matches})