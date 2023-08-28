from rest_framework.test import APITestCase
import pytest

from .models import ParcelType
from .tasks import calculate_delivery_cost

class ParcelTestCase(APITestCase):

    def setUp(self):
        parcel_types = {}
        for parcel_type in ('EL', 'CL', 'OT'):
            parcel_types[parcel_type] = ParcelType.objects.create(type=parcel_type)
        self.parcel_types = parcel_types

    def test_parcels(self):
        resp = self.client.get('/parcels/')
        self.assertEqual(resp.status_code, 200)

        # create parcel
        parcel_data = {'name': 'test', 'value': '100.5', 'weight': '10.6', 'type': self.parcel_types['EL'].id, 'delivery_cost': 100}
        resp = self.client.post('/parcels/', data=parcel_data)
        parcel_id = resp.data['id']
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.data['id'])

        # get parcel types
        resp = self.client.get('/parcel_types/')
        self.assertEqual(resp.status_code, 200)

        # get parcel by id
        resp = self.client.get(f'/parcels/{parcel_id}/')
        self.assertEqual(resp.data['delivery_cost'], 'Не рассчитано')

        # delivery cost calculated
        calculate_delivery_cost()
        resp = self.client.get(f'/parcels/{parcel_id}/')
        self.assertNotEqual(resp.data['delivery_cost'], 'Не рассчитано')
        self.assertIsInstance(float(resp.data['delivery_cost']), float)
