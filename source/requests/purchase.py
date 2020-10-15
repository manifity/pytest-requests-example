import requests

"""
Полный запрос к API - /service/v1/purchase/{request}

endpoint_name - отдельная переменная для поддержки Page Object. 
В случае, если эндпоинт будет переименован по какой-либо причине,
рефакторинг будет минимальным.
"""

endpoint_name = '/purchase'


def get_purchase_info(select_api_version, client_id, items):
    url = f'{select_api_version}/{endpoint_name}/by-client'    # /service/v_/purchase/by-client
    request_body = {
      'client_id': str(client_id),        # client_id is argument from test
      'item_ids': [
        f'{items}'                        # item_ids are arguments from test
      ]
    }
    request = requests.post(url, json=request_body)

    if request.status_code is 200:
        """
        Response:
        {
          'items': [
            {
              'item_id': 'string',
              'purchased': 'true/false',
              'last_order_number': 'string',
              'last_purchase_date': '2020-01-16T13:33:00.000Z',
              'purchase_count': 'string'
            }
          ]
        }
        """
        return request.json()
    else:
        raise TypeError('Server\'s response is not 200')
