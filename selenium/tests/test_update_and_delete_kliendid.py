# selenium/tests/test_kliendid_update_delete.py
from pages.kliendid_page import KliendidPage
from selenium.webdriver.common.by import By
import time

def test_update_and_delete_client(driver, config):
    page = KliendidPage(driver, config["base_url"])
    page.open()

    nimi = "Test Klient"
    telefon = "555-0101"
    email = "test@example.com"
    uus_nimi = "Uuendatud Klient"

    page.add_client(nimi, telefon, email)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    assert any(nimi in r.text for r in rows)

    edit_button = driver.find_element(
        By.XPATH, f"//tr[td[contains(text(), '{nimi}')]]//a[contains(text(),'Muuda') or contains(text(),'m')]"
    )
    edit_button.click()
    nimi_field = driver.find_element(By.NAME, "nimi")
    nimi_field.clear()
    nimi_field.send_keys(uus_nimi)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Salvesta']").click()
    time.sleep(1)
    rows_after_edit = driver.find_elements(By.CSS_SELECTOR, "table tr")
    assert any(uus_nimi in r.text for r in rows_after_edit)

    
    
    
    delete_button = driver.find_element(
        By.XPATH, f"//tr[td[contains(text(), '{uus_nimi}')]]//a[contains(text(),'Kustuta') or contains(text(),'x')]"
    )
    delete_button.click()
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass
    time.sleep(1)
    rows_after_delete = driver.find_elements(By.CSS_SELECTOR, "table tr")
    assert not any(uus_nimi in r.text for r in rows_after_delete)
