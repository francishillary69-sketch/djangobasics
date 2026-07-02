from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from storeapp.models import Employee


class EmployeeFormTests(TestCase):
    def test_home_page_form_creates_employee_record(self):
        response = self.client.post(
            reverse('home'),
            {
                'name': 'Jane Doe',
                'email': 'jane@example.com',
                'phone': '0712345678',
                'gender': 'Female',
                'department': 'IT',
                'title': 'Developer',
                'salary': '75000',
                'hire_date': '2024-01-15',
                'address': 'Nairobi',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.count(), 1)

        employee = Employee.objects.get()
        self.assertEqual(employee.name, 'Jane Doe')
        self.assertEqual(employee.email, 'jane@example.com')
        self.assertEqual(employee.phone_number, '0712345678')
        self.assertEqual(employee.gender, 'Female')
        self.assertEqual(employee.department, 'IT')
        self.assertEqual(employee.job_title, 'Developer')
        self.assertEqual(employee.salary, Decimal('75000'))
        self.assertEqual(employee.hire_date, date(2024, 1, 15))
        self.assertEqual(employee.address, 'Nairobi')
