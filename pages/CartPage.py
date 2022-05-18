from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

class CartPage:
    shopping_cart_id = 'shopping_cart_container'
    remove_products_id = 'remove-sauce-labs-backpack'
    empty_shopping_cart_css='.shopping_cart_link'
    continue_shopping_id = 'continue-shopping'

    def __init__(self, driver):
        self.driver = driver

    def click_shopping_cart(self):
        self.driver.find_element(By.ID, self.shopping_cart_id).click()

    def click_remove(self):   
        self.driver.find_element(By.ID, self.remove_products_id).click() 
        return self.driver.find_element(By.CSS_SELECTOR, self.empty_shopping_cart_css).text != '1'     
        
    def click_continue_shopping(self):   
        self.driver.find_element(By.ID, self.continue_shopping_id).click() 