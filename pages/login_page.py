import config

# This class is for the Login page of SauceDemo
class LoginPage:
   def __init__(self, page):
       self.page = page
       self.username_box = page.locator("#user-name")
       self.password_box = page.locator("#password")
       self.login_button = page.locator("#login-button")

   def open(self):
       self.page.goto(config.BASE_URL)

   def login(self, username, password):
       self.username_box.fill(username)
       self.password_box.fill(password)
       self.login_button.click()