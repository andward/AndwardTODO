from todo.models import *
from action import *


def checkTaskExpiration():
    current_time = timeStamp()
    tasks = Task.objects.filter(expiry_status=0)
    for task in tasks:
        if task.expiry < current_time:
            task.expiry_status = 1
            task.save()
