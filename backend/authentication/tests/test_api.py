from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserAPI(APITestCase):
    def setUp(self):
        self.endpoint = reverse("auth:user-create")
        self.payload = {
            "cpf": "88999520063",
            "email": "davi.oliveira@fakemail.com",
            "password": "D@viP4sswd",
            "preferred_name": "Davi",
            "full_name": "Davi Martins Oliveira",
            "phone_number": "88999520063",
        }

    def test_create_user_return_201(self):
        response = self.client.post(self.endpoint, self.payload, format="json")
        expected_response = {
            "cpf": "88999520063",
            "email": "davi.oliveira@fakemail.com",
            "preferred_name": "Davi",
            "full_name": "Davi Martins Oliveira",
            "phone_number": "+5588999520063",
        }
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), expected_response)

    def test_create_user_invalid_cpf_return_400(self):
        self.payload["cpf"] = "00000000000"
        response = self.client.post(self.endpoint, self.payload, format="json")
        expected_response = {"cpf": ["Enter a valid CPF number."]}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), expected_response)
        
        self.payload["cpf"] = "88999520012"
        response = self.client.post(self.endpoint, self.payload, format="json")
        expected_response = {"cpf": ["Enter a valid CPF number."]}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), expected_response)

    def test_create_user_invalid_phone_return_400(self):
        self.payload["phone_number"] = "00000"
        response = self.client.post(self.endpoint, self.payload, format="json")
        expected_response = {"phone_number": ["Enter a valid phone number."]}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), expected_response)

    def test_create_user_invalid_email_return_400(self):
        self.payload["email"] = "daviwrongmail.com"
        response = self.client.post(self.endpoint, self.payload, format="json")
        expected_response = {"email": ["Enter a valid email address."]}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), expected_response)

