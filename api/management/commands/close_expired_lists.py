from christmas_list.models import WishList
from django.core.management import BaseCommand
from datetime import date


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        This method is required to be overridden. It is the main source of code
        :param args:
        :param options:
        :return:
        """
        count = 0
        for wishlist in WishList.objects.all():
            if wishlist.expiration <= date.today() and not wishlist.is_expired:
                wishlist.close()
                count += 1

        self.stdout.write("{} Lists closed".format(count))