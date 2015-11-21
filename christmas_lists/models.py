
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils import timezone

# Create your models here.
class WishList(models.Model):
    title = models.CharField(max_length=255)
    list_url = models.URLField(max_length=255)
    expiration_date = models.DateTimeField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class Item(models.Model):
    wish_list = models.ForeignKey(WishList)
    item_url = models.URLField(max_length=255)
    image_url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    reserved = False

    def __str__(self):
        return "{}".format(self.title)

    # # @property
    # # def total_pledge(self):
    #     all_pledges = self.pledge_set.all()
    #     total_pledge_amount = 0
    #     for pledge in all_pledges:
    #         total_pledge_amount += pledge.pledge_amount
    #     return total_pledge_amount

    @property
    def pledge_total(self):
        # agg = self.objects.aggregate(total_sum=Sum('pledge__pledge_amount'))
        # return agg.get('total_sum', None)
        all_pledges = self.pledge_set.all()
        total_pledge_amount = 0
        for pledge in all_pledges:
            total_pledge_amount += pledge.pledge_amount
        return total_pledge_amount


    @property
    def active_state(self):
        active = True
        today_date = timezone.now()
        # if self.pledge_total > self.price or today_date > self.wish_list.expiration_date:
        # if self.pledge_total > self.price
        if today_date > self.wish_list.expiration_date:
            self.active = False
        return self.active






class Pledge(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    pledge_amount = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.pledge_amount)



# user
# list creator
# pledger





# list_creator cant see pledgers




