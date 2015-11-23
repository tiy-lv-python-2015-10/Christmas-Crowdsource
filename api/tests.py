from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from christmas_list.models import WishList, Item, Pledge


class UserList(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe',
                                             email='test@test.com',
                                             password='password')

    def test_user_list(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('api_list_users')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        response_user_list = response.data['results'][0]
        self.assertEqual(response_user_list['username'], self.user.username)

    def test_create_user(self):
        url = reverse('api_create_user')
        data = {'username': 'bob', 'email': 'bob@bob.com', 'password': 'pwd',
                'profile': {}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.data['username'], 'bob')


class WishListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe',
                                             email='test@test.com',
                                             password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-25',
                                                title='Xmas list')

    def test_wishlist_list(self):
        url = reverse('api_list_create_wishlists')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        response_wishlist = response.data['results'][0]
        self.assertEqual(response_wishlist['title'], self.wishlist.title)

    def test_create_wishlist(self):
        url = reverse('api_list_create_wishlists')
        self.client.force_authenticate(user=self.user)
        data = {'title': 'TestWishList', 'expiration': '2015-12-25'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WishList.objects.count(), 2)
        self.assertEqual(self.user.id, response.data['user'])
        self.assertEqual(response.data['title'], 'TestWishList')

    def test_wishlist_by_user_id(self):
        url = reverse('api_list_create_wishlists')
        user2 = User.objects.create(username='user2', email='test2@test2.com',
                                    password='password')
        wishlist2 = WishList.objects.create(user=user2,
                                            expiration='2015-12-31',
                                            title='TestWishList2')
        response = self.client.get(url, {'user-id': user2.id}, format='json')
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_wishlist = response.data['results'][0]
        self.assertEqual(response_wishlist['user'], user2.id)

    def test_wishlist_detail(self):
        url = reverse('api_detail_update_wishlist',
                      kwargs={'pk': self.wishlist.id})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.wishlist.title)

    def test_wishlist_update(self):
        url = reverse('api_detail_update_wishlist',
                      kwargs={'pk': self.wishlist.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url,
                                   {"title": "New Title",
                                    "expiration": "2015-12-26"},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'New Title')

    def test_wishlist_delete(self):
        url = reverse('api_detail_update_wishlist',
                      kwargs={'pk': self.wishlist.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(WishList.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe',
                                             email='test@test.com',
                                             password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-25',
                                                title='Xmas list')
        self.item = Item.objects.create(
            wish_list=self.wishlist,
            title='testItem',
            price=50,
            source_url='http://www.google.com'
        )

    def test_item_list(self):
        url = reverse('api_list_create_items')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        response_item = response.data['results'][0]
        self.assertEqual(response_item['title'], self.item.title)

    def test_create_item(self):
        url = reverse('api_list_create_items')
        self.client.force_authenticate(user=self.user)
        data = {
            'wish_list': 1,
            'title': 'testItem2',
            'price': 75,
            'source_url': 'http://www.something.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(response.data['user'], self.user.username)
        self.assertEqual(response.data['title'], 'testItem2')

    def test_item_detail(self):
        url = reverse('api_detail_update_item',
                      kwargs={'pk': self.item.id})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.item.title)

    def test_item_update(self):
        url = reverse('api_detail_update_item',
                      kwargs={'pk': self.item.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {"title": "New Title"},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'New Title')

    def test_wishlist_delete(self):
        url = reverse('api_detail_update_item',
                      kwargs={'pk': self.item.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(Item.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PledgeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe',
                                             email='test@test.com',
                                             password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-25',
                                                title='Xmas list')
        self.item = Item.objects.create(
            wish_list=self.wishlist,
            title='testItem',
            price=50,
            source_url='http://www.google.com'
        )
        self.pledge = Pledge.objects.create(user=self.user,
                                            item=self.item,
                                            amount=10,
                                            charge_id='stripe_id1')

    def test_pledge_list(self):
        url = reverse('api_list_pledges')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        response_pledge = response.data['results'][0]
        self.assertEqual(response_pledge['charge_id'], self.pledge.charge_id)
