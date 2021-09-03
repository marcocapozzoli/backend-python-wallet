import requests
from cashback.models import APIMaisTodos


def call_api_maisTodos(document, cashback):
    url = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'
    payload_data = {
        "document": document,
        "cashback_mt": cashback
    }
    response = requests.post(url, payload_data)
    
    response_json = response.json()
    response_json.pop('id')
    APIMaisTodos.objects.create(**response_json)
        
    return response.json()