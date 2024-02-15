import pytest

from pages.loginpage import Loginpage
from selenium.common.exceptions import NoAlertPresentException,NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium import webdriver

username = "standard_user"
password = "secret_sauce"




class Test_loginpage(Loginpage):

    def setUp(self):
        super().setUp()
        print("Test begins")
        self.open_page()

    def tearDown(self):
        print("Test ends")
        print(self.page_logo)
        #self.assert_title(self.page_logo)
        super().tearDown()

    @pytest.mark.skip
    def test_checklogo(self):
        text = self.get_text(self.page_logo)
        self.assert_equal(text,"Swag Labs")

    @pytest.mark.tryfirst
    def test_login(self):

        self.enter_username(username)
        self.enter_pasword(password)
        self.click_login_butn()  # Corrected method call

        try:
            alert = self.driver.switch_to.alert  # Corrected
            alert_text = self.get_text(alert)
            print(f"OK: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No alert found.")

        print("Waiting for the success login logo to be visible...")

        try:
            self.wait_for_element_visible(self.sucess_login_logo, timeout=10)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

        login_sucess_logo = self.get_text(self.sucess_login_logo)
        #self.save_screenshot("loginsuccess.png")
        self.assert_equal(login_sucess_logo, "Swag Labs", "Login successful logo does not match expected")
        self.save_screenshot_after_test = True  # or False
