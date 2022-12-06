#!/usr/bin/python3
"""Test ats for expected behaviour and documentation"""
import inspect
import ats
import os
import pep8 as pycodestyle
import unittest
from unittest import mock
ats = src.ats.check_match
ats_doc = src.ats.__doc__

class Test_ats_Docs(unittest.TestCase):
    """Tests to check the documentation and style of ats"""

    @classmethod
    def setup(self):
        """Set up for docstring tests"""
        self.ats_funcs = inspect.getmembers(ats, inspect.isfunction)
        print("Start setup...")

    def test_pep8_conformance(self):
        """Test that src/ats.py conforms to PEP8."""
        for path in ['src/ats.py', 'test/test_ats.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_ats_docstring(self):
        """Test for the existence of docstring in ats"""
        for func in self.ats_funcs:
            with self.subTest(function=func):
                self.assertIsNot(func[1].__doc__, None, "{:s} method needs a docstring".format(fun[0]))
                self.assertTrue(len(func[1].__doc__) > 1, "{:s} method needs a docstring".format(func[0]))

class Test_ats(unittest.TestCase):
    """Test to check match"""

    def test_checkMatch(self):
        pass
