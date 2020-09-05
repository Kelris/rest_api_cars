from django.urls import path, include
from rest_framework import status
from rest_framework.exceptions import NotFound, APIException
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework.utils import json

from rest_cars.models import Car, Vote


class URLNamesTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('rest_cars.urls'))
    ]

    def test_url_names(self):
        url_list = ['api_view', 'cars', 'rate', 'popular']
        for urls in url_list:
            url = reverse(urls)
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class RestApiTests(APITestCase):
    def test_url_addresses(self):
        url_addresses = [
            'http://testserver/api/',
            'http://testserver/api/cars/',
            'http://testserver/api/rate/',
            'http://testserver/api/popular/',
        ]

        for url in url_addresses:
            response = self.client.get(url)
            assert response.status_code == 200

    def test_api_(self):
        response = self.client.get('http://testserver/api/')
        self.assertEqual(len(response.data), 6)

    def test_cars(self):
        self.client.post('http://testserver/api/cars/', {
            "make_name": "mazda",
            "model_name": "mazda6"
        }, format='json')

        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(Car.objects.get().make_name, 'mazda')
        self.assertEqual(Car.objects.get().model_name, 'mazda6')

        get_response = self.client.get('http://testserver/api/cars/')
        self.assertEqual(len(get_response.data), 1)

    def test_cars_wrong_data(self):
        self.client.post('http://testserver/api/cars/', {
            "make_name": "xxxxxxx",
            "model_name": "mazda6"
        }, format='json')

        self.assertRaises(NotFound)

        self.client.post('http://testserver/api/cars/', {
            "make_name": "mazda",
            "model_name": "xxxxxxx"
        }, format='json')

        self.assertRaises(NotFound)

        self.client.post('http://testserver/api/cars/', {
            "make_name": "mazda",
            "model_name": "mazda6"
        }, format='json')

        self.client.post('http://testserver/api/cars/', {
            "make_name": "mazda",
            "model_name": "mazda6"
        }, format='json')

        self.assertRaises(APIException)

    def test_rate(self):
        self.client.post('http://testserver/api/cars/', {
            "make_name": "mazda",
            "model_name": "mazda6"
        }, format='json')

        car_id = Car.objects.get().id

        self.client.post('http://testserver/api/rate/', {
            "car": car_id,
            "rate": 2
        }, format='json')

        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(Vote.objects.get().car_id, car_id)
        self.assertEqual(Vote.objects.get().rate, 2)

        get_response = self.client.get('http://testserver/api/rate/')
        self.assertEqual(len(get_response.data), 1)

    def test_popular(self):
        self.client.post('http://testserver/api/cars/', {
            "make_name": "Lamborghini",
            "model_name": "Huracan"
        }, format='json')

        self.client.post('http://testserver/api/cars/', {
            "make_name": "porsche",
            "model_name": "Boxster"
        }, format='json')

        self.client.post('http://testserver/api/cars/', {
            "make_name": "ferrari",
            "model_name": "F12 Berlinetta"
        }, format='json')

        self.client.post('http://testserver/api/cars/', {
            "make_name": "nissan",
            "model_name": "cube"
        }, format='json')

        id_lamborghini = Car.objects.get(make_name="Lamborghini").id
        id_porsche = Car.objects.get(make_name="porsche").id
        id_ferrari = Car.objects.get(make_name="ferrari").id

        self.client.post('http://testserver/api/rate/', {
            "car": id_lamborghini,
            "rate": 5
        }, format='json')

        self.client.post('http://testserver/api/rate/', {
            "car": id_lamborghini,
            "rate": 5
        }, format='json')

        self.client.post('http://testserver/api/rate/', {
            "car": id_lamborghini,
            "rate": 5
        }, format='json')

        self.client.post('http://testserver/api/rate/', {
            "car": id_porsche,
            "rate": 4
        }, format='json')

        self.client.post('http://testserver/api/rate/', {
            "car": id_porsche,
            "rate": 4
        }, format='json')

        self.client.post('http://testserver/api/rate/', {
            "car": id_ferrari,
            "rate": 3
        }, format='json')

        response = self.client.get('http://testserver/api/popular/')

        self.assertEqual(len(json.loads(response.content)), 3)

        self.assertIn('Lamborghini', json.loads(response.content)[0]['make_name'])
        self.assertIn('porsche', json.loads(response.content)[1]['make_name'])
        self.assertIn('ferrari', json.loads(response.content)[2]['make_name'])

        self.assertNotIn('nissan', json.loads(response.content)[0]['make_name'])
        self.assertNotIn('nissan', json.loads(response.content)[1]['make_name'])
        self.assertNotIn('nissan', json.loads(response.content)[2]['make_name'])
