from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    category_img = models.ImageField(upload_to='photo/categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')

    def __str__(self):
        return self.name