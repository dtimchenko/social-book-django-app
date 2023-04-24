from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordrepeat = request.POST['passwordrepeat']

        if password == passwordrepeat:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists!')
                return redirect('signup')
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'password not match!')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
