from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Machine, ProductionLog
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class OEEAPITestCase(APITestCase):
    def setUp(self):
        # Create machine
        self.machine = Machine.objects.create(
            name='Machine 1',
            available_time=420,
            unplanned_downtime=30,
            ideal_cycle_time=60,
            available_operating_time=390,
        )

        # Create production logs
        self.log1 = ProductionLog.objects.create(
            machine=self.machine,
            cycle_id=1,
            log_date='2023-08-01T08:30:00Z',
            units_produced=100,
        )
        self.log2 = ProductionLog.objects.create(
            machine=self.machine,
            cycle_id=2,
            log_date='2023-08-01T09:30:00Z',
            units_produced=50,
        )

    def test_oee_calculation_with_filters(self):
        url = reverse('oee-calculation')
        params = {
            'camera_name': 'Machine 1',
            'oee_threshold': 50,
            'start_date': '2023-08-01T08:00:00Z',
            'end_date': '2023-08-01T10:00:00Z',
        }
        
        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        # Check the structure of the response
        self.assertEqual(len(data), 1)
        self.assertIn('machine_name', data[0])
        self.assertIn('log_date', data[0])
        self.assertIn('availability', data[0])
        self.assertIn('performance', data[0])
        self.assertIn('oee', data[0])

        # Check the values in the response
        self.assertEqual(data[0]['machine_name'], 'Machine 1')
        # Add more assertions for other fields

    def test_invalid_oee_calculation_parameters(self):
        url = reverse('oee-calculation')
        params = {
            # Missing required parameters
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authentication_required(self):
        url = reverse('oee-calculation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_successful_authentication(self):
        # Create a user and obtain a token
        user = User.objects.create_user(username='testuser', password='testpass')
        token = Token.objects.create(user=user)

        # Add the token to the HTTP headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        # Now make a request to a protected endpoint
        url = reverse('oee-calculation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions for the response data

    # Add more test cases as needed
