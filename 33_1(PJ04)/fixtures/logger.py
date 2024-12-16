import pytest
import logging
from datetime import datetime
import os

@pytest.fixture(scope="session", autouse=True)
def logger():
    """
    Фикстура для настройки логгера и записи логов в файл.
    """
    log_dir = "./logs"
    os.makedirs(log_dir, exist_ok=True)

    # Генерируем имя лог-файла
    now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    log_file = os.path.join(log_dir, f"{now}.txt")

    # Настройка логгера
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    # Создаем файл-хендлер
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.INFO)

    # Настройка формата логов
    formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    # Добавляем файл-хендлер к логгеру
    if not logger.handlers:  # Убедитесь, что хендлеры не дублируются
        logger.addHandler(file_handler)

    # Выводим в консоль путь к лог-файлу
    print(f"Логи будут сохранены в файл: {log_file}")

    return logger
