from django.db import models

class Category(models.Model):
    """
    A model class describing a category of deanslisting.
    """
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)


#TODO Subcategory class?

#class Post(models.Model):