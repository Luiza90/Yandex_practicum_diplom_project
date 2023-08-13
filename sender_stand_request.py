import requests
import configuration
import data

# Запрос на создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
           json=data.order_body)

# Запрос на получение заказа по номеру
def get_order_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER,
           params={"t": track_number})