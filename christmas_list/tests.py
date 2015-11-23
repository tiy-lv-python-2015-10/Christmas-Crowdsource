from christmas_list.models import WishList, Item, Pledge
from django.contrib.auth.models import User
from django.test import TestCase


class TestWishList(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='joe', email='joe@joe.com',
                                        password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-23',
                                                title='TestTitle'
                                                )

    # def test_close(self):
    #     self.wishlist.close()
    #     self.assertEqual(self.wishlist.is_expired, True)


class TestItem(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='joe', email='joe@joe.com',
                                        password='password')
        self.user2 = User.objects.create(username='joe2', email='joe2@joe.com',
                                         password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-23',
                                                title='TestTitle'
                                                )
        self.item = Item.objects.create(wish_list=self.wishlist,
                                        title='ItemTitle',
                                        price=50,
                                        source_url='www.google.com')
        self.pledge = Pledge.objects.create(user=self.user2,
                                            item=self.item,
                                            amount=10,
                                            charge_id='stripechargeid')

    def test_total_pledged(self):
        self.assertEqual(self.item.total_pledged, 10)

    def test_amount_needed(self):
        self.assertEqual(self.item.amount_needed, 40)

    # def test_refund_pledges(self):
    #     self.item.refund_pledges()
    #     self.assertEqual(self.item.is_closed, True)


class TestPledges(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='joe', email='joe@joe.com',
                                        password='password')
        self.user2 = User.objects.create(username='joe2', email='joe2@joe.com',
                                         password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-23',
                                                title='TestTitle'
                                                )
        self.item = Item.objects.create(wish_list=self.wishlist,
                                        title='ItemTitle',
                                        price=50,
                                        source_url='www.google.com')
        self.pledge = Pledge.objects.create(user=self.user2,
                                            item=self.item,
                                            amount=10,
                                            charge_id='stripechargeid')
    # def test_refund(self):
    #     self.pledge.refund()
    #     self.assertEqual(self.pledge.is_refunded, True)
