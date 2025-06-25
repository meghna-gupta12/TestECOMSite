import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import config
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.excel_writer import write_to_excel


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(config.URL)
    yield driver
    driver.quit()


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(config.USERNAME, config.PASSWORD)
    time.sleep(2)
    assert "inventory" in driver.current_url
    print("Valid login successful")


def test_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(config.URL)

    login_page = LoginPage(driver)
    login_page.login(config.USERNAME, "wrong_password")
    error_message = login_page.get_error_message()

    assert error_message is not None
    print(f"Invalid Login Error Message Displayed: {error_message}")

    driver.quit()


def test_product_extraction(setup):
    driver = setup
    product_page = ProductPage(driver)
    product_page.sort_products_high_to_low()

    product_list = product_page.get_all_products()
    print("Products Extracted:", product_list)

    write_to_excel(product_list)
    print("Product details written to Excel successfully")
