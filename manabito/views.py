from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        #user has info and wants to enter stuff
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'manabito/signup.html',{'error':'Username has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'manabito/signup.html',{'error':'Passwords must match'})

    else:
        #user wants to enter info
        return render(request, 'manabito/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'manabito/login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'manabito/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def manabitohome(request):
    manabitos = User.objects
    return render(request, 'manabito/home.html',{'manabitos':manabitos})
