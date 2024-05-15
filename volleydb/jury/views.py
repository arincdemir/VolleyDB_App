from datetime import date, datetime
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
    error_message = None
    try:
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
                cursor.execute("SELECT M.rating, M.date FROM MatchSession M WHERE session_ID = %s;", [match_id])
                res = cursor.fetchone()
                old_rating = res[0]
                print(res[0])
                match_date = datetime.strptime(res[1], '%d.%m.%Y').date()
                
                if old_rating is None and match_date < date.today():
                    cursor.execute("UPDATE MatchSession SET rating = %s WHERE session_ID = %s;", [rating, match_id])
                else:
                    raise Exception("You can't rate that match!")
    except Exception as e:
        error_message = str(e)

    return render(request, "juryHome.html", {"username": username, "avg_rating": avg_rating, "total_rates": total_rates, "assigned_matches": assigned_matches, "error_message": error_message})