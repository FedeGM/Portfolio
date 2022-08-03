from distutils.command.upload import upload
from pydoc import describe
from django.db import models
from django.db.models.fields import TextField,CharField, DateField, EmailField, IntegerField, URLField
from django.db.models.fields.files import ImageField, FileField


class Project(models.Model):
    eventdate = DateField()
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/protfolio/images/')
    url = URLField(blank=True)

class WorkExperience(models.Model):
    startdate = DateField()
    enddate = DateField(blank=True)
    title = CharField(max_length=255)
    company = CharField(max_length=255)
    description = TextField()


