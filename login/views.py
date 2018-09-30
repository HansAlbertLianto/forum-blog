from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def index(request):

    loginSuccess = True

    if request.method == 'POST':
        userUsername = request.POST.get('username')
        userPassword = request.POST.get('password')
        userConfirmPassword = request.POST.get('confirmPassword')

        # Handle new signup from signup page
        if userConfirmPassword is not None:

            # Check if username already exists. Then check if confirm password matches with password.
            if User.objects.filter(username=userUsername).exists():
                return render(request, 'login/signup.html', {'usernameTaken': True})
            else:
                if userPassword != userConfirmPassword:
                    return render(request, 'login/signup.html', {'passwordsDontMatch': True})
                user = User.objects.create_user(userUsername, None, userPassword)
                user.save()
                return render(request, 'login/success.html') # change this.

        # Find out if user credentials are correct or not.
        credentialsCorrect = authenticate(username=userUsername, password=userPassword)

        loginSuccess = (user is not None)

        # If user credentials are correct, load home page. Otherwise, return a 
        if credentialsCorrect:
            # Redirect to a success page.
            return render(request, 'login/success.html') # change this.
        else:
            return render(request, 'login/login.html', {'loginSuccess': loginSuccess})

    return render(request, 'login/login.html')

def signup(request):
    return render(request, 'login/signup.html')
