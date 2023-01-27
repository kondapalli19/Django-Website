from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate

# Create your views here.

#user- kkoyal, password- kkoyal
#db inside user-koyal password-kkoyal123@
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def login(request):
    if request.method=="POST":
        #check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(username=username, password=password)
        if User is not None:
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
            
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
