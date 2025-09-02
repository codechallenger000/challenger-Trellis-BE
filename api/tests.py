from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .utils import number_to_english

class NumberConversionTests(TestCase):
    def test_single_digit(self):
        self.assertEqual(number_to_english(5), "five")

    def test_double_digit(self):
        self.assertEqual(number_to_english(42), "forty two")

    def test_three_digit(self):
        self.assertEqual(number_to_english(123), "one hundred twenty three")

    def test_thousand(self):
        self.assertEqual(number_to_english(1000), "one thousand")

    def test_large_number(self):
        self.assertEqual(number_to_english(12345678), "twelve million three hundred forty five thousand six hundred seventy eight")

    def test_zero(self):
        self.assertEqual(number_to_english(0), "zero")

class NumberToEnglishAPITestCase(APITestCase):
    def test_get_valid_number(self):
        response = self.client.get('/num_to_english/', {'number': 123})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['num_in_english'], "one hundred twenty three")

    def test_get_invalid_number(self):
        response = self.client.get('/num_to_english/', {'number': 'abc'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], "error")

    def test_post_valid_number(self):
        response = self.client.post('/num_to_english/', {'number': 9999}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['num_in_english'], "nine thousand nine hundred ninety nine")

    def test_post_invalid_number(self):
        response = self.client.post('/num_to_english/', {'number': 'xyz'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], "error")

    def test_post_missing_number(self):
        response = self.client.post('/num_to_english/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], "error")
