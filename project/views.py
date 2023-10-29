from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  Project
from .forms import ProjectForm


# Create your views here.

def Product(request):
    project_List = Project.objects.all()
    return render(request,'project/Home.html',{'projects': project_List})

def Products(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    if tags is None:
        print("NO TAGS")
    print(tags)
    return render(request,"project/Prod.html",{'project': projectObj,
                                               'tags':tags})


############# C R U D ######################

def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Product')

    context = {'form':form}
    return render(request,'project/project_form.html',context)


def updateProject(request,pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES ,instance=project)
        if form.is_valid():
            form.save()
            return redirect('Product')

    context = {'form':form}
    return render(request,'project/project_form.html',context)



def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return  redirect('Product')
    return render(request,'project/Delete_template.html', {'obj':project})
