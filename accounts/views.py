from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=user_name).exists():
            print("user name is already taken!")
            messages.success(request, user_name + " is not available!")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            print("email already taken!")
            messages.info(request,email+ " already taken!")
            return redirect('register')
        elif password1 != password2:
            print("password not matching...")
            messages.info(request, "password are not matching!")
            return redirect('register')
        else:
            user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
        return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("login successful!")
            return redirect('/')
        else:
            print("login unsuccessful!")
            messages.info(request, 'wrong user name/password')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')