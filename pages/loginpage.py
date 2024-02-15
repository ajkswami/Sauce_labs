from seleniumbase import BaseCase

class Loginpage(BaseCase):
    page_logo = "div.login_logo"
    user_name = "#user-name"
    pass_word = "#password"
    login_button = "//input[@type='submit']"
    sucess_login_logo = "div[class='app_logo']"



    def open_page(self):
        self.open("https://www.saucedemo.com/")



    def enter_username(self,username):
        self.send_keys(self.user_name,username)

    def enter_pasword(self,password):
        self.send_keys(self.pass_word,password)

    def click_login_butn(self):
        self.click(self.login_button)




