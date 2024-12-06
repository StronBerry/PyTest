import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data.data import valid_login, valid_password
from utils.helpers import log_to_txt, save_screenshot, get_http_status
from utils.fixtures import selenium


def test_my_pets_page(selenium):
    """Тест для проверки страницы 'Мои питомцы'."""
    selenium.implicitly_wait(10)  # Настройка неявного ожидания для веб-драйвера
    log_file = None  # Общий файл для лога
    step_number = 1  # Номер текущего шага

    # Шаг 1: Открыть сайт и выполнить авторизацию до страницы "Мои питомцы"
    try:
        selenium.get("https://petfriends.skillfactory.ru/")
        WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success' and @onclick=\"document.location='/new_user';\"]"))
        ).click()
        WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "У меня уже есть аккаунт"))
        ).click()

        selenium.find_element(By.ID, "email").send_keys(valid_login)
        selenium.find_element(By.ID, "pass").send_keys(valid_password)
        selenium.find_element(By.XPATH, "//button[@class='btn btn-success' and @type='submit']").click()
        WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Мои питомцы"))
        ).click()

        assert selenium.current_url == "https://petfriends.skillfactory.ru/my_pets", "URL страницы 'Мои питомцы' неверен"
        http_status = get_http_status(selenium.current_url)
        log_file = log_to_txt(log_file, step_number, "PASS", f"страница {selenium.current_url} открыта (проверка код {http_status})")
    except Exception as e:
        save_screenshot(selenium)
        log_to_txt(log_file, step_number, "FAIL", f"Ошибка открытия страницы: {e}")
        pytest.fail(f"Ошибка в шаге {step_number}: {e}")
    step_number += 1

    # Шаг 2: Проверить количество питомцев
    try:
        pet_info_block = WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'col-sm-4') and contains(@class, 'left')]"))
        ).text
        pet_count_text = [line for line in pet_info_block.split('\n') if "Питомцев:" in line][0]
        expected_pet_count = int(pet_count_text.split(":")[1].strip())

        log_to_txt(log_file, step_number, "PASS", f'найден элемент "{pet_count_text}"')
    except Exception as e:
        save_screenshot(selenium)
        log_to_txt(log_file, step_number, "FAIL", f"Ошибка получения информации о питомцах: {e}")
        pytest.fail(f"Ошибка в шаге {step_number}: {e}")
    step_number += 1

    # Шаг 3: Проверить количество карточек
    try:
        pet_cards = selenium.find_elements(By.XPATH, "//tbody/tr")
        actual_pet_count = len(pet_cards)
        assert expected_pet_count == actual_pet_count, (
            f"Ожидаемое количество питомцев ({expected_pet_count}) не совпадает с отображаемым ({actual_pet_count})"
        )

        log_to_txt(log_file, step_number, "PASS", f"количество карточек питомцев пользователей равно отображаемому числу")
    except Exception as e:
        save_screenshot(selenium)
        log_to_txt(log_file, step_number, "FAIL", f"Ошибка проверки количества карточек: {e}")
        pytest.fail(f"Ошибка в шаге {step_number}: {e}")
    step_number += 1

    # Шаг 4: Логирование подробной информации о карточках
    try:
        missing_name, missing_breed, missing_age, missing_photo = 0, 0, 0, 0

        for card in pet_cards:
            photo = card.find_element(By.TAG_NAME, "th").find_element(By.TAG_NAME, "img").get_attribute("src")
            name = card.find_element(By.XPATH, "./td[1]").text.strip()
            breed = card.find_element(By.XPATH, "./td[2]").text.strip()
            age = card.find_element(By.XPATH, "./td[3]").text.strip()

            if not name:
                missing_name += 1
            if not breed:
                missing_breed += 1
            if not age:
                missing_age += 1
            if not photo:
                missing_photo += 1

        log_to_txt(log_file, step_number, "INFO", f"Общее количество карточек: {actual_pet_count}")
        log_to_txt(log_file, step_number, "INFO", f"Карточек без имени: {missing_name}")
        log_to_txt(log_file, step_number, "INFO", f"Карточек без породы: {missing_breed}")
        log_to_txt(log_file, step_number, "INFO", f"Карточек без возраста: {missing_age}")
        log_to_txt(log_file, step_number, "INFO", f"Карточек без фото: {missing_photo}")
    except Exception as e:
        save_screenshot(selenium)
        log_to_txt(log_file, step_number, "FAIL", f"Ошибка логирования информации о карточках: {e}")
        pytest.fail(f"Ошибка в шаге {step_number}: {e}")
