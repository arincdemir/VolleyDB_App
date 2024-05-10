from django.db import connection
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.

def managerHome(request):
    return render(request, 'managerHome.html', {'username': request.session['username']})

def addCoach(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        nationality = request.POST['nationality']

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Coach (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s);", [username, password, name, surname, nationality])
            row = cursor.fetchone()
            print(row)

        # Redirect to the manager home page after successfully adding a coach
        return render(request, 'managerHome.html', {"outcome" : "added coach successfully"})

    return render(request, 'addCoach.html')


def addJury(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        nationality = request.POST['nationality']

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Jury (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s);", [username, password, name, surname, nationality])
            row = cursor.fetchone()
            print(row)

        # Redirect to the manager home page after successfully adding a coach
        return render(request, 'managerHome.html', {"outcome" : "added jury successfully"})

    return render(request, 'addJury.html')

def addPlayer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        date_of_birth = request.POST['dateOfBirth']
        height = request.POST['height']
        weight = request.POST['weight']

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Player (username, password, name, surname, date_of_birth, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s);", [username, password, name, surname, date_of_birth, height, weight])
            row = cursor.fetchone()
            print(row)

        # Redirect to the manager home page after successfully adding a coach
        return render(request, 'managerHome.html', {"outcome" : "added player successfully"})

    return render(request, 'addPlayer.html')

def updateStadiumName(request):
    if request.method == 'POST':
        stadiumID = request.POST['stadiumID']
        newName = request.POST['newName']

        # TODO update the stadium name
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Player (username, password, name, surname, date_of_birth, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s);", [username, password, name, surname, date_of_birth, height, weight])
            row = cursor.fetchone()
            print(row)

        # Redirect to the manager home page after successfully adding a coach
        return render(request, 'managerHome.html', {"outcome" : "changed stadium name successfully"})

    return render(request, 'updateStadiumName.html')

