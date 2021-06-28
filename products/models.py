from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    category_img = models.ImageField(upload_to='photo/categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    slug = AutoSlugField(max_length=200, unique=True, populate_from='name')
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)

    def __str__(self):
        return self.name
