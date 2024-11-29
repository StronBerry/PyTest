import pytest
from api import PetFriends
from settings import email, password
import os
from datetime import datetime
import time

LOGS_DIR = os.path.join(os.getcwd(), "Logs")
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

log_filename = datetime.now().strftime("%H-%M-%S-%d.%m.%Y.txt")
log_filepath = os.path.join(LOGS_DIR, log_filename)


def log_message(message: str):
    """Функция для записи логов"""
    with open(log_filepath, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")


import functools

def time_logger(func):
    """Декоратор для логирования времени выполнения теста"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
        finally:
            end_time = time.time()
            duration = end_time - start_time
            log_message(f"                  Время выполнения: {duration:.2f} секунд.")
        return result
    return wrapper


def log_message(message: str):
    """Функция для записи логов"""
    with open(log_filepath, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")


@pytest.fixture
def get_key():
    """Фикстура для получения API-ключа"""
    pf = PetFriends()
    status, result = pf.get_api_key(email, password)
    assert status == 200, "Не удалось получить API-ключ"
    log_message(f"[INFO] Получен API-ключ: {result['key']}")
    return result['key']


@pytest.fixture
def get_pets(get_key):
    """Фикстура для получения списка питомцев"""
    pf = PetFriends()
    status, result = pf.get_pets(get_key)
    assert status == 200, "Не удалось получить список питомцев"
    log_message(f"[INFO] Получен список питомцев: {len(result.get('pets', []))} питомцев найдено")
    return status, result


@pytest.fixture
def create_pet(get_key):
    """Фикстура для создания тестового питомца"""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "Тест", "Тестовая порода", "3")
    assert status == 200, "Не удалось добавить тестового питомца"
    log_message(f"[INFO] Создан тестовый питомец с ID: {result['id']}")
    yield result
    pf.delete_pet(get_key, result["id"])
    log_message(f"[INFO] Удалён тестовый питомец с ID: {result['id']}")


# *** Позитивные тесты ***
@time_logger
def test_positive_get_api_key():
    """Тест на получение API-ключа"""
    pf = PetFriends()
    status, result = pf.get_api_key(email, password)
    try:
        assert status == 200, "Не удалось получить API-ключ"
        assert 'key' in result, "Ответ не содержит ключа 'key'"
        log_message("[PASS] Тест на получение API-ключа прошёл успешно")
    except AssertionError as e:
        log_message(f"[FAIL] Тест на получение API-ключа провалился: {str(e)}")
        raise

@time_logger
def test_positive_add_new_pet(get_key):
    """Тест добавления нового питомца без фото."""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "4")
    try:
        assert status == 200, "Питомец не добавлен"
        assert result["name"] == "Маффин", "Имя добавленного питомца не совпадает"
        log_message("[PASS] Тест добавления питомца без фото прошёл успешно")
    except AssertionError as e:
        log_message(f"[FAIL] Тест добавления питомца без фото провалился: {str(e)}")
        raise

@time_logger
def test_positive_add_new_pet_with_photo(get_key):
    """Тест добавления нового питомца с фото."""
    pf = PetFriends()
    status, result = pf.add_new_pet_with_photo(get_key, "Маффин", "Лабрадор", "4", "images/001.jpg")
    try:
        assert status == 200, "Питомец с фото не добавлен"
        assert result["name"] == "Маффин", "Имя добавленного питомца не совпадает"
        assert "pet_photo" in result, "Фото питомца отсутствует в ответе"
        log_message("[PASS] Тест добавления питомца с фото прошёл успешно")
    except AssertionError as e:
        log_message(f"[FAIL] Тест добавления питомца с фото провалился: {str(e)}")
        raise

@time_logger
def test_positive_get_pets(get_key):
    """Тест на получение списка питомцев"""
    pf = PetFriends()
    status, result = pf.get_pets(get_key)
    try:
        assert status == 200, "Не удалось получить список питомцев"
        assert len(result['pets']) > 0, "Список питомцев пуст"
        assert isinstance(result, dict), "Результат не является словарём"
        log_message("[PASS] Тест на получение списка питомцев прошёл успешно")
    except AssertionError as e:
        log_message(f"[FAIL] Тест на получение списка питомцев провалился: {str(e)}")
        raise

@time_logger
def test_positive_add_pet_photo(get_key, create_pet):
    """Тест на добавление фото питомца"""
    pf = PetFriends()
    pet_id = create_pet["id"]
    status, result = pf.add_pet_photo(get_key, pet_id, "images/001.jpg")
    try:
        assert status == 200, f"Не удалось добавить фото для питомца с ID {pet_id}"
        assert "pet_photo" in result, "Фото питомца отсутствует в ответе"
        log_message(f"[PASS] Тест на добавление фото питомца с ID {pet_id} прошёл успешно")
    except AssertionError as e:
        log_message(f"[FAIL] Тест на добавление фото питомца с ID {pet_id} провалился: {str(e)}")
        raise

@time_logger
def test_positive_delete_pet(get_key, get_pets):
    """Тест на удаление питомца"""
    pf = PetFriends()
    status, pets = get_pets
    if pets['pets']:
        pet_id = pets['pets'][0]['id']
        status, _ = pf.delete_pet(get_key, pet_id)
        try:
            assert status == 200, f"Питомец с ID {pet_id} не был удалён"
            log_message(f"[PASS] Тест на удаление питомца с ID {pet_id} прошёл успешно")
        except AssertionError as e:
            log_message(f"[FAIL] Тест на удаление питомца провалился: {str(e)}")
            raise
    else:
        pytest.fail("Нет доступных питомцев для удаления")


# *** Негативные тесты с обработкой кода 200 ***
@time_logger
def test_negative_invalid_login_for_api_key():
    """Тест на получение API-ключа с неправильным логином"""
    pf = PetFriends()
    invalid_login = "wrong_user"
    invalid_password = "wrong_password"
    status, _ = pf.get_api_key(invalid_login, invalid_password)
    try:
        assert status == 403, f"API вернул статус {status}, ожидался 403"
        log_message("[PASS] Тест на получение API-ключа с неверным логином прошёл успешно")
    except AssertionError:
        if status == 200:
            log_message(f"[FAIL] Тест на получение API-ключа с неверным логином: сервер вернул 200 вместо 403")
        else:
            log_message(f"[FAIL] Тест на получение API-ключа с неверным логином: сервер вернул {status} вместо 403")
        raise

@time_logger
def test_negative_add_new_pet_without_name(get_key):
    """Тест на добавление питомца без имени"""
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, "", "Лабрадор", "4")
    expected_error_message = {'error': 'Все поля (name, animal_type, age) обязательны'}

    if status == 400 and response == expected_error_message:
        log_message("[PASS] Тест на добавление питомца без имени прошёл успешно: сервер корректно вернул сообщение об ошибке")
    elif status == 400:
        log_message(f"[FAIL] Тест на добавление питомца без имени провалился: сервер вернул 200, но ответ не соответствует ожидаемому. Ответ сервера: {response}")
        assert False, "API разрешил добавить питомца без имени с некорректным ответом"
    else:
        log_message(f"[FAIL] Тест на добавление питомца без имени провалился: сервер вернул статус {status} и ответ {response}, ожидался код ошибки")
        assert False, f"Ожидался код ошибки с сообщением: {expected_error_message}, но сервер вернул {status} с ответом: {response}"


@time_logger
def test_negative_delete_non_existent_pet(get_key):
    """Тест на удаление несуществующего питомца"""
    pf = PetFriends()
    non_existent_pet_id = "1234567890"
    status, _ = pf.delete_pet(get_key, non_existent_pet_id)
    try:
        assert status != 200, f"Удаление несуществующего питомца вернуло статус {status}"
        log_message("[PASS] Тест на удаление несуществующего питомца прошёл успешно")
    except AssertionError:
        if status == 200:
            log_message(f"[FAIL] Тест на удаление несуществующего питомца: сервер вернул 200, ожидался код ошибки")
        else:
            log_message(f"[FAIL] Тест на удаление несуществующего питомца: сервер вернул {status}, ожидался код ошибки")
        raise

@time_logger
def test_negative_add_new_pet_without_breed(get_key):
    """Тест на добавление питомца без породы"""
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, "Маффин", "", "4")
    assert status == 400, "Ожидался статус 400, но сервер вернул другой код"
    log_message(f"[PASS] Ответ сервера (без породы): {response}")

@time_logger
def test_negative_add_new_pet_without_age(get_key):
    """Тест на добавление питомца без возраста"""
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "")
    assert status == 400, "Ожидался статус 400, но сервер вернул другой код"
    log_message(f"[PASS] Ответ сервера (без возраста): {response}")


@time_logger
def test_negative_add_new_pet_with_large_name(get_key):
    """Тест на добавление питомца с именем в 256 символов"""
    long_name = "А" * 256
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, long_name, "Лабрадор", "4")

    if status == 400:
        log_message(f"[PASS] Тест на добавление питомца с именем в 256 символов прошёл успешно. Код ответа: {status}")
    elif status == 200:
        log_message(f"[FAIL] Сервер создал объект с именем в 256 символов - ожидалось сообщение об ошибке. Код ответа: {status}")
        assert False, "Сервер разрешил создать питомца с именем в 256 символов"
    else:
        log_message(f"[FAIL] Сервер вернул неожиданный статус: {status}. Код ответа: {status}")
        assert False, f"Ожидался статус 400, но сервер вернул {status}"

@time_logger
def test_negative_add_new_pet_with_negative_age(get_key):
    """Тест на добавление питомца с отрицательным возрастом"""
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "-4")

    if status == 400:
        log_message(f"[PASS] Тест на добавление питомца с отрицательным возрастом прошёл успешно. Код ответа: {status}")
    elif status == 200:
        log_message(f"[FAIL] Сервер создал объект с отрицательным возрастом - ожидалось сообщение об ошибке. Код ответа: {status}")
        assert False, "Сервер разрешил создать питомца с отрицательным возрастом"
    else:
        log_message(f"[FAIL] Сервер вернул неожиданный статус: {status}. Код ответа: {status}")
        assert False, f"Ожидался статус 400, но сервер вернул {status}"


@time_logger
def test_negative_add_new_pet_with_numbers_as_name(get_key):
    """Тест на добавление питомца с числами вместо имени"""
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, "123456", "Лабрадор", "4")

    if status == 400:
        log_message(f"[PASS] Тест на добавление питомца с числами вместо имени прошёл успешно. Код ответа: {status}")
    elif status == 200:
        log_message(f"[FAIL] Сервер создал объект с числами вместо имени - ожидалось сообщение об ошибке. Код ответа: {status}")
        assert False, "Сервер разрешил создать питомца с числами вместо имени"
    else:
        log_message(f"[FAIL] Сервер вернул неожиданный статус: {status}. Код ответа: {status}")
        assert False, f"Ожидался статус 400, но сервер вернул {status}"


@time_logger
def test_negative_add_new_pet_with_numbers_as_breed(get_key):
    """Тест на добавление питомца с числами вместо породы"""
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, "Маффин", "123456", "4")

    if status == 400:
        log_message(f"[PASS] Тест на добавление питомца с числами вместо породы прошёл успешно. Код ответа: {status}")
    elif status == 200:
        log_message(f"[FAIL] Сервер создал объект с числами вместо породы - ожидалось сообщение об ошибке. Код ответа: {status}")
        assert False, "Сервер разрешил создать питомца с числами вместо породы"
    else:
        log_message(f"[FAIL] Сервер вернул неожиданный статус: {status}. Код ответа: {status}")
        assert False, f"Ожидался статус 400, но сервер вернул {status}"


@time_logger
def test_negative_add_new_pet_with_letters_as_age(get_key):
    """Тест на добавление питомца с буквами вместо возраста"""
    pf = PetFriends()
    status, response = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "четыре")

    if status == 400:
        log_message(f"[PASS] Тест на добавление питомца с буквами вместо возраста прошёл успешно. Код ответа: {status}")
    elif status == 200:
        log_message(f"[FAIL] Сервер создал объект с буквами вместо возраста - ожидалось сообщение об ошибке. Код ответа: {status}")
        assert False, "Сервер разрешил создать питомца с буквами вместо возраста"
    else:
        log_message(f"[FAIL] Сервер вернул неожиданный статус: {status}. Код ответа: {status}")
        assert False, f"Ожидался статус 400, но сервер вернул {status}"


# @time_logger
# def test_delete_all_pets(get_key):
#     """Тест на удаление всех уникальных питомцев (в том числе питомцев других пользователей)"""
#     pf = PetFriends()
#
#     # Получаем список питомцев
#     status, pets = pf.get_pets(get_key)
#     assert status == 200, "Не удалось получить список питомцев"
#     log_message(f"[INFO] Статус получения списка питомцев: {status}, количество найденных питомцев: {len(pets.get('pets', []))}")
#
#     if isinstance(pets, dict) and 'pets' in pets:
#         pets = pets['pets']
#     assert len(pets) > 0, "Список питомцев пуст"
#
#     # Сохраняем ID всех питомцев для проверки
#     initial_pet_ids = {pet["id"] for pet in pets}
#
#     # Удаляем всех питомцев
#     for pet in pets:
#         pet_id = pet["id"]
#         pf.delete_pet(get_key, pet_id)
#
#     # Получаем обновлённый список питомцев
#     status, pets_after = pf.get_pets(get_key)
#     assert status == 200, "Не удалось получить обновлённый список питомцев"
#
#     if isinstance(pets_after, dict) and 'pets' in pets_after:
#         pets_after = pets_after['pets']
#
#     remaining_pet_ids = {pet["id"] for pet in pets_after}
#
#     # Проверяем, остались ли удалённые ID
#     deleted_pet_ids = initial_pet_ids.intersection(remaining_pet_ids)
#     if len(deleted_pet_ids) == 0:
#         log_message(f"[FAIL] Все питомцы, включая чужих, были успешно удалены. Это недопустимо.")
#         assert False, "Сервер позволил удалить всех питомцев, включая чужих. Ожидались ограничения."
#     else:
#         log_message(f"[PASS] Не удалось удалить всех питомцев. Тест на ограничения прав прошёл успешно.")
