import config

class CartPage:
   def __init__(self, page):
       self.page = page
    
       self.title = page.locator(".title")
       self.cart_items = page.locator(".cart_item")
       self.checkout_button = page.locator("#checkout")
  
   def get_title(self):
       return self.title.inner_text()
   
   def get_cart_products(self):
       products = []
       count = self.cart_items.count()
       for i in range(count):
           item = self.cart_items.nth(i)
           name = item.locator(".inventory_item_name").inner_text()
           price_text = item.locator(".inventory_item_price").inner_text()
           price = float(price_text.replace("$", ""))
           products.append({"name": name, "price": price})
       return products
  
   def click_checkout(self):
       self.checkout_button.click()
       self.page.wait_for_url(config.INFO_PAGE_URL)