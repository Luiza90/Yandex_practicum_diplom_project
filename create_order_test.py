# Луиза Махмудова, 7-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request
def get_track_number_of_order():
    track_number = sender_stand_request.post_new_order()
    return track_number.json()["track"]


def test_create_track_order():
    track_number = get_track_number_of_order()
    response = sender_stand_request.get_order_number(track_number)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200
