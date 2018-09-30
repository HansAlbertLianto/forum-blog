from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    if request.method == 'POST':
        userUsername = request.POST.get('username')
        userPassword = request.POST.get('password')

        user = authenticate(username=userUsername, password=userPassword)

        print(user)

        if user is not None:
            print("hello")
            # Redirect to a success page.
            return render(request, 'login/success.html')
        else:
            return render(request, 'login/login.html', )

    return render(request, 'login/login.html')
