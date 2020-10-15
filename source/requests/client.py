import requests
from faker import Faker
from source.credo import generate_phone

"""
Полный запрос к API - /service/v1/client/{request}

endpoint_name - отдельная переменная для поддержки Page Object. 
В случае, если эндпоинт будет переименован по какой-либо причине,
рефакторинг будет минимальным.
"""

endpoint_name = '/client'
fake = Faker()


def create_new_client(select_api_version):
    url = f'{select_api_version}/{endpoint_name}/create'    # /service/v_/client/create
    request_body = {
        'name': f'{fake.first_name()}',     # random generated first name (localization can be changed)
        'surname': f'{fake.last_name()}',   # random generated last name (localization can be changed)
        'phone': f'{generate_phone}'        # random generated phone
    }
    request = requests.post(url, json=request_body)

    if request.status_code is 200:
        """
        Response:
        {
        'client_id': int
        }
        """
        return request.json().get('client_id')
    else:
        raise TypeError('Server\'s response is not 200')
