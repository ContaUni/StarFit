from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')    
        email = request.POST.get('email')    
        password = request.POST.get('password')    
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')
        date_birth = request.POST.get('date_birth')
        
        existing_user = User.objects.filter(email=email).first()
        if existing_user:
            print('Usuario existente')
            return redirect('login')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            profile = UserProfile.objects.create(
                user=user,
                date_birth=date_birth
            )
            profile.save()
            print('Usuario criado com sucesso!')
            return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,  password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            print('Usuario inexistente.')
            return redirect('signup')
    return render(request, 'login.html')