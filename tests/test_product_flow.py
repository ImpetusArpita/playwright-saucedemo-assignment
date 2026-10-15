import allure

from playwright.sync_api import expect

import config
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from api.product_api import ProductAPI
from utils.helper import attach_data, pair_products, compare_products
from utils.helper import find_highest_and_lowest, check_same_products

@allure.feature("Product Validation")
@allure.title("Compare product details on UI with FakeStore API")
def test_compare_ui_with_api(logged_in_page):
   inventory = InventoryPage(logged_in_page)
   api = ProductAPI()
   with allure.step("Check user is on inventory page"):
       expect(inventory.title).to_have_text(config.INVENTORY_TITLE)
   with allure.step("Capture all products from UI"):
       ui_products = inventory.get_all_products()
       print("Products on UI: " + str(len(ui_products)))
       attach_data("UI products", ui_products)
   with allure.step("Get all products from API"):
       api_products = api.get_all_products()
       print("Products in API: " + str(len(api_products)))
       attach_data("API products", api_products)
   with allure.step("Compare name, price and category"):
       pairs = pair_products(ui_products, api_products)
       mismatches = compare_products(pairs)
       attach_data("Mismatches", mismatches)
       for m in mismatches:
           print("Product " + str(m["product_no"]) + " - " + m["field"] +
                 " mismatch -> UI: " + str(m["ui_value"]) + " | API: " + str(m["api_value"]))

   assert len(mismatches) == 0, str(len(mismatches)) + " mismatches found between UI and API"

@allure.feature("Checkout Flow")
@allure.title("Add highest and lowest priced products and complete checkout")
def test_checkout_highest_and_lowest(logged_in_page):
   inventory = InventoryPage(logged_in_page)
   cart = CartPage(logged_in_page)
   checkout = CheckoutPage(logged_in_page)
   api = ProductAPI()
   with allure.step("Get products from UI and API"):
       ui_products = inventory.get_all_products()
       api_products = api.get_all_products()
       pairs = pair_products(ui_products, api_products)
   with allure.step("Find highest and lowest priced product from API"):
       highest, lowest = find_highest_and_lowest(pairs)
       selected = [highest["ui"], lowest["ui"]]
       print("Highest (API): " + highest["api"]["name"] + " -> UI: " + highest["ui"]["name"])
       print("Lowest (API): " + lowest["api"]["name"] + " -> UI: " + lowest["ui"]["name"])
       attach_data("Selected products", selected)
   with allure.step("Add both products to cart"):
       for product in selected:
           inventory.add_product_to_cart(product["name"])
       inventory.go_to_cart()
   with allure.step("Validate products on Cart page"):
       expect(cart.title).to_have_text(config.CART_TITLE)
       cart_products = cart.get_cart_products()
       attach_data("Cart products", cart_products)
       check_same_products(selected, cart_products, "Cart")
       cart.click_checkout()
   with allure.step("Fill checkout information"):
       checkout.fill_information(config.FIRST_NAME, config.LAST_NAME, config.ZIP_CODE)
   with allure.step("Validate products and subtotal on Overview page"):
       expect(checkout.title).to_have_text(config.OVERVIEW_TITLE)
       overview_products = checkout.get_overview_products()
       attach_data("Overview products", overview_products)
       check_same_products(selected, overview_products, "Checkout Overview")
    
       expected_subtotal = 0
       for product in selected:
           expected_subtotal = expected_subtotal + product["price"]
       expected_subtotal = round(expected_subtotal, config.PRICE_DECIMALS)
       subtotal = checkout.get_subtotal()
       tax = checkout.get_tax()
       total = checkout.get_total()
       attach_data("Price summary", {
           "expected_subtotal": expected_subtotal,
           "subtotal_on_page": subtotal,
           "tax": tax,
           "total": total,
       })
       assert subtotal == expected_subtotal, "Subtotal wrong. Expected " + str(expected_subtotal) + " but got " + str(subtotal)
       assert round(subtotal + tax, config.PRICE_DECIMALS) == total, "Total is not equal to subtotal + tax"
   with allure.step("Finish order and validate Confirmation page"):
       checkout.click_finish()
       expect(checkout.title).to_have_text(config.COMPLETE_TITLE)
       expect(checkout.complete_header).to_have_text(config.CONFIRMATION_MESSAGE)