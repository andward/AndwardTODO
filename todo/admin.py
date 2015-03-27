from django.contrib import admin
from todo.models import *

admin.site.register(Task)
admin.site.register(Comment)