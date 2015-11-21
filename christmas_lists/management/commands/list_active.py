from django.core.management.base import BaseCommand
from christmas_lists.models import Item


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        al_items = Item.objects.all()
        for item in al_items:
            active = item.active_state
            if active == True and item.pledge_total > item.price:
                self.stdout.write("{} is reserved".format(item.wish_list.title))
                item.reserved = True
            else:
                self.stdout.write("{} is not reserved".format(item.wish_list.title))
                item.reserved = False

