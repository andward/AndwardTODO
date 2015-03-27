#!/usr/bin/env python
#coding=utf-8
import unittest
class WebTestCase(unittest.TestCase):
    def SetUp(self):
        self.widget = Widget("The widget!")
        