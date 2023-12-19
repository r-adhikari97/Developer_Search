from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


#### Search Project Using Search Bar ###

def Search_Project(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    # Searching via tags
    Tags = Tag.objects.filter(name__icontains=search_query)

    # Setting up Search Parameters
    project_List = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=Tags)
    )

    # Sending a list of data back
    data = [project_List,search_query]

    return data


def Projects_Home(request):
    # Util Search Method
    value = Search_Project(request)

    # Setting Page, Results
    page = request.GET.get('page')
    print(page)
    results = 3
    paginator = Paginator(value[0], results)

    # Try catch block to Handle exceptions
    try:

        # Pagination based on Page Value
        projects = paginator.page(page)

    except PageNotAnInteger:

        # Entered Page is not an Integer
        page = 1
        projects = paginator.page(page)

    except EmptyPage:

        # Entered Page is Empty
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    # Custom range of Records / Pages to display
    custom_range = range(leftIndex, rightIndex)

    data = [projects,paginator,custom_range,value[0]]

    return  data
