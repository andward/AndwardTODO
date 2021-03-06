from django.views.decorators.csrf import csrf_exempt
from todo.models import Task, Comment
from todo.serializers import taskSerializer, commentSerializer, tagSeralizer, userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
import datetime


TASK_STATUS = {
    'top': 2,
    'todo': 0,
    'done': 1
}

@api_view(['POST'])
def createUser(request):
    user = User.objects.create_user(
        username=request['username'],
        email=request['username'])
    user.set_password(request['password'])
    user.save()
    serializer = userSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def taskList(request, status_filter=None):
    if status_filter and status_filter in TASK_STATUS.keys():
        tasks = Task.objects.filter(status=TASK_STATUS[status_filter])
    elif not status_filter:
        tasks = Task.objects.all()
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = taskSerializer(tasks.order_by("-id"), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def tagList(request):
    tags = Task.objects.values("tag").distinct()
    serializer = tagSeralizer(tags, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def createTask(request, status_filter=None):
    created_time = datetime.datetime.now()
    request.data['time'] = created_time
    request.data['expiry'] = created_time
    request.data['status'] = 0
    request.data['expiry_status'] = 0
    serializer = taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def taskDetail(request, task_id):
    try:
        task = Task.objects.get(id=int(task_id))
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = taskSerializer(task)
    return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def updateTask(request, task_id):
    try:
        task = Task.objects.get(id=int(task_id))
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = taskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def commentList(request, task_id=None):
    if task_id:
        comments = Comment.objects.filter(mark=task_id)
    elif not task_id:
        comments = Comment.objects.all()
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = commentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def createComment(request, task_id=None):
    created_time = datetime.datetime.now()
    request.data['time'] = created_time
    serializer = commentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
