from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

class ProductDetailsPage:
    product_details_class = 'inventory_item_name'
    add_to_cart_button_id = 'add-to-cart-sauce-labs-backpack'
    back_to_products_id = 'back-to-products'

    def __init__(self, driver):
        self.driver = driver

    def product_details(self):
        self.driver.find_element(By.CLASS_NAME, self.product_details_class).click()

    def add_to_cart(self):
        self.driver.find_element(By.ID, self.add_to_cart_button_id).click()

    def back_to_products(self):
        self.driver.find_element(By.ID, self.back_to_products_id).click()

 