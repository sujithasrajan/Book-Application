
# Create your models here.
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Book(models.Model):
    url = models.CharField('URL: ', max_length=200, blank=False, unique=True)
    name = models.CharField('Name: ', max_length=200)
    isbn = models.CharField('ISBN: ', max_length=500)
    publisher_year = models.IntegerField('Year of publication: ')
    publisher_name = models.CharField('Publisher: ', max_length=300)
    #owner = models.CharField('Owner: ', max_length=350)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


