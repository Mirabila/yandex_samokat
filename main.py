import configuration
import data
import sender_stand_request


#Меняем имя для проверки в поле name параметра kit_body
def get_track(user_body):
    response = sender_stand_request.post_new_order(user_body)
    track = response.json().get("track")
    return track

#Проверка, что введенные данные возвращают код ответа — 201 и поле name в ответе совпадает с полем name в запросе
def test_track():
    track = get_track(data.user_body)
    response = sender_stand_request.get_order(str(track))
    assert response.status_code == 200

