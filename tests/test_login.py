from pages.LoginPage import LoginPage
from utilities.readconfig import ReadConfig
from utilities.logger import Logger


class TestLogin:
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    logger = Logger.get_logger()

    def test_login_page_title(self, setup):
        self.driver = setup
        page_title = self.driver.title
        self.logger.info('Test Case: Validating Loging Page Title')
        if page_title == 'Swag Labs':
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.logger.info('Test Case: Validating Loging Process')
        if 'products' in self.driver.page_source.lower():
            assert True
        else:
            assert False