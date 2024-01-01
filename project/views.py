from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Util file
from .utils import Projects_Home


# Create your views here.

# All Projects
def Product(request):

    data = Projects_Home(request)
    return render(request, 'project/Home.html', {'projects':data[0],
                                                 'paginator':data[1],
                                                 'custom_range':data[2],
                                                 'search_query': data[3]
                                                 })


# Specific Product
def Products(request, pk):
    projectObj = Project.objects.get(id=pk)
    print(projectObj.id)

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner =request.user.profile
        review.save()

        projectObj.getVoteCount

        # Update Project Vote Count
        messages.success(request,"Your Review is Submitted")
        return redirect('Products',projectObj.id)

    tags = projectObj.tags.all()
    if tags is None:
        print("NO TAGS")
    #print(tags)
    return render(request, "project/Prod.html", {'project': projectObj,
                                                 'tags': tags,
                                                 'form':form
                                                 })


############# C R U D ######################

@login_required(login_url="Login")
def createProject(request):

    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":

        # Checking Tags
        newTags = request.POST.get('newtags').replace(',', '').split()
        print("DATA: ", newTags)

        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            # Adding Tags
            for tag in newTags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('Product')

    context = {'form': form}
    return render(request, 'project/project_form.html', context)


@login_required(login_url="Login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    form = ProjectForm(instance=project)

    if request.method == "POST":
        newTags = request.POST.get('newtags').replace(',','').split()
        print("DATA: ", newTags)


        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newTags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            messages.success(request,"Project Updated Successfully !")
            return redirect('Product')


    context = {'form': form}
    return render(request, 'project/project_form.html', context)


@login_required(login_url="Login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('Product')
    return render(request, 'Delete_template.html', {'obj': project})
