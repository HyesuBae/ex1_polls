from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)    # varchar(100)
    authors = models.ManyToManyField('Author')  # integer
    publisher = models.ForeignKey('Publisher')  # integer
    publication_date = models.DateField()       # date

    def __unicode__(self): # __str__ on Python 3
        return self.title


class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.URLField()

    def __unicode__(self):
        return self.name
