import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data.data import valid_login, valid_password
from utils.helpers import log_step, get_http_status, save_screenshot
import time
from utils.fixtures import selenium, log  # Импорт фикстур selenium и log


def test_petfriends(selenium, log):
    selenium.implicitly_wait(10)  # Установка implicitly wait для всего теста
    test_start_time = time.time()

    # Шаг 1: Открыть сайт
    step_start_time = time.time()
    try:
        selenium.get("https://petfriends.skillfactory.ru/")
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 1", "PASS", "Открыт сайт petfriends.skillfactory.ru", step_start_time, http_status)
    except Exception as e:
        log_step(log, "Step 1", "FAIL", f"Ошибка: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 1: {e}")

    # Шаг 2: Клик по кнопке "Зарегистрироваться"
    step_start_time = time.time()
    try:
        btn_register = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success' and @onclick=\"document.location='/new_user';\"]"))
        )
        btn_register.click()
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 2", "PASS", "Клик по кнопке 'Зарегистрироваться'", step_start_time, http_status)
    except Exception as e:
        log_step(log, "Step 2", "FAIL", f"Ошибка: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 2: {e}")

    # Шаг 3: Проверка перехода на страницу регистрации
    step_start_time = time.time()
    try:
        assert selenium.current_url == "https://petfriends.skillfactory.ru/new_user"
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 3", "PASS", "Открыта страница регистрации", step_start_time, http_status)
    except Exception as e:
        log_step(log, "Step 3", "FAIL", f"Ошибка проверки: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 3: {e}")

    # Шаг 4: Клик по ссылке "У меня уже есть аккаунт"
    step_start_time = time.time()
    try:
        WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "У меня уже есть аккаунт"))
        ).click()
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 4", "PASS", "Клик по ссылке 'У меня уже есть аккаунт'", step_start_time, http_status)
    except Exception as e:
        log_step(log, "Step 4", "FAIL", f"Ошибка: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 4: {e}")

    # Шаг 5: Проверка перехода на страницу входа
    step_start_time = time.time()
    try:
        assert selenium.current_url == "https://petfriends.skillfactory.ru/login"
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 5", "PASS", "Открыта страница входа", step_start_time, http_status)
    except Exception as e:
        log_step(log, "Step 5", "FAIL", f"Ошибка проверки: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 5: {e}")

    # Шаг 6: Ввод логина
    step_start_time = time.time()
    try:
        login_field = WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        login_field.send_keys(valid_login)
        log_step(log, "Step 6", "PASS", "Введен логин", step_start_time)
    except Exception as e:
        log_step(log, "Step 6", "FAIL", f"Ошибка: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 6: {e}")

    # Шаг 7: Ввод пароля
    step_start_time = time.time()
    try:
        password_field = WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.ID, "pass"))
        )
        password_field.send_keys(valid_password)
        log_step(log, "Step 7", "PASS", "Введен пароль", step_start_time)
    except Exception as e:
        log_step(log, "Step 7", "FAIL", f"Ошибка: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 7: {e}")

    # Шаг 8: Клик по кнопке "Войти"
    step_start_time = time.time()
    try:
        submit_button = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success' and @type='submit']"))
        )
        submit_button.click()
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 8", "PASS", "Клик по кнопке 'Войти'", step_start_time, http_status)
    except Exception as e:
        log_step(log, "Step 8", "FAIL", f"Ошибка: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 8: {e}")

    # Шаг 9: Проверка перехода на страницу всех питомцев
    step_start_time = time.time()
    try:
        assert selenium.current_url == "https://petfriends.skillfactory.ru/all_pets"
        log_step(log, "Step 9", "PASS", "Открыта страница 'Все питомцы'", step_start_time)
    except Exception as e:
        log_step(log, "Step 9", "FAIL", f"Ошибка проверки: {e}", step_start_time)
        save_screenshot(selenium)
        pytest.fail(f"Ошибка в шаге 9: {e}")

    # Итог
    total_duration = round(time.time() - test_start_time, 3)
    log_step(log, "Test", "PASS", f"Тест завершен успешно, Duration: {total_duration}s", test_start_time)
