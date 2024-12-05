import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import uuid
import os
import csv
from datetime import datetime
from Data.data import valid_login, valid_password
import requests

# Фикстура для браузера
@pytest.fixture(scope="session")
def selenium():
    driver = webdriver.Chrome()
    driver.set_window_size(1400, 1000)
    yield driver
    driver.quit()

# Фикстура для логирования
@pytest.fixture(scope="session")
def log():
    if not os.path.exists('LOG'):
        os.makedirs('LOG')
    log_file = "LOG/" + datetime.now().strftime("%d_%m_%y_%H_%M_%S") + ".csv"
    with open(log_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Step", "Result", "Description", "Duration (s)", "HTTP Status Code"])
    print(f"Log file created: {log_file}")
    return log_file

# Функция логирования шагов
def log_step(log_file, step, result, description, start_time, status_code):
    duration = round(time.time() - start_time, 3)
    print(f"Logging step: {step}, Result: {result}, Duration: {duration}s, HTTP Status Code: {status_code}")
    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([step, result, description, duration, status_code])

# Функция для получения HTTP-кода состояния
def get_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException:
        return None

# Тестовый сценарий
def test_petfriends(selenium, log):
    test_start_time = time.time()

    # Шаг 1: Открыть сайт
    step_start_time = time.time()
    try:
        selenium.get("https://petfriends.skillfactory.ru/")
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 1", "PASS", "Открыт сайт petfriends.skillfactory.ru", step_start_time, http_status)
    except Exception as e:
        http_status = None
        log_step(log, "Step 1", "FAIL", f"Ошибка: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 1: {e}")

    # Шаг 2: Клик по кнопке "Зарегистрироваться"
    step_start_time = time.time()
    try:
        btn_register = selenium.find_element(By.XPATH, "//button[@class='btn btn-success' and @onclick=\"document.location='/new_user';\"]")
        btn_register.click()
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 2", "PASS", "Клик по кнопке 'Зарегистрироваться'", step_start_time, http_status)
    except Exception as e:
        http_status = None
        log_step(log, "Step 2", "FAIL", f"Ошибка: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 2: {e}")

    # Шаг 3: Проверка перехода на страницу регистрации
    step_start_time = time.time()
    try:
        assert selenium.current_url == "https://petfriends.skillfactory.ru/new_user"
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 3", "PASS", "Открыта страница регистрации", step_start_time, http_status)
    except Exception as e:
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 3", "FAIL", f"Ошибка проверки: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 3: {e}")

    # Шаг 4: Клик по ссылке "У меня уже есть аккаунт"
    step_start_time = time.time()
    try:
        btn_exist_acc = selenium.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
        btn_exist_acc.click()
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 4", "PASS", "Клик по ссылке 'У меня уже есть аккаунт'", step_start_time, http_status)
    except Exception as e:
        http_status = None
        log_step(log, "Step 4", "FAIL", f"Ошибка: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 4: {e}")

    # Шаг 5: Проверка перехода на страницу входа
    step_start_time = time.time()
    try:
        assert selenium.current_url == "https://petfriends.skillfactory.ru/login"
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 5", "PASS", "Открыта страница входа", step_start_time, http_status)
    except Exception as e:
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 5", "FAIL", f"Ошибка проверки: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 5: {e}")

    # Шаг 6: Ввод логина
    step_start_time = time.time()
    try:
        field_email = selenium.find_element(By.ID, "email")
        field_email.clear()
        field_email.send_keys(valid_login)
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 6", "PASS", "Введен логин", step_start_time, http_status)
    except Exception as e:
        http_status = None
        log_step(log, "Step 6", "FAIL", f"Ошибка: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 6: {e}")

    # Шаг 7: Ввод пароля
    step_start_time = time.time()
    try:
        field_pass = selenium.find_element(By.ID, "pass")
        field_pass.clear()
        field_pass.send_keys(valid_password)
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 7", "PASS", "Введен пароль", step_start_time, http_status)
    except Exception as e:
        http_status = None
        log_step(log, "Step 7", "FAIL", f"Ошибка: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 7: {e}")

    # Шаг 8: Клик по кнопке "Войти"
    step_start_time = time.time()
    try:
        btn_submit = selenium.find_element(By.XPATH, "//button[@class='btn btn-success' and @type='submit']")
        btn_submit.click()
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 8", "PASS", "Клик по кнопке 'Войти'", step_start_time, http_status)
    except Exception as e:
        http_status = None
        log_step(log, "Step 8", "FAIL", f"Ошибка: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 8: {e}")

    # Шаг 9: Проверка перехода на страницу всех питомцев
    step_start_time = time.time()
    try:
        assert selenium.current_url == "https://petfriends.skillfactory.ru/all_pets"
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 9", "PASS", "Открыта страница 'Все питомцы'", step_start_time, http_status)
    except Exception as e:
        http_status = get_http_status(selenium.current_url)
        log_step(log, "Step 9", "FAIL", f"Ошибка проверки: {e}", step_start_time, http_status)
        selenium.save_screenshot('Scr_shoots/' + str(uuid.uuid4()) + '.png')
        pytest.fail(f"Ошибка в шаге 9: {e}")

    # Итог
    total_duration = round(time.time() - test_start_time, 3)
    log_step(log, "Test", "PASS", f"Тест завершен успешно, Duration: {total_duration}s", test_start_time, None)
