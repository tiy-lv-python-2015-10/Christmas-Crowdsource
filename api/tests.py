from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from christmas_list.models import WishList


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
        data = {}

class ItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe',
                                             email='test@test.com',
                                             password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-25',
                                                title='Xmas list')

class PledgeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe',
                                             email='test@test.com',
                                             password='password')
        self.wishlist = WishList.objects.create(user=self.user,
                                                expiration='2015-12-25',
                                                title='Xmas list')


# class ChirpTests(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_user('test1', email='test@test.com',
#                                              password='password')
#
#
#     def test_chirp_list(self):
#         chirp = Chirp.objects.create(title='Chirp Title',
#                                      message='Chirp Message', author=self.user)
#         url = reverse('api_chirp_list_create')
#         response = self.client.get(url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
#         response_chirp = response.data['results'][0]
#         self.assertEqual(response_chirp['title'], chirp.title)
#
#     def test_chirp_list_request(self):
#         chirp = Chirp.objects.create(title='Chirp Title',
#                                      message='Chirp Message', author=self.user)
#         url = reverse('api_chirp_list_create')
#         view = ListCreateChirp.as_view()
#         factory = APIRequestFactory()
#         request = factory.get(url, {}, format='json')
#         response = view(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
#         response_chirp = response.data['results'][0]
#         self.assertEqual(response_chirp['title'], chirp.title)
#
#     def test_create_chirp(self):
#
#         url = reverse('api_chirp_list_create')
#         data = {'title':'Test Chrip 1', 'message':'Test Chirp 1'}
#         self.client.force_authenticate(user=self.user)
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Chirp.objects.count(), 1)
#         self.assertEqual(self.user.id, response.data['author'])
#
#     def test_list_chirp_username_filter(self):
#         chirp = Chirp.objects.create(title='Chirp Title',
#                                      message='Chirp Message', author=self.user)
#         user2 = User.objects.create_user('test2', email='test2@test.com',
#                                              password='password')
#         chirp2 = Chirp.objects.create(title='Chirp Title2',
#                                      message='Chirp Message2', author=user2)
#
#         url = reverse('api_chirp_list_create')
#
#         response = self.client.get(url, {'username': user2.username},
#                                    format='json')
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['count'], 1)
#         chirp_response = response.data['results'][0]
#         self.assertEqual(chirp_response['author'], user2.id)