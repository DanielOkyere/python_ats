#!/usr/bin/env python3

"""
This is a flask server for my ats
"""
from flask import Flask, render_template
from flask import request
from Keyword_Extractor import Extractor
import docx2txt

app = Flask(__name__)

@app.route('/ats', strict_slashes=False, methods=['GET', 'POST'])
def ats():
    """ Renders the ATS Page """
    if request.method == 'POST':
        # read data to temp files
        resume = request.form['resume']
        txt_resume = open("texts/resume.txt", "w+")
        txt_resume.write(resume)
        job_desc = request.form['job_desc']
        txt_jd = open("texts/job_desc.txt", "w+")
        txt_jd.write(job_desc)

        # close written files
        txt_jd.close()
        txt_resume.close()

        # perform keyword extraction
        k = Extractor('job_desc.txt', 'resume.txt')
        k.makeTable()
        table = k.sendCumlatives()
        return render_template('ats_home.html', table=table)
    else:
        return render_template('ats_home.html', table=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
    app.config['SECRET_KEY'] = '9dd21f5256b89957bd773445af45bad791fa258f72a3b04f'
