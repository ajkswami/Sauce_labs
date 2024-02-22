


import time
import pytest
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.loginpage import Loginpage
from selenium import webdriver

from configuration import testdata

from datetime import datetime

# Used Data driven frame work via pandas

class TestDDT(Loginpage):

    def setUp(self):
        super().setUp()
        print("Test begins")
        self.open_page()

    def tearDown(self):
        print("Test ends")
        print(self.page_logo)
        super().tearDown()

    @pytest.mark.mark1
    def test_check_logo(self):
        text = self.get_text(self.page_logo)
        self.assert_equal(text, "Swag Labs")

    @pytest.mark.mark2
    def test_login(self):
        file_path = "C:/Users/pc/Downloads/test_data.xlsx"
        df = pd.read_excel(file_path)

        successful_login = False  # Initialize successful_login flag

        for index, row in df.iterrows():
            cell_username = row['username']
            cell_pass_word = row['password']
            # Manually invoke the fixture
            self.enter_username(cell_username)
            time.sleep(1)
            self.enter_pasword(cell_pass_word)
            time.sleep(1)
            self.click_login_butn()
            time.sleep(1)

            try:
                error_h3 = self.driver.find_element(By.CSS_SELECTOR,"h3" )
                error_msg = error_h3.text



                # Update DataFrame with error message
                df.at[index, "result"] = error_msg
                df.at[index, "date & time"] = f" Login status is Failed at: {datetime.now()}"  # Add date and time stamp

            except NoSuchElementException as e:
                print(f"Logged in Succesful with {e}")
                # Update DataFrame with success message
                df.at[index, "result"] = "Login Sucessful"
                df.at[index, "data & time"] = f" Login status is Success at: {datetime.now()}"
                successful_login = True

            self.refresh_page()
            time.sleep(4)


        # Write updated DataFrame back to Excel file
        df.to_excel(file_path, index=False)

        if successful_login:
            print("All tests are done")


        try:
            self.wait_for_element_visible(self.sucess_login_logo, timeout=10)
            successful_login = True

            sucess_txt = self.get_text(self.sucess_login_logo)
            self.assert_equal(sucess_txt, "Swag Labs", "Login successful logo does not match expected")
            self.save_screenshot_after_test = True
            print(f"Login Assertion is passed with {sucess_txt} as title ")

        except NoSuchElementException as e:
            print(f"Fail and exception is {e}")

