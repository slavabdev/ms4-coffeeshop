from django.db import models
from products.models import Product
from users.models import UserProfile


class Review(models.Model):
    '''Creating review model  '''
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=False, blank=False)
    review_title = models.CharField(max_length=200, blank=False, default='')                               
    review_body = models.CharField(max_length=400, blank=False, default='')
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_body
