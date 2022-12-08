#!/usr/bin/python3
"""Test Keyword_Extractor for exepected behaviour and documentation"""
from src import Keyword_Extractor
from src import ats_flask
import pep8 as pycodestyle
import unittest
import pathlib as pl

pep8s = pycodestyle.StyleGuide(quiet=True)

class Test_Docs(unittest.TestCase):
    """Test to check the documentation and style of Keyword_Extractor.py and ats_flask.py"""

    def test_keywordExtractor_docstring(self):
        """Test for the existence of docstring in Keyword_Extractor"""
        self.assertIsNot(Keyword_Extractor.__doc__, 0, 
                         "Keyword_Extractor.py needs a docstring")

    def test_ats_flask(self):
        """Test for the existence of docstring in ats_flask.py"""
        self.assertIsNot(ats_flask.__doc__, 0,
                         "ats_flask.py needs a docstring")
