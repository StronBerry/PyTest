import time
import uuid
import requests
import csv
import os

def log_step(log_file, step, result, description, start_time, status_code=None):
    """Функция для логирования шага теста."""
    duration = round(time.time() - start_time, 3)
    print(f"Logging step: {step}, Result: {result}, Duration: {duration}s, HTTP Status Code: {status_code}")
    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([step, result, description, duration, status_code])

def log_to_txt(log_file, step, result, description):
    """
    Функция для записи одного шага в лог.
    Лог сохраняется в папке /LOG/ с именем ЧЧ_ММ_СС_ДД_ММ_ГГ.txt.

    :param log_file: Имя файла лога (должно быть единым для всех шагов)
    :param step: Номер шага
    :param result: Результат шага (например, PASS, FAIL, INFO)
    :param description: Описание шага
    """
    # Создаем папку для логов, если она отсутствует
    log_dir = "LOG"
    os.makedirs(log_dir, exist_ok=True)

    # Создаем файл лога с уникальным именем, если он не передан
    if log_file is None:
        timestamp = time.strftime("%H_%M_%S_%d_%m_%y")
        log_file = os.path.join(log_dir, f"{timestamp}.txt")

    # Формируем строку лога
    log_line = f"{step}. [{result}] {description}"

    # Записываем строку в файл
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(log_line + "\n")

    print(f"Шаг записан в лог: {log_line}")
    return log_file


def get_http_status(url):
    """Функция для получения HTTP-кода состояния страницы."""
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException:
        return None

def save_screenshot(driver, folder="Scr_shoots"):
    """Функция для сохранения скриншота текущей страницы."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    screenshot_path = os.path.join(folder, str(uuid.uuid4()) + '.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    return screenshot_path
