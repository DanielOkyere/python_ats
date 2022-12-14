#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
from contextlib import redirect_stdout
import inspect
import io
import os
import pep8
import unittest
ATSCommand = console.ATSCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the ATSCommand class docstring"""
        self.assertIsNot(ATSCommand.__doc__, None,
                         "ATSCommand class needs a docstring")
        self.assertTrue(len(ATSCommand.__doc__) >= 1,
                        "ATSCommand class needs a docstring")


class TestConsoleCommands(unittest.TestCase):
    """Class to test functionality of console commands"""
    @classmethod
    def setUpClass(cls):
        """Create command console to test with"""
        cls.cmdcon = ATSCommand()

    def setup(self):
        """Create in memory buffer to caputure stdout"""
        self.output = io.StringIO()

    def tearDown(self):
        """Close in memory buffer after test completes"""
        self.output.close()
