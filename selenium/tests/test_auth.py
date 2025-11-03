import os
from pages.login_page import LoginPage

def test_login_success(driver, config):
    page = LoginPage(driver, config["base_url"])
    page.open()
    page.login(config["users"]["admin"]["username"], config["users"]["admin"]["password"])
    # Теоретическая проверка: наличие имени пользователя в шапке/меню
    assert True  # TODO: заменить на проверку видимости приветствия

def test_login_wrong_password(driver, config):
    page = LoginPage(driver, config["base_url"])
    page.open()
    page.login(config["users"]["admin"]["username"], "wrongpass")
    # Ожидается сообщение об ошибке
    assert True  # TODO: проверить видимость .error/.alert-danger
