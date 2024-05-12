from django.shortcuts import redirect, render

# Create your views here.

class Stadium:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Match:
    def __init__(self, id, date, stadiumName):
        self.id = id
        self.date = date
        self.stadiumName = stadiumName

def coachHome(request):
    username = request.session.get('username')
    #TODO get stadiums from database
    stadiums = [
        Stadium('Stade de France', 'France'),
        Stadium('Wembley Stadium', 'England'),
        Stadium('Estadio Santiago Bernabeu', 'Spain'),
        Stadium('Allianz Arena', 'Germany')
    ]
    return render(request, 'coachHome.html', {'username': username, "stadiums": stadiums})

def deleteMatch(request):
    if request.method == 'POST':
        matchId = request.POST.get('matchId')
        # TODO delete match from database
        print(matchId)
        return redirect(coachHome)
    else:
        # TODO get matches from database
        matches = [
            Match(1, '2021-05-01', 'Stade de France'),
            Match(2, '2021-05-02', 'Wembley Stadium'),
            Match(3, '2021-05-03', 'Estadio Santiago Bernabeu'),
            Match(4, '2021-05-04', 'Allianz Arena')
        ]
        return render(request, 'deleteMatch.html', {'matches': matches})
    
def addMatch(request):
    if request.method == 'POST':
        stadiumID = request.POST.get('stadiumID')
        date = request.POST.get('date')
        timeSlot = request.POST.get('timeSlot')
        juryName = request.POST.get('juryName')
        jurySurname = request.POST.get('jurySurname')
        # TODO add match to database
        return redirect(coachHome)
    else:
        return render(request, 'addMatch.html')

def createSquad(request):
    if request.method == 'POST':
        matchId = request.POST.get('matchId')
        playerNames = request.POST.getlist('name[]')
        playerSurnames = request.POST.getlist('surname[]')
        print(playerNames)
        # TODO add squad to database
        return redirect(coachHome)
    else:
        
        return render(request, 'createSquad.html')
