from selenium.webdriver.common.by import By

class LoginPage:
    URL = "login.php"
    USERNAME = (By.NAME, "login")
    PASSWORD = (By.NAME, "parool")
    SUBMIT   = (By.CSS_SELECTOR, "button, input[type=submit]")
    ERROR    = (By.CSS_SELECTOR, ".error, .alert-danger")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()
