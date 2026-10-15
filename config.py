# ---------- links ----------
BASE_URL = "https://www.saucedemo.com/"
API_URL = "https://fakestoreapi.com/products"
API_TIMEOUT = 30

# ---------- login details ----------
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# ---------- browser settings ----------
HEADLESS = False
VIDEO_FOLDER = "videos"

# ---------- checkout details ----------
FIRST_NAME = "Test"
LAST_NAME = "User"
ZIP_CODE = "110001"

# ---------- expected text on pages ----------
INVENTORY_TITLE = "Products"
CART_TITLE = "Your Cart"
OVERVIEW_TITLE = "Checkout: Overview"
COMPLETE_TITLE = "Checkout: Complete!"
CONFIRMATION_MESSAGE = "Thank you for your order!"

# SauceDemo does not display category information
UI_CATEGORY = "Not shown on UI"

# ---------- page addresses (used to wait for page to open) ----------
CART_PAGE_URL = "**/cart.html"
INFO_PAGE_URL = "**/checkout-step-one.html"
OVERVIEW_PAGE_URL = "**/checkout-step-two.html"
COMPLETE_PAGE_URL = "**/checkout-complete.html"

# money is shown with 2 decimal places
PRICE_DECIMALS = 2