from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
from seleniumbase.fixtures.page_actions import wait_for_element_visible
from selenium import webdriver

from configuration.configtest import Configtest

class Test_Dashboard(Configtest,BaseCase):
    footer_txt = "div.footer_copy"



    def test_get_sorted_lst(self):
        # Use the login method from the base class
        self.test_get_login()

        # Wait for the select element to be visible
        self.wait_for_element_visible(self.sort_container)
        self.assert_element_present(self.sort_container, timeout=20)
        #
        #
        self.assert_text_visible("© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy")

        # Find the select element
        select_ele = self.find_element(self.sort_container)


        option_texts = list(map(lambda option: option.text, select_ele.find_elements(By.TAG_NAME, "option")))

        print(option_texts)

        expected_txt = self.get_text(self.footer_txt)
        actual_txt = "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        assert actual_txt == expected_txt



