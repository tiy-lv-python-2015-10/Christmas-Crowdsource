from django.core.management.base import BaseCommand
from christmas_lists.models import Item, WishList
from django.utils import timezone


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        ###check is wishlist is expired
        all_lists = WishList.objects.all()
        for wishlist in all_lists:
            time_left = wishlist.expiration_date - timezone.now()
            if timezone.now() > wishlist.expiration_date:
                self.stdout.write("{} is expired it still has {} ".format(wishlist.title))
                wishlist.expired = True
            else:
                self.stdout.write("{} is not expired. It still has {} until it does".format(wishlist.title, time_left))





