from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Rest
from rest_framework.permissions import IsAuthenticated

# Importing Serializers
from .serializers import ProjectSerializer
from project.models import Project,Review


@api_view(['GET'])
def getRoutes(request):

    routes=[
        {'GET':'/api/projects'},
        {'GET': '/api/projects/id'},

        {'POST': '/api/projects/id/vote'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request,pk):
    print("USER : ",request.user)
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review , created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )
    review.value = data['value']
    review.save()

    project.getVoteCount

    print("Data: ",data)

    serializer = ProjectSerializer(project,many=False)
    return Response(serializer.data)