#! /usr/bin/python2.6

from django.conf.urls.defaults import *
from views import task, signup
from action import *
from todo.models import *
import django.contrib.auth
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                        'document_root': settings.STATIC_PATH}),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                        'document_root': settings.MEDIA_ROOT}),
                       (r'^admin/', admin.site.urls),
                       (r'^task/(.*)/(.*)$', httpMethod, {
                        'GET': task.getTask, 'POST': task.postTask}),
                       (r'^accounts/login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'login.html'}),
                       (r'^accounts/logout/$', signup.logout),
                       (r'^accounts/signup/$', httpMethod, {
                        'GET': signup.getRegister, 'POST': signup.postRegister}),
                       )
