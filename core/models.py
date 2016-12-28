from django.db import models

class Category(models.Model):
    """
    A model class describing a category of deanslisting.
    """
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)


#TODO Subcategory class?
class Subcategory(models.Model):
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)

class User(models.Model):
    
    """
    Model class for user
    """
    
    # Firstname/lastname? Or is that unnecessary
    first_name = models.CharField(u'FirstName', max_length=30)
    last_name = models.CharField(u'FirstName', max_length=30)
    username = models.CharField(u'Username', max_length=30)
    email = models.CharField(u'Email', max_length=30)
    password = models.CharField(u'Password', max_length=30)
    # TODO: Password authentication

class SalePost(models.Model):
    
    """
    Model class for an item that is for sale
    """
    
    title = models.CharField(u'Title', max_length=50)
    #slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
