Этот проект содержит набор тестов для проверки работы API PetFriends. Тесты охватывают функциональность, связанную с авторизацией, управлением питомцами, а также обработкой ошибок.

Тесты проверяют основные возможности API: добавление, получение, обновление и удаление питомцев, а также обработку некорректных данных. Используется pytest.

#### Описание тестов
#### Авторизация
- test_positive_get_api_key: Проверяет получение API-ключа с корректными данными.
- test_negative_invalid_login_for_api_key: Проверяет, что некорректный логин возвращает ошибку.
- test_negative_invalid_password_for_api_key: Проверяет, что неправильный пароль возвращает ошибку.
#### Управление питомцами
- test_positive_add_new_pet: Добавляет питомца без фото.
- test_positive_get_pets: Получает список питомцев.
- test_positive_add_new_pet_with_photo: Добавляет питомца с фото.
- test_positive_add_pet_photo: Добавляет фото для питомца.
- test_positive_delete_pet: Удаляет питомца.
- test_delete_all_pets: Удаляет всех питомцев, в том числе питомцев, созданных другими пользователями.
#### Негативные тесты
- test_negative_add_new_pet_without_name: Проверяет добавление питомца без имени.
- test_negative_add_new_pet_without_animal_type: Проверяет добавление питомца без типа.
- test_negative_add_new_pet_without_age: Проверяет добавление питомца без возраста.
- test_add_new_pet_with_negative_age: Проверяет добавление питомца с отрицательным возрастом.
- test_add_new_pet_with_large_name: Проверяет добавление питомца с длинным именем.
- test_negative_add_new_pet_with_huge_age: Проверяет добавление питомца с некорректно большим возрастом.
- test_add_new_pet_with_invalid_photo: Проверяет добавление питомца с фото в некорректном формате.
- test_negative_delete_non_existent_pet: Проверяет удаление несуществующего питомца.