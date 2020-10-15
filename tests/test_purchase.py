import pytest
import time
from source.requests.client import create_new_client
from source.requests.order import create_new_order
from source.requests.purchase import get_purchase_info

# Позволил себе создать возможные id, которые могут существовать
ITEM_IDS = ['1', '2', '3', '4']


@pytest.mark.parametrize('item_id', ITEM_IDS)
def test_success_purchase_by_client(api_version, item_id):
    """

    :param api_version: версия API для тестирования - 'v1' или 'v2git add .'
    :param item_id: id приобретаемого продукта - '1', '2', '3' или '4'

    Asserts:
    'item_id' - сверка, что приобретённый item_id соответствует значению у пользователя
    'purchased' - подтверждение, что продукт был приобретён
    'last_order_number' - проверка, что оформленный заказ совпадает с записанным у пользователя
    'last_purchase_date' - сверяем только дату оформления
    'purchase_count' - для нового пользователя всегда будет '1', так как продукт оформляется впервые

    """
    client = create_new_client(select_api_version=api_version)
    order_json = create_new_order(select_api_version=api_version, client_id=client, item_id=item_id)
    purchase_json = get_purchase_info(select_api_version=api_version, client_id=client, items=item_id)

    assert purchase_json['items'][0]['item_id'] == item_id
    assert purchase_json['items'][0]['purchased'] is True
    assert purchase_json['items'][0]['last_order_number'] == order_json.get('order_number')
    assert time.strftime('%Y-%m-%d') in purchase_json['items'][0]['last_purchase_date']
    assert purchase_json['items'][0]['purchase_count'] == '1'
