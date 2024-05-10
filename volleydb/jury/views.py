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

    # TODO get avg_rating and total_rates and matches from database
    avg_rating = 4.5
    total_rates = 100
    assigned_matches = [MatchSession(1, 1, 1, "10:00", "2021-01-01", "jury1", 4.5), MatchSession(2, 2, 2, "12:00", "2021-01-01", "jury1", 4.5)]

    if request.method == "POST":
        match_id = request.POST.get("match_id")
        rating = request.POST.get("rating")
        # TODO update rating in database

    
    return render(request, "juryHome.html", {"username": username, "avg_rating": avg_rating, "total_rates": total_rates, "assigned_matches": assigned_matches})