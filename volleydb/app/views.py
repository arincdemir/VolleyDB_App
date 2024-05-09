from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
# Create your views here.

def home(request):
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Player")  # replace with your actual SQL query
        rows = cursor.fetchall()

    return HttpResponse(rows)
    """

    return render(request, 'home.html')

def databaseManagerLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM DatabaseManager WHERE username = %s AND password = %s", [username, password])
            row = cursor.fetchone()
            if row:
                return HttpResponseRedirect('/manager/')
            else:
                return render(request, 'managerLogin.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'managerLogin.html')


def manager(request):
    return render(request, 'manager.html')

def login2(request):
    return render(request, 'login2.html')