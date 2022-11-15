#!/usr/bin/env python3
"""
Script for processing resume & job description
"""
from sys import argv
from Keyword_Extractor import Extractor


def check_match(resume, job_desc):
    k = Extractor(resume, job_desc)
    k.makeTable()
    k.sendToFile()
    k.printMeasures()


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: <ats> <resume> <job_desc>")
    else:
        check_match(argv[1], argv[2])
