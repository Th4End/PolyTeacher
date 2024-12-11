from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Translation

class TranslationAPITestCase(APITestCase):
    def test_get_translations(self):
        response = self.client.get('/api/translations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_translation(self):
        data = {
            "source_text": "Bonjour",
            "source_language": "fr",
            "target_language": "en"
        }
        response = self.client.post('/api/translations/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('translated_text', response.data)
