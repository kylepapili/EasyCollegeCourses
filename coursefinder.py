import requests
import json
from time import sleep
import csv
import argparse
import os
import sys
#Get Average GPA For Given Course
def get_avg_gpa(university, subject, course):
	resp = requests.get("https://anaanu.com/api/v1/course?university=" + university + "&subject=" + subject + "&course=" + course)
	data = json.loads(resp.text)
	try:
		gpa = data["course"]["average"]["gpa"]
	except:
		gpa = "NULL"
	return gpa

def main():
    #Parses argument files 
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', 
            help='Path to courses file')
    parser.add_argument('-id',action='store',help='Anaanu ID')
    args = parser.parse_args()
    if args.id is not None:
        school_name = str(args.id)
    else:
        school_name = input("Enter your University Anaanu ID:\n")
    if args.file is not None:
        file_name = str(args.file)
        if not os.path.isdir(file_name):
            print('The path specified does not exist')
            sys.exit()
        course_data = open(file_name, "r")
    else:
        course_data = input("Past course data \n")
    # Request For Each Course
    titles = course_data.read().split(",")
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

if __name__ == "__main__":
    main()
