#!/usr/bin/env python3

"""
This is a flask server for my ats
"""
from flask import Flask, render_template
from flask import request
from src.Keyword_Extractor import Extractor
import docx2txt
import uuid

app = Flask(__name__)
document_id = uuid.uuid4()

@app.errorhandler(404)
def page_not_found(e):
    """ Renders the page not found """
    return render_template('404.html'), 404

@app.route('/ats', strict_slashes=False, methods=['GET', 'POST'])
def ats():
    """ Renders the ATS Page """
    if request.method == 'POST':
        # read data to temp files
        resume = request.form['resume']
        txt_resume = open("./src/texts/resume.txt", "w+")
        txt_resume.write(resume)
        job_desc = request.form['job_desc']
        txt_jd = open("./src/texts/job_desc.txt", "w+")
        txt_jd.write(job_desc)

        # close written files
        txt_jd.close()
        txt_resume.close()

        # perform keyword extraction
        k = Extractor('./src/texts/job_desc.txt', './src/texts/resume.txt')
        k.makeTable()
        table = k.sendCumlatives()
        return render_template('ats_home.html', table=table, doc_id=document_id)
    else:
        return render_template('ats_home.html', table=None, doc_id=document_id)

@app.route("/home", strict_slashes=False)
def home():
    """Returns Landing Page"""
    return render_template('landing.html', doc_id=document_id)

@app.route("/ats/about-us", strict_slashes=False)
def about():
    """Return about Page"""
    return render_template('about.html', doc_id=document_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
