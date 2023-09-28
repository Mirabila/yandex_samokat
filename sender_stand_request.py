import configuration
import requests
import data

#Создаем нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK + track,  # подставляем полный url
                         headers=data.headers)  # а здесь заголовки

