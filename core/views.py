from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Profile
from django.shortcuts import render, redirect

# Create your views here.

@login_required(login_url='signin')
def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    return render(request, 'index.html', {'user_profile' : profile})

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
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                authenticated_user = auth.authenticate(request)
                auth.login(request, authenticated_user)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'password not match!')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid Credentials!')
            return redirect('signin')
        else:
            auth.login(request, user)
            return redirect('/')

    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        profile_img = user_profile.profile_img if request.FILES.get('profile_image') is None else request.FILES.get('profile_image')
        bio = request.POST['bio']
        location = request.POST['location']

        user_profile.profile_img = profile_img
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()
        return redirect('settings')
    else:
        return render(request, 'settings.html', {'user_profile' : user_profile})

@login_required(login_url='signin')
def upload(request):
    pass
