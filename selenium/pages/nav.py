from selenium.webdriver.common.by import By

class Nav:
    LOGOUT = (By.LINK_TEXT, "Väljalogimine")
    LOGIN  = (By.LINK_TEXT, "Sisselogimine")
    KLIENDID = (By.LINK_TEXT, "Kliendid")
    JUUKSURID = (By.LINK_TEXT, "Juuksurid")
    TELLIMUSED = (By.LINK_TEXT, "Tellimused")

    def __init__(self, driver):
        self.driver = driver
