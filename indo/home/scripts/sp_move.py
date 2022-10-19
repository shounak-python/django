import csv
from home.models import Specialization

def run():
    fhand = open('home/specializations_data.csv')
    file = csv.reader(fhand)
    Specialization.objects.all().delete()
    next(file)
    for line in file:

        obj = Specialization(
            name = line[1],
            org = line[4],
            issue_date = line[5],
            cred = line[7],
            cred_link = line[8],
        )
        obj.save()
