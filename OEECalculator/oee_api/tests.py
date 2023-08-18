from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Machine, ProductionLog
from rest_framework import status
from django.urls import reverse


class OEEAPITestCase(TestCase):
    def setUp(self):
        # Create machine
        self.machine = Machine.objects.create(
            name='Machine 1',
            available_time=420,  # 7 hours
            unplanned_downtime=30,  # 30 minutes
            ideal_cycle_time=60,  # 1 minute
            available_operating_time=390,  # 6.5 hours
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

        response = self.client.get(url, {
        'camera_name': 'Machine 1',
        'oee_threshold': 50,
        'start_date': '2023-08-01T08:00:00Z',
        'end_date': '2023-08-01T10:00:00Z',
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

            # Print the data to help troubleshoot
        print(data)

    
        # Update the assertion based on the actual data you expect
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['machine_name'], 'Machine 1')
        self.assertEqual(data[1]['machine_name'], 'Machine 1')


