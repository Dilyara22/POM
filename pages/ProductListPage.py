from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

class ProductListPage:
    add_to_cart_button_id = 'add-to-cart-sauce-labs-backpack'
    shopping_cart_symbol_css = '.shopping_cart_badge'
    button_remove_id = 'remove-sauce-labs-backpack'

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, self.add_to_cart_button_id).click()

    def product_added(self):   
        return self.driver.find_element(By.CSS_SELECTOR, self.shopping_cart_symbol_css).text == '1'
        
    def click_remove(self):   
        self.driver.find_element(By.ID, self.button_remove_id).click() 
   
