import config

class InventoryPage:
   def __init__(self, page):
       self.page = page

       self.title = page.locator(".title")
       self.all_items = page.locator(".inventory_item")
       self.cart_icon = page.locator(".shopping_cart_link")

   def get_title(self):
       return self.title.inner_text()

   def get_all_products(self):
       self.all_items.first.wait_for()
       products = []
       count = self.all_items.count()
       for i in range(count):
           item = self.all_items.nth(i)
           name = item.locator(".inventory_item_name").inner_text()
           description = item.locator(".inventory_item_desc").inner_text()
           price_text = item.locator(".inventory_item_price").inner_text()

           price = float(price_text.replace("$", ""))
           product = {
               "name": name,
               "description": description,
               "price": price,
               "category": config.UI_CATEGORY,
           }
           products.append(product)
       return products

   def add_product_to_cart(self, product_name):
       item = self.all_items.filter(has_text=product_name)
       item.locator("button").click()
       
   def go_to_cart(self):
       self.cart_icon.click()
       self.page.wait_for_url(config.CART_PAGE_URL)