#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from django import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.conf import settings
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from todo.models import *
from form import ContactForm
from django.template import RequestContext
import datetime
import simplejson
from django.core.paginator import Paginator, PageNotAnInteger
from errormsg import *
import socket
import smtplib
from email.mime.text import MIMEText


def httpMethod(request, *args, **kwargs):
    # Http method separate by POST and GET
    get = kwargs.pop('GET', None)
    post = kwargs.pop('POST', None)
    if request.method == 'GET' and get is not None:
        return get(request, *args, **kwargs)
    elif request.method == 'POST' and post is not None:
        return post(request, *args, **kwargs)
    raise Http404


def JSONFormat(data):
    return simplejson.dumps(data, ensure_ascii=False)



def modelValidator(func):
    # Validate model if empty
    if func:
        return func
    else:
        return ''


def dataValidator(data):
    # Validate data if empty
    if type(data) is str:          
        if str(data).strip() == '':
            return False
        else:
            return True
    else:
        return data


def SearchValidator(func):
    pass


def SearchBug(query):
    # Search bug by query
    query = query.strip().replace(" ", "").lower()
    if query.isdigit():
        list = BugList.objects.filter(bug_id=query)
    elif query in ["fixed", "duplicate", "notrepeatable", "workingasintended"]:
        list = BugList.objects.filter(status=query)
    else:
        list = BugList.objects.filter(sammary__icontains=query)
    if list:
        return [[item.bug_id, item.status, item.sammary, item.comment] for item in list]
    else:
        return "none"


def timeStamp():
    return datetime.datetime.now()


def Pagination(objects, count, page):
    # Django pagination
    if objects:
        paginator = Paginator(objects, count)
        try:
            item = paginator.page(int(page))
        except PageNotAnInteger:
            item = paginator.page(1)
        except:
            item = paginator.page(paginator.num_pages)
        else:
            return item


def getVisitorDomain(request):
    # Get visitor Domain name
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    domain = (socket.gethostbyaddr(ip))[0].split('.')[0]
    return ''.join([i for i in domain if not (i.isdigit() or i in '`~!@#$%^&*()_+-=.,/[]')])


def taskEmailNotification(request, todo, comment=None, new_owner=None, status=None):
    # email notification for new TODO and its comment
    receiver = request.user.username
    user_email = User.objects.get(username=receiver).email
    if comment:
        email_text = "{0} has submitted a comment:\n\n{1}".format(receiver, comment)
        cc_email_addr = 'someone@domain.com'
    elif new_owner:
        email_text = "TODO: {0}\n\nhas been reassigned to {1}".format(todo, new_owner)
        try:
            cc_email_addr = User.objects.get(username=new_owner).email
        except:
            cc_email_addr = new_owner + '@domain.com'
    elif status:
        email_text = "{0} has marked it as {1}".format(receiver, status)
        cc_email_addr = 'someone@domain.com'
    else:
        email_text = "{0} has submitted a TODO:\n\n{1}".format(receiver, todo)
        cc_email_addr = 'someone@domain.com'
    signature = "\n\nTo check TODO, visit Andward.TODO site"
    msg = MIMEText(email_text + signature)
    msg['Subject'] = 'TODO: {}'.format(todo)
    from_email_addr = 'someone@domain.com'
    to_email_addr = user_email
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['CC'] = cc_email_addr
    mail = smtplib.SMTP('localhost')
    mail.sendmail(from_email_addr, [
                  to_email_addr, cc_email_addr], msg.as_string())
    mail.quit()
