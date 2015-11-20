import datetime
from christmas_list.models import Item, WishList
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        """
        Creates an optional argument of --limit to specify how many to return
        :param parser:
        :return:
        """
        parser.add_argument('--limit', type=int, help='Limit the results',
                            default=1)

    def handle(self, *args, **options):
        """
        This method is required to be overridden. It is the main source of code
        :param args:
        :param options:
        :return:
        """
        item = Item.objects.order_by('-created_at')[:options['limit']]
        a = User.objects.create_user(username='dingo4', password='a',
                                 email="dingo@dingo.com")

        self.stdout.write("Got chirp len of {}".format(len(item)))
        self.stdout.write("{} created".format(a.username))

        for wishlist in WishList.objects.all():
            if wishlist.expiration < datetime.date.today():
                pass #wishlist.is_expired = False
                for item in wishlist.item_set.all():
                    for pledge in item.pledge_set.all():
                        pass #refund