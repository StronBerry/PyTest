import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="session")
def selenium():
    # Создание экземпляра WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_petfriends(selenium):
    # Открыть базовую страницу PetFriends:
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Кликнуть на кнопку нового пользователя
    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # Кликнуть на кнопку для существующего пользователя
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # Ввести email
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("stron@gmail.com")

    # Ввести пароль
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("qwertyuiop")

    # Кликнуть на кнопку отправки формы
    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Проверка, что текущий URL совпадает с нужным
    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Сделать скриншот окна браузера
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")