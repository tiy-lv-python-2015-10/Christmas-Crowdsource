from django.core.management.base import BaseCommand
from christmas_lists.models import Item, WishList
from django.utils import timezone


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        ###check is wishlist is expired
        for wi
