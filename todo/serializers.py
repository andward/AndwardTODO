from rest_framework import serializers
from models import Task, Comment


class taskSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=5000)
    name = serializers.CharField(max_length=50)
    tag = serializers.CharField(max_length=100)
    status = serializers.IntegerField()
    time = serializers.DateTimeField()
    expiry = serializers.DateTimeField()
    expiry_status = serializers.BooleanField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, task, validated_data):
        task.task = validated_data.get('task', task.task)
        task.name = validated_data.get('name', task.name)
        task.tag = validated_data.get('tag', task.tag)
        task.status = validated_data.get('status', task.status)
        task.time = validated_data.get('time', task.time)
        task.expiry = validated_data.get('expiry', task.expiry)
        task.expiry_status = validated_data.get('expiry_status', task.expiry_status)
        task.save()
        return task


class commentSerializer(serializers.Serializer):
    mark = serializers.CharField(max_length=10)
    comment = serializers.CharField(max_length=1000)
    name = serializers.CharField(max_length=50)
    time = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, comment, validated_data):
        comment.mark = validated_data.get('mark', comment.mark)
        comment.comment = validated_data.get('comment', comment.comment)
        comment.name = validated_data.get('name', comment.name)
        comment.time = validated_data.get('time', comment.time)
        comment.save()
        return comment
