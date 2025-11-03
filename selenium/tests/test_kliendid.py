from pages.kliendid_page import KliendidPage
def test_add_client(driver, config):
    page = KliendidPage(driver, config["base_url"])
    page.open()
    page.add_client("Test Klient", "555-0101", "test@example.com")
    assert True  # TODO: проверить появление строки в таблице
