#!/usr/bin/python3
"""Test ats for expected behaviour and documentation"""
from src import ats
import pep8 as pycodestyle
import unittest
import pathlib as pl


pep8s = pycodestyle.StyleGuide(quiet=True)


class Test_ats_Docs(unittest.TestCase):
    """Tests to check the documentation and style of ats"""

    def test_pep8_conformance_ats(self):
        """Test that src/ats.py conforms to PEP8."""
        result = pep8s.check_files(['src/ats.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_ats(self):
        """Test test_ats.py conforms to PEP8."""
        result = pep8s.check_files(['test/test_ats.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    
    def test_pep8_conformance_test_keyword_extract(self):
        """Test keyword_extract.py conforms to PEP8."""
        result = pep8s.check_files(['src/Keyword_Extractor.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_ats_docstring(self):
        """Test for the existence of docstring in ats"""
        self.assertIsNot(ats.__doc__, None,
                         "ats.py needs a docstring")
        self.assertIsNot(len(ats.__doc__) >= 1,
                         "ats.py needs a docstring")

class Test_ats(unittest.TestCase):
    """Test to check match"""

    def test_checkMatch(self):
        """Test for extracted words"""
        job_desc = "src/texts/job_desc.txt"
        resume = "src/texts/resume.txt"
        extracted_file = "src/tmp/Extracted_keywords.csv"
        ats.check_match(job_desc, resume)
        if not pl.Path(extracted_file).resolve().is_file():
            raise AssertionError("File does not exist: {}".format(extracted_file))
