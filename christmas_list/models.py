from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class WishList(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50, null=True, blank=True)
    expiration = models.DateField()
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}'s wishlist".format(self.user.username)


class Item(models.Model):
    wish_list = models.ForeignKey(WishList)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    source_url = models.URLField()
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def total_pledged(self):
        total = self.pledge_set.all().aggregate(Sum('amount'))['amount__sum']
        if not total:
            return 0

        return total


    @property
    def amount_needed(self):
        return self.price - self.total_pledged


class Pledge(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    charge_id = models.CharField(max_length=50, null=True)
    is_refunded = models.BooleanField(default=False)
    pledged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}'s pledge: ${}".format(self.user, self.amount)
