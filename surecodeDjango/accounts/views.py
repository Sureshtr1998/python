from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth



# Create your views here.

def logout(req):
    auth.logout(req)
    return redirect('/')
def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            return redirect("/")
        else:
            messages.info(req,"Invalid credentials")
            return redirect('login')
    else:
        return render(req, 'login.html')

def register(req):

    if req.method == 'POST':
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        password1 = req.POST['password1']
        password2 = req.POST['password2']
        email = req.POST['email']

        if password1 == password2:
            if User.objects.filter(username= username).exists():

                # print("Username taken")
                messages.info(req, "Username taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                # print("Email exists")
                messages.info(req, "Email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name,last_name=last_name)
                user.save()
                print("USER CREATED")
                messages.info(req, "Username created")
                return redirect('login')
        else:
            # print("Passowrd not matching")
            messages.info(req, "Password not matching")
            return redirect('register')

    else:
        return render(req, 'register.html')