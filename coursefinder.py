import requests
import json
from time import sleep
import csv

#Get Average GPA For Given Course
def get_avg_gpa(university, subject, course):
	resp = requests.get("https://anaanu.com/api/v1/course?university=" + university + "&subject=" + subject + "&course=" + course)
	data = json.loads(resp.text)
	try:
		gpa = data["course"]["average"]["gpa"]
	except:
		gpa = "NULL"
	return gpa

# Get Input For University / Courses
school_name = input("Enter your University Anaanu ID:\n")
file_or_paste = ""
while file_or_paste != 'f' and file_or_paste != 'p':
	file_or_paste = input("Would you like to input from a file or would you like to paste course names? (f/p)\n")

if file_or_paste == 'f':
	file_name = input("File Name: \n")
	courseData = open(file_name, "r")
else:
	courseData = input("Paste Course Data \n")

# Request For Each Course
titles = courseData.read().split(",")
grades = []
for title in titles:
	subject, course = title.split(" ")
	print("Subject: " + subject + ", Course: " + course)
	gpa = get_avg_gpa(school_name, subject, course)
	print("GPA: ")
	print(gpa)
	grades.append(gpa)

# Write to File
with open('results.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(zip(titles, grades))

