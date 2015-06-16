"""
Unittest for Task model
"""

from django.test import TestCase
from action import *
import datetime
import models
from django.core.exceptions import *


class TaskTest(TestCase):

    def setUp(self):
        """
        Create new task
        """
        Task.objects.create(
            task='new_task',
            name='people1',
            tag='test_tag',
            status=0,
            time=timeStamp(),
            expiry=datetime.datetime.strptime("1/1/2015", "%m/%d/%Y"),
            expiry_status=0
        )
        self.new_task = Task.objects.get(task='new_task')

    def test_new_task_created(self):
        self.assertEqual(self.new_task.status, 0)
        self.assertEqual(self.new_task.name, 'people1')
        self.assertEqual(self.new_task.tag, 'test_tag')
        self.assertEqual(self.new_task.expiry_status, 0)

    def test_update_task(self):
        self.new_task.name = 'people2'
        self.new_task.status = 1
        self.new_task.expiry_status = 1
        self.new_task.save()
        self.assertEqual(self.new_task.name, 'people2')
        self.assertEqual(self.new_task.status, 1)
        self.assertEqual(self.new_task.expiry_status, 1)
        self.assertEqual(self.new_task.tag, 'test_tag')

    def test_delete_task(self):
        self.new_task.delete()
        with self.assertRaises(ObjectDoesNotExist):
            task = Task.objects.get(task='new_task')


class CommentTest(TestCase):

    def setUp(self):
        """
        Create new Comment
        """
        Comment.objects.create(
            mark='1',
            comment='new_comment',
            name='people1',
            time=timeStamp())
        self.new_comment = Comment.objects.get(comment='new_comment')

    def test_new_comment_created(self):
        self.assertEqual(self.new_comment.mark, '1')
        self.assertEqual(self.new_comment.name, 'people1')

    def test_delete_comment(self):
        self.new_comment.delete()
        with self.assertRaises(ObjectDoesNotExist):
            comment = Comment.objects.get(comment='new_comment')
