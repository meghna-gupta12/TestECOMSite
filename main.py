import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config import config
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.excel_writer import write_to_excel


def main():
    # Setup Chrome options to keep browser open after script finishes
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # 🔥 This keeps Chrome open

    # Setup WebDriver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()

    try:
        # Open URL
        driver.get(config.URL)

        # Login
        login_page = LoginPage(driver)
        login_page.login(config.USERNAME, config.PASSWORD)
        time.sleep(2)  # Wait for the page to load

        # Check if login is successful
        if "inventory" not in driver.current_url:
            error_message = login_page.get_error_message()
            print(f"Login failed with error: {error_message}")
            return  # Stop execution if login fails
        else:
            print("Login Successful")

        # Sort products from high to low
        product_page = ProductPage(driver)
        product_page.sort_products_high_to_low()
        time.sleep(2)  # Wait for sorting to apply

        # Extract product details
        product_list = product_page.get_all_products()

        if product_list:
            print("\nExtracted Product Details:\n")
            for product in product_list:
                print(product)

            # Write data to Excel
            write_to_excel(product_list)
            print("\nProduct data written successfully to Product_Data.xlsx\n")
        else:
            print("No products found on the page.")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        # Optional: Close browser
        # If you want the browser to close automatically after run, uncomment below:
        # driver.quit()
        
        # With 'detach' enabled, browser stays open even after script finishes.
        print("Script completed. Browser will remain open until you close it manually.")


if __name__ == "__main__":
    main()
