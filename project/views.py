from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
Projects = [
    {
        'id': '1',
        'Title':'E commerce Website',
        'Description':'A Website for shoes'
    },
    {
        'id': '2',
        'Title': 'Portfolio Website',
        'Description': 'Website for Portfolio'
    },
    {
        'id': '3',
        'Title': 'Database Management Webstie',
        'Description': 'Database with Website'
    }
]





def Product(request):
    Project_List = Projects
    return render(request,'project/Home.html',{'projects':Projects})

def Products(request,pk):
    projectObj = None
    for i in Projects:
        if i['id'] == pk:
            projectObj = i
    return render(request,"project/Prod.html",{'context': projectObj})