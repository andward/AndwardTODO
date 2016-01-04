#! /usr/bin/python2.6

from django.conf.urls.defaults import *
from django.conf.urls import url
from views import task, signup, api
from action import *
from todo.models import *
import django.contrib.auth
from django.contrib import admin
from rest_framework.authtoken import views

admin.autodiscover()

# Regular URL patterns
urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                        'document_root': settings.STATIC_PATH}),
                       (r'^static/media/(?P<path>.*)$', 'django.views.static.serve', {
                        'document_root': settings.MEDIA_ROOT}),
                       (r'^admin/', admin.site.urls),
                       (r'^task/(.*)/(.*)$', httpMethod, {
                        'GET': task.getTask,
                        'POST': task.postTask}),
                       (r'^accounts/login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'login.html'}),
                       (r'^accounts/logout/$', signup.logout),
                       (r'^accounts/signup/$', httpMethod, {
                        'GET': signup.getRegister,
                        'POST': signup.postRegister}),
                       url('', include('django_socketio.urls')),
                       )


# RESTful API patterns
urlpatterns += patterns('',
                        (r'api/tasks/(.*)$', httpMethod, {
                            'GET': api.taskList,
                            'POST': api.createTask}),
                        (r'api/task/(.*)$', httpMethod, {
                            'GET': api.taskDetail,
                            'PUT': api.updateTask}),
                        (r'api/comments/(.*)$', httpMethod, {
                            'GET': api.commentList,
                            'POST': api.createComment}),
                        (r'api/tags$', httpMethod, {
                            'GET': api.tagList}),
                        (r'api/createuser$', httpMethod, {
                            'POST': api.createUser}),
                        (r'^api/token-auth$', views.obtain_auth_token),
                        )
