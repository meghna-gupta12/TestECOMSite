from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def sort_products_high_to_low(self):
        """Sort products from high price to low price."""
        sort_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("hilo")
        time.sleep(2)  # wait for sorting to apply

    def get_all_products(self):
        """Extract product details: name, description, and price in USD (as shown on website)."""
        product_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        products = []

        for item in product_elements:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            description = item.find_element(By.CLASS_NAME, "inventory_item_desc").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text  # Keep price as $XX.XX

            product = {
                "Product Name": name,
                "Product Description": description,
                "Product Price": price  # Example: $29.99
            }
            products.append(product)

        return products
