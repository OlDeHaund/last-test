from selenium.webdriver.common.by import By

class KliendidPage:
    URL = "kliendid.php"
    NAME = (By.NAME, "nimi")
    PHONE = (By.NAME, "telefon")
    EMAIL = (By.NAME, "email")
    ADD = (By.NAME, "lisa")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.URL)

    def add_client(self, nimi, telefon, email):
        self.driver.find_element(*self.NAME).send_keys(nimi)
        self.driver.find_element(*self.PHONE).send_keys(telefon)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.ADD).click()
