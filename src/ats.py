#!/usr/bin/env python3
"""
Script for processing resume & job description
"""
from sys import argv
from src.Keyword_Extractor import Extractor


def check_match(resume, job_desc):
    """
    check_match - checks the resume with the job_description
    submitted.
    It prints out measures to file and to table

    Args:
        resume: String - Text of resume content
        job_desc: String - Text of job description
    Return:
        None
    """
    k = Extractor(resume, job_desc)
    k.makeTable()
    k.sendToFile()
    k.printMeasures()


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: <ats> <resume> <job_desc>")
    else:
        check_match(argv[1], argv[2])
