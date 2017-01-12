from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
    """
    A model class describing a category of deanslisting.
    """
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)
    parent_category = models.ForeignKey('self', null=True, blank=True)
    parent_category_name = models.ForeignKey('self', null=True, max_length=100, related_name='category_name')
    # Subcategories can be represented by assigning an existing Category
    #  instance as another's parent_category

    def save(self, *args, **kwargs):
    	# newly created category, set slug
    	if not self.id:
    		self.slug = slugify(self.name)

    	super(Category, self).save(*args, **kwargs)


class Post(models.Model):


    title = models.CharField(u'Title', max_length=50)
    price = models.CharField(u'Price', max_length=10)
    description = models.TextField(u'Description', blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(u'Category', max_length=10)

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='parent_category')
    #category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='parent_category_name')
    #subcategory = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='id')
    #subcategory_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='name')





    








