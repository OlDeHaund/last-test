from selenium.webdriver.common.by import By

class JuuksuridPage:
    URL = "juuksurid.php"
    NAME = (By.NAME, "nimi")
    PHONE = (By.NAME, "telefon")
    EMAIL = (By.NAME, "email")
    ADD = (By.NAME, "lisa")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.URL)

    def add_master(self, nimi, telefon, email):
        self.driver.find_element(*self.NAME).send_keys(nimi)
        self.driver.find_element(*self.PHONE).send_keys(telefon)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.ADD).click()
