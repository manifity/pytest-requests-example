import requests
from random import randint
from faker import Faker
from source.credo import generate_phone

"""
Полный запрос к API - /service/v1/order/{request}

endpoint_name - отдельная переменная для поддержки Page Object. 
В случае, если эндпоинт будет переименован по какой-либо причине,
рефакторинг будет минимальным.
"""

endpoint_name = '/order'
fake = Faker()


def create_new_order(select_api_version, client_id, item_id):
    url = f'{select_api_version}/{endpoint_name}/create'    # /service/v_/order/create
    request_body = {
      'client_id': f'{client_id}',      # client_id is method's argument, get it the tests
      'address': f'{fake.address()}',   # random generated address (localization can be changed)
      'phone': f'{generate_phone()}',   # random generated phone
      'items': [
        {
          'item_id': item_id,                    # product item_id for user
          'price': float(randint(100, 500)),     # random generated float number
          'quantity': randint(1, 10),            # random generated float number
        }
      ]
    }
    request = requests.post(url, json=request_body)

    if request.status_code is 200:
        """
        Response:
        {
        'order_id': int,
        'order_number': string
        } 
        """
        return request.json()
    else:
        raise TypeError('Server\'s response is not 200')
