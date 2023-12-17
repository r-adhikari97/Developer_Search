from .models import Skill, Profile
from django.db.models import Q


def SearchProfiles(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    print(search_query)

    # Extracting skills
    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                                 Q(short_intro__icontains=search_query) |
                                                 Q(skill__in=skills))
    print(skills,profiles)

    return skills, profiles
