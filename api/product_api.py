import requests
import config

# API methods
class ProductAPI:
   def get_all_products(self):
       response = requests.get(config.API_URL, timeout=config.API_TIMEOUT)
     
       assert response.status_code == 200, "API failed, status code: " + str(response.status_code)
       data = response.json()
       products = []
       for item in data:
           product = {
               "id": item["id"],
               "name": item["title"],
               "price": float(item["price"]),
               "category": item["category"],
           }
           products.append(product)
       return products