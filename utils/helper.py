import json
import allure

def attach_data(name, data):
   text = json.dumps(data, indent=4)
   allure.attach(text, name=name, attachment_type=allure.attachment_type.JSON)

def pair_products(ui_products, api_products):
   pairs = []
   for i in range(len(ui_products)):
       if i < len(api_products):
           pairs.append({"ui": ui_products[i], "api": api_products[i]})
   return pairs

def compare_products(pairs):
   mismatches = []
   fields = ["name", "price", "category"]
   number = 1
   for pair in pairs:
       for field in fields:
           ui_value = pair["ui"][field]
           api_value = pair["api"][field]
           if ui_value != api_value:
               mismatch = {
                   "product_no": number,
                   "field": field,
                   "ui_value": ui_value,
                   "api_value": api_value,
               }
               mismatches.append(mismatch)
       number = number + 1
   return mismatches

def find_highest_and_lowest(pairs):
   highest = pairs[0]
   lowest = pairs[0]
   for pair in pairs:
       if pair["api"]["price"] > highest["api"]["price"]:
           highest = pair
       if pair["api"]["price"] < lowest["api"]["price"]:
           lowest = pair
   return highest, lowest

def check_same_products(expected, actual, page_name):
   assert len(actual) == len(expected), page_name + " page has wrong number of items"
   for product in expected:
       found = False
       for item in actual:
           if item["name"] == product["name"]:
               found = True
               assert item["price"] == product["price"], "Price of " + product["name"] + " is different on " + page_name + " page"
       assert found, product["name"] + " is missing on " + page_name + " page"