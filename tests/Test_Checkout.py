from pages.LoginPage import LoginPage
from utilities.readconfig import ReadConfig
from utilities.logger import Logger
from pages.ProductListPage import ProductListPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

class TestCheckout:
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    firstname = ReadConfig.get_firstname()
    lastname = ReadConfig.get_lastname()
    zipcode = ReadConfig.get_zipcode()

    logger = Logger.get_logger()

    def test_click_checkout(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        self.logger.info('Test Case: Go to Checkout')
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.click_checkout()
        if 'your information' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_info_input(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.click_checkout()
        self.logger.info('Test Case: Validating info')
        self.checkout_page.set_firstname(self.firstname)
        self.checkout_page.set_lastname(self.lastname)
        self.checkout_page.set_zipcode(self.zipcode)
        self.logger.info('Test Case: Validating Checkout')
        self.checkout_page.click_continue()
        if 'overview' in self.driver.page_source.lower():
            assert True
        else:
            assert False

