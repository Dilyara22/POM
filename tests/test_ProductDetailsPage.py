from pages.LoginPage import LoginPage
from utilities.readconfig import ReadConfig
from utilities.logger import Logger
from pages.ProductDetailsPage import ProductDetailsPage


class TestProductDetails:
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    logger = Logger.get_logger()

    def test_product_details(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.logger.info('Test Case: Check product details')
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.product_details()
        if 'back to products' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_add_to_cart(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.product_details()
        self.logger.info('Test Case: Add to Cart from Product Details Page')
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.add_to_cart()
        if 'remove' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_back_to_products(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.product_details()
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.add_to_cart()
        self.logger.info('Test Case: Back to Products List')
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.back_to_products()
        if 'products' in self.driver.page_source.lower():
            assert True
        else:
            assert False

