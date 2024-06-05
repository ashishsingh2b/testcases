from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

class StdTest(APITestCase):

    def std_test(self):
        _data ={
            'id': 1,
            'name': 'Ashish',
            'roll': 12,
            'city': 'Surat'
        }

        _response =self.client.post('lcstu/', data=_data, format="json")
        _data= _response.json()
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)