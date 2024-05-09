from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def managerLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM DatabaseManager WHERE username = %s AND password = %s", [username, password])
            row = cursor.fetchone()
            if row:
                return HttpResponseRedirect('/manager/')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'login.html')
    
def coachLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Coach WHERE username = %s AND password = %s", [username, password])
            row = cursor.fetchone()
            if row:
                return HttpResponseRedirect('/manager/')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'login.html')

def juryLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Jury WHERE username = %s AND password = %s", [username, password])
            row = cursor.fetchone()
            if row:
                return HttpResponseRedirect('/manager/')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'login.html')
    
def playerLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Player WHERE username = %s AND password = %s", [username, password])
            row = cursor.fetchone()
            if row:
                return HttpResponseRedirect('/manager/')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'login.html')