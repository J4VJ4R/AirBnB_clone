#!/usr/bin/python3
"""Test for file storage"""
import models
from models.review import Review
import os
import unittest
from models.base_model import BaseModel
"""import json"""


class TestReview(unittest.TestCase):
    """we start the test"""
    def test_docstring(self):
        '''test if function, methods, classes and modules have doc
        string'''
        msj = "Module doesnt have docstring"
        obj = models.review.__doc__
        self.assertIsNotNone(obj, msj)  # Modules
        msj = "Classes doesnt have docstring"
        self.assertIsNotNone(obj, msj)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to executable'''

        is_read_true = os.access('models/review.py', os.R_OK)
        self.assertTrue(is_read_true)

        is_write_true = os.access('models/review.py', os.W_OK)
        self.assertTrue(is_write_true)

        is_exec_true = os.access('models/review.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check if my_models is an instance of BaseModel'''
        my_model = Review()
        self.assertIsInstance(my_model, Review)
