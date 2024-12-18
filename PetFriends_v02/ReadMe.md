Этот проект содержит набор тестов для проверки работы API PetFriends. Тесты охватывают функциональность, связанную с авторизацией, управлением питомцами, а также обработкой ошибок. В проект добавлено логирование и засекание времени выполнения каждого теста.

Тесты проверяют основные возможности API: добавление, получение, обновление и удаление питомцев, а также обработку некорректных данных. Используется pytest.

#### Особенности
Логирование каждого теста с результатами: [PASS] или [FAIL].
Запись времени выполнения тестов в лог.
Обработка как позитивных, так и негативных сценариев.
Удобная структура для масштабирования тестов.
Логи
Все логи сохраняются в директорию Logs с именами в формате: HH-MM-SS-DD.MM.YYYY.txt.

#### Описание тестов
#### Авторизация
- test_positive_get_api_key: Проверяет получение API-ключа с корректными данными.
- test_negative_invalid_login_for_api_key: Проверяет, что некорректный логин возвращает ошибку.
Управление питомцами
- test_positive_add_new_pet: Добавляет питомца без фото.
- test_positive_add_new_pet_with_photo: Добавляет питомца с фото.
- test_positive_get_pets: Получает список питомцев.
- test_positive_add_pet_photo: Добавляет фото для питомца.
- test_positive_delete_pet: Удаляет питомца.
- test_delete_all_pets: Проверяет, что сервер ограничивает удаление чужих питомцев.
Негативные тесты
- test_negative_add_new_pet_without_name: Проверяет добавление питомца без имени.
- test_negative_add_new_pet_without_breed: Проверяет добавление питомца без породы.
- test_negative_add_new_pet_without_age: Проверяет добавление питомца без возраста.
- test_negative_add_new_pet_with_large_name: Проверяет добавление питомца с длинным именем (256 символов).
- test_negative_add_new_pet_with_negative_age: Проверяет добавление питомца с отрицательным возрастом.
- test_negative_add_new_pet_with_numbers_as_name: Проверяет добавление питомца с числовым именем.
- test_negative_add_new_pet_with_numbers_as_breed: Проверяет добавление питомца с числовой породой.
- test_negative_add_new_pet_with_letters_as_age: Проверяет добавление питомца с буквами вместо возраста.
- test_negative_delete_non_existent_pet: Проверяет удаление несуществующего питомца.
