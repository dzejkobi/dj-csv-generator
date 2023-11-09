from django.test import TestCase

from example.models import Address
from example.csv_generators import AddressCsv


class AddressCsvTestCase(TestCase):

    def setUp(self):
        self.address1 = Address(
            company='ACME',
            first_name='Edward',
            last_name='Scissorhands',
            street_address='Far Away 1',
            locality='Somewhere',
            province='DSL',
            postal_code='12-345',
            phone_number='+48 987-654-321'
        )
        self.address1.save()
        self.address2 = Address(
            company='',
            first_name='Bob',
            last_name='Builder',
            street_address='Brick street 12',
            locality='Somewhere else',
            province='MAZ',
            postal_code='54-321',
            phone_number='111222333'
        )
        self.address2.save()

    def test_address_csv(self):
        generator = AddressCsv()
        rows = generator.process_data(Address.objects.all())
        self.assertEqual(len(rows), 2)
        # for row in rows:
        #     print(row)
