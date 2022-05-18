from pages.LoginPage import LoginPage
from utilities.readconfig import ReadConfig
from utilities.logger import Logger
from pages.ProductListPage import ProductListPage

class TestProductList:
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    logger = Logger.get_logger()

    def test_add_to_cart(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.logger.info('Test Case: Add to Cart')
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        if 'remove' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_product_added(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.logger.info('Test Case: Product added to cart')
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.product_added()
        if '1' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_click_remove(self, setup):
        self.driver = setup
        self.logger.info('Test Case: Remove item from cart')
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.product_added()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.click_remove()
        if 'add to cart' in self.driver.page_source.lower():
            assert True
        else:
            assert False