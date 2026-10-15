import config

# This class is for the 3 checkout pages:
# 1. Your Information  2. Overview  3. Complete
class CheckoutPage:
   def __init__(self, page):
       self.page = page
       self.title = page.locator(".title")
       # page 1 - your information
       self.first_name = page.locator("#first-name")
       self.last_name = page.locator("#last-name")
       self.postal_code = page.locator("#postal-code")
       self.continue_button = page.locator("#continue")
       # page 2 - overview
       self.overview_items = page.locator(".cart_item")
       self.subtotal_label = page.locator(".summary_subtotal_label")
       self.tax_label = page.locator(".summary_tax_label")
       self.total_label = page.locator(".summary_total_label")
       self.finish_button = page.locator("#finish")
       # page 3 - complete
       self.complete_header = page.locator(".complete-header")
  
   def get_title(self):
       return self.title.inner_text()

   def fill_information(self, first, last, zip_code):
       self.first_name.fill(first)
       self.last_name.fill(last)
       self.postal_code.fill(zip_code)
       self.continue_button.click()
       self.page.wait_for_url(config.OVERVIEW_PAGE_URL)
  
   def get_overview_products(self):
       products = []
       count = self.overview_items.count()
       for i in range(count):
           item = self.overview_items.nth(i)
           name = item.locator(".inventory_item_name").inner_text()
           price_text = item.locator(".inventory_item_price").inner_text()
           price = float(price_text.replace("$", ""))
           products.append({"name": name, "price": price})
       return products

   def get_amount(self, label):
       text = label.inner_text()
       amount = text.split("$")[1]
       return round(float(amount), config.PRICE_DECIMALS)
   def get_subtotal(self):
       return self.get_amount(self.subtotal_label)
   def get_tax(self):
       return self.get_amount(self.tax_label)
   def get_total(self):
       return self.get_amount(self.total_label)
 
   def click_finish(self):
       self.finish_button.click()
       self.page.wait_for_url(config.COMPLETE_PAGE_URL)

   def get_confirmation_message(self):
       return self.complete_header.inner_text()