from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class WishList(models.Model):
    title = models.CharField(max_length=255)
    list_url = models.URLField(max_length=255)
    expiration_date = models.DateTimeField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    wish_list = models.ForeignKey(WishList)
    item_url = models.URLField(max_length=255)
    image_url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Pledge(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    pledge_amount = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# user
# list creator
# pledger



# crud items
# crud list
# list_creator cant see pledgers




