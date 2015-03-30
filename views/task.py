#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from django import *
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from todo.models import *
from form import *
from action import *
from errormsg import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def getTask(request, url_type, type_name=None):
    """Get tasks seprated by 1.status 2.author 3.tag

    Args:
     request: Default arg of HTTP method
     author_name: author name catched in URL

    Return:
     1. Return status tasks if has author
     2. Return status tasks if has tag
    """
    username = request.user.username
    task_all = Task.objects.order_by("-id")
    task_users = User.objects.all()
    if url_type == 'people' and type_name:
        task_todo = task_all.filter(
            status=0).filter(name=type_name)
        task_done = task_all.filter(
            status=1).filter(name=type_name)
        task_top = task_all.filter(
            status=2).filter(name=type_name)
    elif url_type == 'tag' and type_name == "ALL":
        task_todo = task_all.filter(
            status=0)
        task_done = task_all.filter(
            status=1)
        task_top = task_all.filter(
            status=2)
    elif url_type == 'tag' and type_name:
        task_todo = task_all.filter(
            status=0).filter(tag=type_name)
        task_done = task_all.filter(
            status=1).filter(tag=type_name)
        task_top = task_all.filter(
            status=2).filter(tag=type_name)
    task_summary = [
        {'name': 'TOP', 'value': task_top.count()},
        {'name': 'TODO', 'value': task_todo.count()},
        {'name': 'DONE', 'value': task_done.count()}]
    user_summary = [
        {'name': user,
         'value': task_all.filter(name=user).count()
         } for user in task_users]
    if len(task_done) > 10:
        task_done = task_done[:10]
    return render_to_response('task.html',
                              {'task_todo': task_todo,
                               'task_done': task_done,
                               'task_top': task_top,
                               'task_summary': task_summary,
                               'user_summary': user_summary,
                               'task_tag': getFullTagList(),
                               'users': task_users,
                               'current_user': username}
                              )


def getFullTagList():
    return [tag["tag"] for tag in Task.objects.values("tag").distinct()]


def postPattern():
    # Pattern of request POST method
    return {
        "new_task": addNewTask,
        "new_comment": addNewComment,
        "look_for_task": getTaskComment,
        "task_done": markTaskDone,
        "task_todo": markTaskTodo,
        "task_top": markTaskTop,
        "change_owner": reassignOwner,
        "expand_all_task": returnAllDoneTask
    }


@csrf_exempt
def postTask(request, *args, **kwargs):
    # Map method in request POST
    post_list = set(request.POST) & set(postPattern())
    if len(post_list):
        post = postPattern().get(post_list.pop(), "")
        return post(request, *args, **kwargs)


def addNewTask(request, url_type=None, type_name=None):
    # Ajax function: add new task
    username = request.user.username
    new_task = request.POST.get("task", "")
    tag = request.POST.get("task_tag", "")
    if dataValidator(new_task):
        p = Task(task=new_task,
                 name=username,
                 tag=tag,
                 status=0,
                 time=timeStamp()
                 )
        p.save()
        # taskEmailNotification(request=request, todo=new_task)
        if tag in getFullTagList():
            new_tag = 0
        else:
            new_tag = 1
        return HttpResponse(JSONFormat({
            "id": p.id,
            "time": p.time.strftime('%d %b %Y'),
            "username": username,
            "new_tag": new_tag
        }))
    else:
        return HttpResponse(JSONFormat(""),
                            content_type='application/json'
                            )


def reassignOwner(request, url_type=None, type_name=None):
    # Ajax function: reassign task to new owner
    new_owner = request.POST.get("new_owner", "")
    task_id = request.POST.get("task_id", "")
    task = Task.objects.get(id=int(task_id))
    if dataValidator(new_owner):
        task.name = new_owner
        task.save()
        # taskEmailNotification(
        #    request=request, todo=task.task, new_owner=new_owner)
        return HttpResponse(JSONFormat({
            "new_owner": new_owner
        }))
    else:
        return HttpResponse(JSONFormat(""),
                            content_type='application/json'
                            )


def markTaskDone(request, url_type=None, type_name=None):
    # Ajax function: mark task as DONE
    task = Task.objects.get(
        id=request.POST.get("task_id", ""))
    task.status = 1
    task.save()
    # taskEmailNotification(
    #    request=request, todo=task.task, status='DONE')
    return HttpResponse(JSONFormat("Mark DONE succeed"),
                        content_type='application/json'
                        )


def markTaskTodo(request, url_type=None, type_name=None):
    # Ajax function: mark task as TODO
    task = Task.objects.get(
        id=request.POST.get("task_id", ""))
    task.status = 0
    task.save()
    # taskEmailNotification(
    #    request=request, todo=task.task, status='TODO')
    return HttpResponse(JSONFormat("Mark TODO succeed"),
                        content_type='application/json'
                        )


def markTaskTop(request, url_type=None, type_name=None):
    # Ajax function: mark task as High priority
    task = Task.objects.get(
        id=request.POST.get("task_id", ""))
    task.status = 2
    task.save()
    # taskEmailNotification(
    #    request=request, todo=task.task, status='High Priority')
    return HttpResponse(JSONFormat("Mark TOP succeed"),
                        content_type='application/json'
                        )


def addNewComment(request, url_type=None, type_name=None):
    # Ajax function: add comment for selected task
    username = request.user.username
    new_comment = request.POST.get("task_comment", "")
    task_id = request.POST.get("task_id", "")
    task = Task.objects.get(id=int(task_id))
    if dataValidator(new_comment):
        p = Comment(mark=task_id,
                    comment=new_comment,
                    name=username,
                    time=timeStamp()
                    )
        p.save()
        # taskEmailNotification(
        #    request=request, todo=task.task, comment=new_comment)
        return HttpResponse(JSONFormat(username))
    else:
        return HttpResponse(JSONFormat(""),
                            content_type='application/json'
                            )


def getTaskComment(request, url_type=None, type_name=None):
    # Ajax function: return all task
    comments = Comment.objects.filter(
        mark=request.POST.get("task_id", ""))
    if comments:
        return HttpResponse(JSONFormat([{
            "comment": item.comment,
            "username": item.name,
            "time": item.time.strftime('%d %b %Y')
        } for item in comments]))
    else:
        return HttpResponse(JSONFormat(""),
                            content_type='application/json'
                            )


# def scanNewTask(request, url_type, type_name):
# Ajax function: real time scan new TODO
#     if url_type == 'tag' and type_name == 'ALL':
#         max_id = request.POST.get("scan_id", "")
#         if ((Task.objects.all().order_by("-id"))[0]).id > int(max_id):
#             return HttpResponse(simplejson.dumps('1'),
#                                 mimetype='application/javascript')
#         else:
#             return HttpResponse(simplejson.dumps('0'),
#                                 mimetype='application/javascript')
#     else:
#         return HttpResponse(simplejson.dumps('0'),
#                             mimetype='application/javascript')


# def returnNewTask(request, url_type, type_name):
# Ajax function: real time return new TODO
#     if url_type == 'tag' and type_name == 'ALL':
#         max_id = request.POST.get("return_id", "")
#         tasks = Task.objects.filter(id__gt=int(max_id))
#         if tasks:
#             return HttpResponse(simplejson.dumps(
#                 [[item.id, item.tag, item.task, item.name] for item in tasks]),
#                 mimetype='application/javascript')
#         else:
#             return HttpResponse(simplejson.dumps(''),
#                                 mimetype='application/javascript')
#     else:
#         return HttpResponse(simplejson.dumps(''),
#                             mimetype='application/javascript')


def returnAllDoneTask(request, url_type, type_name):
    if url_type == "tag" and type_name == "ALL":
        task_done = Task.objects.filter(
            status=1).order_by("-id")
    elif url_type == "tag" and type_name:
        task_done = Task.objects.filter(
            status=1).filter(tag=type_name).order_by("-id")
    return HttpResponse(JSONFormat([{
        "id": item.id,
        "tag": item.tag,
        "task": item.task,
        "username": item.name,
        "time": item.time.strftime('%d %b %Y')
    } for item in task_done]),
        content_type='application/json'
    )
