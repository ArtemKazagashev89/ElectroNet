from .models import Supplier
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class SupplierAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')

        self.supplier = Supplier.objects.create(
            name='Test Supplier',
            email='supplier@example.com',
            country='Testland',
            city='Testcity',
            street='Test Street',
            house_number='1A'
        )

    def test_supplier_list(self):
        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_supplier_create(self):
        response = self.client.post('/api/suppliers/', {
            'name': 'New Supplier',
            'email': 'new_supplier@example.com',
            'country': 'Testland',
            'city': 'Testcity',
            'street': 'New Street',
            'house_number': '3C'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Supplier.objects.count(), 2)

    def test_supplier_update(self):
        response = self.client.put(f'/api/suppliers/{self.supplier.id}/', {
            'name': 'Updated Supplier',
            'email': 'updated_supplier@example.com',
            'country': 'Updatedland',
            'city': 'Updatedcity',
            'street': 'Updated Street',
            'house_number': '2B'
        })
        self.assertEqual(response.status_code, 200)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Updated Supplier')

    def test_supplier_delete(self):
        response = self.client.delete(f'/api/suppliers/{self.supplier.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Supplier.objects.count(), 0)

    def test_supplier_create_invalid(self):
        response = self.client.post('/api/suppliers/', {
            'email': 'invalid_email',
            'country': '',
            'city': '',
            'street': '',
            'house_number': ''
        })
        self.assertEqual(response.status_code, 400)

    def test_supplier_filter_by_country(self):
        Supplier.objects.create(
            name='Supplier A',
            email='supplier_a@example.com',
            country='Country A',
            city='City A',
            street='Street A',
            house_number='1A'
        )
        Supplier.objects.create(
            name='Supplier B',
            email='supplier_b@example.com',
            country='Country B',
            city='City B',
            street='Street B',
            house_number='2B'
        )
        response = self.client.get('/api/suppliers/?search=Country A')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_supplier_integration(self):
        response = self.client.post('/api/suppliers/', {
            'name': 'New Supplier',
            'email': 'new_supplier@example.com',
            'country': 'Integrationland',
            'city': 'Integrationcity',
            'street': 'Integration Street',
            'house_number': '3C'
        })
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Supplier')
