from pages.LoginPage import LoginPage
from utilities.readconfig import ReadConfig
from utilities.logger import Logger
from pages.ProductListPage import ProductListPage
from pages.CartPage import CartPage

class TestCart:
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    logger = Logger.get_logger()

    def test_click_shopping_cart(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.logger.info('Test Case: Go to Cart')
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        if 'your cart' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_click_remove(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        self.logger.info('Test Case: Empty shopping cart')    
        self.cart_page.click_remove()
        if '1' in self.driver.page_source.lower():
            assert True
        else:
            assert False
    
    def test_click_continue_shopping(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()   
        self.cart_page.click_remove()
        self.logger.info('Test Case: Continue shopping') 
        self.cart_page.click_continue_shopping()
        if 'products' in self.driver.page_source.lower():
            assert True
        else:
            assert False