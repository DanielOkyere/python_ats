## Background
The process of looking for a new job is in itself a full-time job.
There is an overwhelming amount of job postings and many times it is difficult to determine which jobs are the best matches to your skills and preferences.
It is important to do some research about the jobs before applying and furthermore, before accepting a job offer. On the other hand, job postings also receive an overwhelming amount of applications, and it is well-known[citation needed] that the companies use Application Tracking Systems (ATS) to weed out those candidates that are not a good match for the job. The basic idea is that the ATS searches the applicant's resume for predetermined keywords and for a particular language (mostly hard and soft skills) and then only saves those resumes with the highest match. For this reason, each time that you want to apply for a job, you should change your resume to emphasize those things that the company is looking for. To put an example, if I am looking into a data science job, I should emphasize the work that I have done working with data, while if it is a machine learning job, then I should emphasize in my resume the machine learning algorithms that I have used. This all sounds simple enough, and it sounds that you would just need a small set of resumes and use a different one for each type of job. However, the job postings are all different, and some of them use some words more than others, and your resume should match that language too.

To help job seekers "beat" the ATS, we have developed a python program that 
1) looks for hard skills (e.g. "Python", "Programming") and soft skills (e.g. "Communication", "Team Work") in a job description and in your current resume, and tells you how many times it is mentioned on each, and
2) Looks for the common words or phrases that are used in the job description (e.g. "data","experience","excellent") and tells you how many times it is written in the job description and how many times it is written in your resume. Given this data, the goal is to modify your resume to look as similar as possible to the job description.

If you would like to try it out, all you would need to do is download the code from my github [here](github.com/DanielOkyere/python_ats), make a txt file with the job description, and make a txt file with your resume. Put all of the files in the same folder, and then run `ats file_name` entering the job description file and the resume as parameters in standard input. In other words:

## Project was completed using
- Python
- Pep8
- Flask
- Unittest

## General Requirement
- Use python3 to run most of the files
- All files should begin with `#!/usr/bin/env python3`
- Use `Pep8` Style of coding

## Environment Variables
- ATS_DB_USER 
- ATS_DB_PWD 
- ATS_DB_HOST 
- ATS_DB_NAME

## Example
```commandline
$ cd python_ats
$ cd src

$ ./ats resume.txt job_desc.txt

```
## Demo
The project can be found live on [www.danielokyere.tech/python_ats/home](#)

## Test
To test this application the following packages are need
- Nltk Packages
- Unittest

Test can be run with in root directory with b
```bash
ATS_DB_USER=daniel ATS_DB_PWD=dan13l ATS_DB_HOST=localhost ATS_DB_NAME=python_ats python3 -m unittest discover test
```

## Project Management
Currently all user stories are being handled by team using the current trello board for the project. It can be viewed [here](https://trello.com/invite/b/4MqO3faK/ATTI747d5b3c69b03796c7765c207a6949987A05C02D/free-application-tracking-system)

## Authors
- **Daniel K. Okyere**
- **Gabriel Ahiamata**
- **Derrick Ahortu**

## Roadmap
- Picture to text feature
- PWA services