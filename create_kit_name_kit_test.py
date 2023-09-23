import sender_stand_request
import data

def post_new_user():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json ()['authToken']

data.headers_kits["Authorization"] = f"Bearer {post_new_user()}"

def kkit_body(live):
    response2 = data.kit_body.copy()
    response2["name"] = live
    return response2

def positive_assert(live):
    kit_body = kkit_body(live)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == live

def negative_assert(live):
    kit_body = kkit_body(live)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

# Тест 1. Допустимое количество символов (1):
# kit_body = {
# "name": "a"
# }
def test_create_kit_name_kit_success():
    positive_assert("a")

# Тест 2. 	Допустимое количество символов (511):
# kit_body = {
# "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
# }
def test_create_kit_name_kit_success():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0):
# kit_body = {
# "name": ""
# }
def test_create_kit_name_kit_error():
    negative_assert("")

# Тест 4. Количество символов больше допустимого (512):
# kit_body = {
# "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
# }
def test_create_kit_name_kit_error():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы:
# kit_body = {
# "name": "QWErty"
# }
def test_create_kit_name_kit_success():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы:
# kit_body = {
# "name": "Мария"
# }
def test_create_kit_name_kit_success():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы:
# kit_body = {
# "name": ""№%@","
# }
def test_create_kit_name_kit_success():
    positive_assert("№%@",)

# Тест 8. Разрешены пробелы:
# kit_body = {
# "name": " Человек и КО "
# }
def test_create_kit_name_kit_success():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры:
# kit_body = {
# "name": "123"
# }
def test_create_kit_name_kit_success():
    positive_assert("123")

# Тест 10. Параметр не передан в запросе:
# kit_body = {
# }
def test_create_kit_name_kit_error():
    negative_assert("")

# Тест 11. Передан другой тип параметра (число):
# kit_body = {
# "name": 123
# }
def test_create_kit_name_kit_error():
    negative_assert(123)