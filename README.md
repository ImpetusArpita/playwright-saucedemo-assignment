Playwright Python Assignment
Project Overview:

This project is created using Python, Playwright and Pytest.

The assignment covers:

Login to SauceDemo website
Read product information from UI
Read product information from FakeStore API
Compare UI and API data
Find highest and lowest priced products
Add products to cart
Complete checkout process
Generate Allure reports
Capture screenshot and video when a test fails

Project Structure:

playwright_assignment/

├── api/

├── pages/

├── tests/

├── utils/

├── screenshots/

├── videos/

├── config.py

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md

Technologies Used:

Python
Playwright
Pytest
Requests
Allure Reporting

Installation:

Create virtual environment:
python -m venv venv

Activate virtual environment:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Install Playwright browsers:
playwright install

Run Tests:

Run all tests:
pytest

Run tests and generate Allure results:
pytest --alluredir=allure-results

Generate Allure Report
allure serve allure-results

Test Scenarios:


Test 1
Login to SauceDemo and verify all products are displayed.

Test 2
Compare product details available on UI with FakeStore API data and report mismatches.

Test 3
Find highest and lowest priced products, add them to cart, complete checkout and verify order confirmation.

Result:
Three test cases were executed.

test_login_and_read_products → Passed
test_checkout_highest_and_lowest → Passed
test_compare_ui_with_api → Failed (Expected)

Reason:

SauceDemo and FakeStore API contain different product data.

The comparison test is designed to identify mismatches between UI and API. During execution, mismatches were detected in product name, price and category values.

This failure is expected and demonstrates that the validation logic is working correctly.

Screenshot and video are automatically attached in the Allure report when a test fails.

Notes:

Standard SauceDemo user credentials are used.
Configuration values are stored in config.py.
Video recording is enabled for failed tests.
Screenshots are captured automatically on failure.