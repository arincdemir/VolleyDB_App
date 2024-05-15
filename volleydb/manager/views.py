from django.db import Error, connection
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.

def managerHome(request):
    return render(request, 'managerHome.html', {'username': request.session['username']})

def addCoach(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        nationality = request.POST['nationality']

        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Coach (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s);", [username, password, name, surname, nationality])

            # Redirect to the manager home page after successfully adding a coach
            return redirect(managerHome)
        except Exception as e:
            error_message = str(e)

    return render(request, 'addCoach.html', {'error_message': error_message})


def addJury(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        nationality = request.POST['nationality']
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Jury (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s);", [username, password, name, surname, nationality])

            # Redirect to the manager home page after successfully adding a coach
            return redirect(managerHome)
        except Exception as e:
            error_message = str(e)

    return render(request, 'addJury.html', {'error_message': error_message})

def addPlayer(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        date_of_birth = request.POST['dateOfBirth']
        height = request.POST['height']
        weight = request.POST['weight']
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Player (username, password, name, surname, date_of_birth, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s);", [username, password, name, surname, date_of_birth, height, weight])
                
            # Redirect to the manager home page after successfully adding a coach
            return redirect(managerHome)
        except Exception as e:
            error_message = str(e)

    return render(request, 'addPlayer.html', {'error_message': error_message})

def updateStadiumName(request):
    error_message = None
    if request.method == 'POST':
        stadiumID = request.POST['stadiumID']
        newName = request.POST['newName']

        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Stadium SET stadium_name = %s WHERE Stadium_id = %s;", [newName, stadiumID])

            # Redirect to the manager home page after successfully adding a coach
            return redirect(managerHome)
        except Exception as e:
            error_message = str(e)

    return render(request, 'updateStadiumName.html', {'error_message': error_message})

