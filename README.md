#  ECOM Price Tracker - Selenium Automation Framework

##  Project Description

This project is a Selenium-based automation framework that:

- Logs into an e-commerce website ([saucedemo.com](https://www.saucedemo.com)).
- Sorts products by **highest to lowest price**.
- Extracts **Product Name**, **Price**, and **Description**.
- Saves the data into an Excel file with a **timestamp**.

It also includes a negative test case to validate incorrect login attempts.

---

##  Functional Requirements

###  Login Automation
- URL: [https://www.saucedemo.com](https://www.saucedemo.com)
- Login with credentials:
  - **Username:** `standard_user`
  - **Password:** `secret_sauce`
- Invalid login test with wrong password to verify error message handling.

###  Product Price Extraction
- Sort products from **High to Low**.
- Extract:
  - Product Name
  - Product Price
  - Product Description

###  Excel Report Generation
- Data saved to an Excel file (`Product_Data.xlsx`) with columns:
  - Product Name
  - Price
  - Description
  - Timestamp

---

##  Project Structure

