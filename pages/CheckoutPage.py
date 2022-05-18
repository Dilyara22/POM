from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

class CheckoutPage:
    checkout_button_id = 'checkout'
    textbox_firstname_id = 'first-name'
    textbox_lastname_id = 'last-name'
    textbox_zipcode_id = 'postal-code'
    continue_button_id = 'continue'

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.ID, self.checkout_button_id).click()

    def set_firstname(self,firstname):   
        self.driver.find_element(By.ID, self. textbox_firstname_id).send_keys(firstname) 
        
    def set_lastname(self,lastname):   
        self.driver.find_element(By.ID, self. textbox_lastname_id).send_keys(lastname) 
    
    def set_zipcode(self,zipcode):   
        self.driver.find_element(By.ID, self. textbox_zipcode_id).send_keys(zipcode) 

    def click_continue(self):
        self.driver.find_element(By.ID, self.continue_button_id).click()