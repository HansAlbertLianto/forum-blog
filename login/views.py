from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

    return render(request, 'login/login.html')
