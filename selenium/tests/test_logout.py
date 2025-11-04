# selenium/tests/test_logout_fail.py
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_logout_fail(driver, config):
    page = LoginPage(driver, config["base_url"])
    page.open()
    page.login(config["users"]["admin"]["username"], config["users"]["admin"]["password"])

    driver.get(config["base_url"] + "logout.php")
    try:
        driver.find_element(By.CSS_SELECTOR, "div.alert-danger")
    except:
        assert "login.php" not in driver.current_url