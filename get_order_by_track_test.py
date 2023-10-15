# Леонид Шлангман, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import pytest
import data
import sender_stand_request


# позитивные проверки
def positive_assert_get_order_by_track(track):
    # В переменную get_order_by_track_response сохраняется результат запроса на получение сведений о заказе:
    get_order_by_track_response = sender_stand_request.get_order_by_track(str(track))
    # Проверяется, что код ответа равен 200
    assert get_order_by_track_response.status_code == 200


# Тест 1: успешное получение заказа по его треку (при создании заказа все поля заполнены корректно)
def test_get_order_by_track():
    curr_order_body = data.order_body.copy()
    curr_order_body["firstName"] = "Виктор"
    curr_order_body["lastName"] = "Франкенштейн"
    curr_order_body["address"] = "Женева, ул. Морг"
    curr_order_body["metroStation"] = 4
    curr_order_body["phone"] = "+78003553535"
    curr_order_body["rentTime"] = 6
    curr_order_body["deliveryDate"] = "2023-10-30"
    curr_order_body["comment"] = "оно живое"
    curr_order_body["color"] = [
        "BLACK"
    ]

    order_create_response = sender_stand_request.post_new_order(curr_order_body)
    if order_create_response.status_code == 201:    # вдруг по какой-то причине заказ не создан
        positive_assert_get_order_by_track(order_create_response.json()["track"])
    else:   # тогда дальше проверять не имеет смысла
        pytest.fail("Ошибка создания заказа.")


# Тест 2: успешное получение заказа по его треку (при создании заказа отсутствует "цвет")
def test_get_order_without_color_by_track():
    curr_order_body = data.order_body.copy()
    curr_order_body["firstName"] = "Боб"
    curr_order_body["lastName"] = "Спанч"
    curr_order_body["address"] = "Дно океана"
    curr_order_body["metroStation"] = 4
    curr_order_body["phone"] = "+78003553535"
    curr_order_body["rentTime"] = 4
    curr_order_body["deliveryDate"] = "2023-10-30"
    curr_order_body["comment"] = "бульк"
    curr_order_body.pop("color")

    order_create_response = sender_stand_request.post_new_order(curr_order_body)
    if order_create_response.status_code == 201:
        positive_assert_get_order_by_track(order_create_response.json()["track"])
    else:
        pytest.fail("Ошибка создания заказа.")


# Тест 3: успешное получение заказа по его треку (при создании заказа отсутствует "комментарий")
def test_get_order_without_comment_by_track():
    curr_order_body = data.order_body.copy()
    curr_order_body["firstName"] = "Фокс"
    curr_order_body["lastName"] = "Малдер"
    curr_order_body["address"] = "Вашингтон, округ Колумбия"
    curr_order_body["metroStation"] = 6
    curr_order_body["phone"] = "+78003553535"
    curr_order_body["rentTime"] = 7
    curr_order_body["deliveryDate"] = "2023-10-30"
    curr_order_body.pop("comment")
    curr_order_body["color"] = [
        "BLACK"
    ]

    order_create_response = sender_stand_request.post_new_order(curr_order_body)
    if order_create_response.status_code == 201:
        positive_assert_get_order_by_track(order_create_response.json()["track"])
    else:
        pytest.fail("Ошибка создания заказа.")


# Тест 4: успешное получение заказа по его треку (при создании заказа отсутствуют "цвет" и "комментарий")
def test_get_order_without_unnecessary_by_track():
    curr_order_body = data.order_body.copy()
    curr_order_body["firstName"] = "Чарли"
    curr_order_body["lastName"] = "Кауфман"
    curr_order_body["address"] = "ул. им. Джона Малковича"
    curr_order_body["metroStation"] = 8
    curr_order_body["phone"] = "+78003553535"
    curr_order_body["rentTime"] = 2
    curr_order_body["deliveryDate"] = "2023-10-30"
    curr_order_body.pop("comment")
    curr_order_body.pop("color")

    order_create_response = sender_stand_request.post_new_order(curr_order_body)
    if order_create_response.status_code == 201:
        positive_assert_get_order_by_track(order_create_response.json()["track"])
    else:
        pytest.fail("Ошибка создания заказа.")