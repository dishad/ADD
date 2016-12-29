from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    A model class describing a category of deanslisting.
    """
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)
    parent_category = models.ForeignKey('self', null=True, blank=True)
    # Subcategories can be represented by assigning an existing Category
    #  instance as another's parent_category


class SalePost(models.Model):
    
    """
    Model class for an item that is for sale
    """
    
    title = models.CharField(u'Title', max_length=50)
    #slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)