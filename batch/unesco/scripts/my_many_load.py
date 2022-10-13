import csv
from unesco.models import Category, State, Region, Iso, Site


def run():
    fhand = open("unesco/whc-sites-2018-clean.csv")
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for item in reader:
        c, _ = Category.objects.get_or_create(name=item[7])
        s, _ = State.objects.get_or_create(name=item[8])
        r, _ = Region.objects.get_or_create(name=item[9])
        i, _ = Iso.objects.get_or_create(name=item[10])

        try:
            name=item[0]
        except:
            name=None

        try:
            description=item[1]
        except:
            description=None

        try:
            justification=item[2]
        except:
            justification=None

        try:
            year=int(item[3])
        except:
            year=None

        try:
            longitude=float(item[4])
        except:
            longitude=None

        try:
            latitude=float(item[5])
        except:
            latitude=None

        try:
            area_hectares=float(item[6])
        except:
            area_hectares=None


        site = Site(
            name=name,
            description=description,
            justification=justification,
            year=year,
            longitude=longitude,
            latitude=latitude,
            area_hectares=area_hectares,
            category=c,
            region=r,
            iso=i,
            state=s,
        )

        site.save()
