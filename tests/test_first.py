import config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_and_read_products(page):

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(config.USERNAME, config.PASSWORD)

    inventory = InventoryPage(page)
    assert inventory.get_title() == "Products"

    products = inventory.get_all_products()

    for product in products:
        print(product["name"], product["price"])

    assert len(products) == 6