from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from api.views import APIListCreateItem, APIListCreateWishList, APIListCreatePledge, APIDetailUpdateWishList, \
    APIDetailUpdateItem, APIDetailUpdatePledge
from christmas_lists.models import WishList, Item, Pledge


class WishListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test1', email='test@test.com', password='password')

    def test_wish_list(self):
        wishlist = WishList.objects.create(title='WishList Title', list_url="http://www.christmas.com",
                                           expiration_date="2015-12-25", user=self.user)
        url = reverse('api_wishlist_list_create')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_wishlist = response.data['results'][0]
        self.assertEqual(response_wishlist['title'], wishlist.title)

    def test_create_wish_list(self):
        url = reverse('api_wishlist_list_create')
        data = {"title": 'WishList Title', "list_url": "http://www.christmas.com",
                "expiration_date": "2015-12-25", "user": "self.user"}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WishList.objects.count(), 1)
        self.assertEqual(self.user.id, response.data['user'])



class ItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test1', email='test@test.com', password='password')
        pledge = WishList.objects.create(title='WishList Title', list_url="http://www.christmas.com",
                                           expiration_date="2015-12-25", user=self.user)

    def test_item(self):
        wishlist = WishList.objects.create(title='WishList Title', list_url="http://www.christmas.com",
                                       expiration_date="2015-12-25", user=self.user)
        item = Item.objects.create(title='Item Title',  wish_list= wishlist,
            item_url= "http://www.newegg.com/Product/Product.aspx?Item=N82E16832106454",
            image_url = "http://images10.newegg.com/ProductImage/32-106-454-01.jpg",
            description = "I want this to paint",
            price= "300.00")
        url = reverse('api_item_list_create')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_item = response.data['results'][0]
        self.assertEqual(response_item['title'], item.title)

    def test_create_item(self):
        url = reverse('api_item_list_create')
        data = {
            "item_url": "http://www.newegg.com/Product/Product.aspx?Item=N82E16832106454",
            "image_url": "http://images10.newegg.com/ProductImage/32-106-454-01.jpg",
            "title": "Item Title",
            "description": "I want this to paint",
            "price": "300.00",}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(self.user.id, response.data['user'])



class PledgeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test1', email='test@test.com', password='password')
        self.wishlist = WishList.objects.create(title='WishList Title', list_url="http://www.christmas.com",
                                       expiration_date="2015-12-25", user=self.user)
        self.item = Item.objects.create(title='Item Title',  wish_list= self.wishlist,
            item_url= "http://www.newegg.com/Product/Product.aspx?Item=N82E16832106454",
            image_url = "http://images10.newegg.com/ProductImage/32-106-454-01.jpg",
            description = "I want this to paint",
            price= "300.00")

    def test_pledge(self):
        pledge = Pledge.objects.create(user=self.user, item=self.item, pledge_amount = 100)
        url = reverse('api_pledge_list_create')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_pledge = response.data['results'][0]
        self.assertEqual(response_pledge['user'], self.user)

    def test_create_pledge(self):
        url = reverse('api_pledge_list_create')
        data = {"user": 'self.user', "item":"self.item", "pledge_amount" : "100"}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pledge.objects.count(), 1)
        self.assertEqual(self.user.id, response.data['user'])
