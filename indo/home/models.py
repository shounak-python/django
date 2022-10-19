from django.db import models

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=100, default="")
    org = models.CharField(max_length=100, default="")
    issue_date = models.DateField(default="")
    cred = models.CharField(max_length=100, default="")
    cred_link = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=100, default="")
    grade = models.FloatField()
    org = models.CharField(max_length=100, default="")
    issue_date = models.DateField(default="")
    cred = models.CharField(max_length=100, default="")
    cred_link = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name