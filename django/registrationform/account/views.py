from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def index(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def Login(request):
    return render(request, 'login.html')


def Register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exists")
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email exists")
            else:
                user = User.objects.create(
                    username=username, first_name=fname, last_name=lname, email=email, password=pass1)
                user.save()
                if user is not None:
                    auth.login(request, user)
                    return render(request, 'index.html')

        else:
            messages.error(request, "Both password not match")
    else:
        return render(request, 'login.html')
# Create your views here.
