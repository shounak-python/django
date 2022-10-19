import csv
from home.models import Courses

def run():
    fhand = open('home/course_data.csv')
    file = csv.reader(fhand)
    Courses.objects.all().delete()
    next(file)
    for line in file:

        obj = Courses(
            name = line[1],
            grade = line[2],
            org = line[4],
            issue_date = line[5],
            cred = line[7],
            cred_link = line[8],
        )
        obj.save()