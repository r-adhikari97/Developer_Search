from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreation, ProfileForm, SkillForm
# util file
from .utils import Profile_Home


# Create your views here.

@login_required(login_url="Login")
def User_account(request):
    profile = request.user.profile
    p_skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'p_skills': p_skills,
        'projects': projects,
    }
    return render(request, "users/account.html", context)


@login_required(login_url="Login")
def Edit_Profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('Account')

    context = {'form': form}
    return render(request, "users/edit_form.html", context)


def LoginUser(request):
    page = "login"
    context = {"page": page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, "User name Does not Exist")

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, 'users/login_register.html', context)


def LogoutUser(request):
    logout(request)
    messages.info(request, "User Successfully Logged out")
    return redirect('Login')


@csrf_protect
def register_user(request):
    page = "Register"
    form = CustomUserCreation()

    if request.method == "POST":
        print(request.POST)
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Holding a temp instance
            user.username = user.username.lower()
            # context = {'first_name':request.POST.first_name}
            user.save()
            messages.success(request, "Account Created Successfully")

            login(request, user)
            return redirect('Edit_Profile')

        else:
            messages.error(request, "An error Occurred During Registration")

    context = {"page": page,
               "form": form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    # Using Search_Profile Method
    data = Profile_Home(request)

    context = {'profiles': data[0],
               'paginator':data[1],
               'custom_url': data[2],
               'search_query':data[3]}
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


#############################  Skills   #############################

@login_required(login_url='Login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill Added to Account!")
            return redirect('Account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='Login')
def updateSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill Updated to Account!")
            return redirect('Account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='Login')
def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, "Skill Deleted from Account")
        return redirect('Account')

    context = {'obj':skill}
    return render(request, 'Delete_template.html', context)