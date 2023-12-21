from .models import Skill, Profile
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def SearchProfiles(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    #print(search_query)

    # Extracting skills
    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                                 Q(short_intro__icontains=search_query) |
                                                 Q(skill__in=skills))

    # Sending data as a list
    data = [profiles,search_query]

    return data



def Profile_Home(request):
    # Util Search Method
    value = SearchProfiles(request)

    # Setting Page, Results
    page = request.GET.get('page')
    #print(page)
    results = 3
    paginator = Paginator(value[0], results)

    # Try catch block to Handle exceptions
    try:

        # Pagination based on Page Value
        profiles = paginator.page(page)

    except PageNotAnInteger:

        # Entered Page is not an Integer
        page = 1
        profiles = paginator.page(page)

    except EmptyPage:

        # Entered Page is Empty
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    # Custom range of Records / Pages to display
    custom_range = range(leftIndex, rightIndex)

    data = [profiles,paginator,custom_range,value[0]]

    return data
