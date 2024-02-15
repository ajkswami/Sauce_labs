from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

class Configtest(BaseCase):
    BaseUrl = "https://www.saucedemo.com/"
    user_name = "#user-name"
    pass_word = "#password"
    login_button = "//input[@type='submit']"
    sort_container = ".product_sort_container"
    error_msg_text = '//button[contains(@class, "error-button")]/text()'

    def test_get_login(self):
        self.open(self.BaseUrl)
        self.send_keys(self.user_name, "standard_user")
        self.send_keys(self.pass_word, "secret_sauce")
        self.click(self.login_button)
        # self.wait_for_element_visible(self.error_msg_text, timeout=10)
        # txt = self.get_text(self.error_msg_text)
        # print(txt)


        # self.driver.find_element('//button[contains(@class, "error-button")]/text()')

        self.wait_for_element_visible(self.sort_container)
        self.assert_element_present(self.sort_container)












    #  this below code is for dummy checks and to avoid misatkes in POM
    #
    #  to get elements  test execution  purpose only use it
    #
    # def test_get_dashboard(self):
    #     self.open(self.BaseUrl)
    #     self.send_keys("#user-name", "standard_user")
    #     self.send_keys("#password", "secret_sauce")
    #     self.click(self.login_button)
    #
    #
    #     self.wait_for_element_visible(self.sort_container)
    #
    #     # Find the select element
    #     select_ele = self.find_element(self.sort_container)
    #
    #     # Find all option elements within the select
    #     options = select_ele.find_elements(By.TAG_NAME, "option")
    #
    #     # Extract text from each option and store it in a list
    #     option_texts = [option.text for option in options]
    #
    #     # Print the list of option texts
    #     print(option_texts)
    #
    #
    #
    #
    #
    #     # text = self.get_text(".product_sort_container")
    #     # new_lst = list(text)
    #     # print(new_lst)
    #
    #















