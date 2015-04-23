from django.db import models

# Create your models here.


class Task(models.Model):
        # Customer feedback pager model
    task = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=100)
    status = models.IntegerField()
    time = models.DateTimeField()
    expiry = models.DateTimeField()
    expiry_status = models.BooleanField()


class Comment(models.Model):
        # Customer comment
    mark = models.CharField(max_length=10)
    comment = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
