from cashback.api import call_api_maisTodos
from rest_framework.test import APITestCase


class APIMaisTodosTestCase(APITestCase):
    
    def test_call_external_api(self):
        """test that checks communication with the external API"""
        data = {
            "document":"19738091098",
            "cashback": 20.50
        }
        response = call_api_maisTodos(**data)
        self.assertEqual(response['document'], data['document'])
        self.assertEqual(response['cashback_mt'], str(data['cashback']))