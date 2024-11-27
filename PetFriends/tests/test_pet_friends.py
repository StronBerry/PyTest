import pytest
from api import PetFriends
from settings import email, password

@pytest.fixture
def get_key():
    """Фикстура для получения API-ключа"""
    pf = PetFriends()
    status, result = pf.get_api_key(email, password)
    assert status == 200
    return result['key']

@pytest.fixture
def get_pets(get_key):
    """Фикстура для получения списка питомцев"""
    pf = PetFriends()
    status, result = pf.get_pets(get_key)
    return status, result

def test_positive_get_api_key():
    """Тест на получение API-ключа"""
    pf = PetFriends()
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_positive_add_new_pet(get_key):
    """Тест добавления нового питомца без фото."""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "4")
    assert status == 200
    assert result["name"] == "Маффин"

def test_positive_get_pets(get_key):
    """Тест на получение списка питомцев"""
    pf = PetFriends()
    status, result = pf.get_pets(get_key)
    print(result)
    assert status == 200
    assert len(result['pets']) > 0
    assert isinstance(result, dict)

def test_positive_add_pet_photo(get_key, get_pets):
    """Тест на добавление фото питомца"""
    pf = PetFriends()
    status, pets = get_pets
    if pets['pets']:
        pet_id = pets['pets'][0]['id']
        status, result = pf.add_pet_photo(get_key, pet_id, "images/001.jpg")
        assert status == 200
        assert 'pet_photo' in result
    else:
        pytest.fail("Нет доступных питомцев для добавления фото")

def test_positive_add_new_pet_with_photo(get_key):
    """Тест добавления нового питомца с фото."""
    pf = PetFriends()
    status, result = pf.add_new_pet_with_photo(get_key, "Маффин", "Лабрадор", "4", "images/001.jpg")
    assert status == 200
    assert result["name"] == "Маффин"
    assert "pet_photo" in result

def test_positive_update_pet_data(get_key):
    """Тест на обновление данных питомца"""
    pf = PetFriends()

    # Шаг 1: Создание питомца для последующего изменения данных
    initial_data = {
        "name": "Маффин",
        "animal_type": "Лабрадор",
        "age": "4"
    }
    status, result = pf.add_new_pet_simple(get_key, **initial_data)
    assert status == 200
    assert result["name"] == initial_data["name"]
    assert result["animal_type"] == initial_data["animal_type"]
    assert result["age"] == initial_data["age"]

    pet_id = result["id"]
    print(f"Добавлен питомец с ID: {pet_id}")

    # Шаг 2: Изменение данных добавленного питомца
    updated_data = {
        "name": "Бублик",
        "animal_type": "Пудель",
        "age": "3"
    }
    status, updated_result = pf.update_pet(get_key, pet_id, **updated_data)
    assert status == 200
    assert updated_result["id"] == pet_id
    print(f"Питомец с ID: {pet_id} успешно обновлен")

    # Шаг 3: Проверка обновленных питомца
    assert updated_result["name"] == updated_data["name"]
    assert updated_result["animal_type"] == updated_data["animal_type"]
    assert updated_result["age"] == updated_data["age"]
    print("Данные питомца обновлены корректно")


def test_positive_delete_pet(get_key, get_pets):
    """Тест на удаление питомца"""
    pf = PetFriends()
    status, pets = get_pets
    if pets['pets']:
        pet_id = pets['pets'][0]['id']
        status, _ = pf.delete_pet(get_key, pet_id)
        assert status == 200
    else:
        pytest.fail("Нет доступных питомцев для удаления")


def test_negative_invalid_login_for_api_key():
    """Тест на получение API-ключа с неправильным логином"""
    pf = PetFriends()
    invalid_login = "wrong_user"
    invalid_password = "wrong_password"

    status, result = pf.get_api_key(invalid_login, invalid_password)
    if status == 403:
        print(" - 403 - правильный ответ в данном тесте")
    assert status == 403

def test_negative_invalid_password_for_api_key():
    """Тест на получение API-ключа с правильным логином, но неправильным паролем"""
    pf = PetFriends()
    valid_login = "stron@gmail.com" # Правильный логин
    invalid_password = "wrong_password"

    status, result = pf.get_api_key(valid_login, invalid_password)
    if status == 403:
        print(" - 403 - правильный ответ в данном тесте")
    assert status == 403

def test_negative_add_new_pet_without_name(get_key):
    """Тест на добавление питомца без имени"""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "", "Лабрадор", "4")
    if status == 200:
        print(" - Сервер добавил питомца без имени")
    assert status != 200

def test_negative_add_new_pet_without_animal_type(get_key):
    """Тест на добавление питомца без типа"""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "Маффин", "", "4")
    if status == 200:
        print(" - Сервер добавил питомца без типа")
    assert status != 200

def test_negative_add_new_pet_without_age(get_key):
    """Тест на добавление питомца без возраста"""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "")
    if status == 200:
        print(" - Сервер добавил питомца без возраста")
    assert status != 200

def test_negative_add_new_pet_with_negative_age(get_key):
    """Тест на добавление питомца с отрицательным возрастом"""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "-4")
    if status == 200 and result["age"] == "-4":
        print(" - Сервер добавил питомца с возрастом -4")
    assert status != 200
    assert result["age"] == "-4"


def test_negative_add_new_pet_with_large_name(get_key):
    """Тест на добавление питомца со слишком длинным именем"""
    long_name = "А" * 256  # Очень длинное имя
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, long_name, "Лабрадор", "4")
    if status == 200 and result["name"] == long_name:
        print(" - Сервер добавил питомца с именем в 256 символов")
    assert status != 200
    assert result["name"] == long_name


def test_negative_add_new_pet_with_huge_age(get_key):
    """Тест на добавление питомца со слишком большим возрастом"""
    pf = PetFriends()
    status, result = pf.add_new_pet_simple(get_key, "Маффин", "Лабрадор", "1234567890")
    if status == 200 and result["age"] == "long_name":
        print(" - Сервер добавил питомца с именем в 256 символов")
    assert status != 200
    assert result["age"] == "1234567890"

def test_negative_add_new_pet_with_invalid_photo(get_key):
    """Тест на добавление питомца с некорректным форматом фото"""
    pf = PetFriends()
    status, result = pf.add_new_pet_with_photo(get_key, "Маффин", "Лабрадор", "4", "images/invalid_file.txt")
    if status == 200 and result.get("pet_photo") == "":
        print(' - Ответ содержит статус 200, но фото "images/invalid_file.txt" не было добавлено')
    assert status != 200
    assert result.get("pet_photo") == ""

def test_negative_delete_non_existent_pet(get_key):
    """Тест на удаление несуществующего питомца"""
    pf = PetFriends()
    non_existent_pet_id = "1234567890"  # Невалидный ID питомца
    status, result = pf.delete_pet(get_key, non_existent_pet_id)

    assert status != 200

def test_delete_all_pets(get_key):
    """Тест на удаление всех уникальных питомцев (в том числе питомцев других пользователей)"""
    pf = PetFriends()

    status, pets = pf.get_pets(get_key)
    assert status == 200
    if isinstance(pets, dict) and 'pets' in pets:
        pets = pets['pets']
    assert len(pets) > 0

    # Удаляем всех питомцев
    for pet in pets:
        pet_id = pet["id"]
        delete_status = pf.delete_pet(get_key, pet_id)
        delete_status_code, _ = delete_status
        assert delete_status_code == 200