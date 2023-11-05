from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def LoginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            print("User name Does not Exist")

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            print("Username or Password is incorrect")

    return render(request, 'users/login_register.html')


def LogoutUser(request):
    logout(request)
    return redirect('Login')

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    p_skills = profile.skill_set.exclude(description__exact="")
    s_skills = profile.skill_set.filter(description='')
    context = {
        "profile": profile,
        'p_skill': p_skills,
        's_skill': s_skills
    }
    return render(request, 'users/user_profile.html', context)
