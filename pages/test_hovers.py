from selenium.webdriver.common.action_chains import ActionChains
from seleniumbase import BaseCase


class Test_Hovers(BaseCase):
    Baseurl = "https://www.toolsqa.com/"  # URL
    url_logo = "//img[@alt='Tools QA']"  # XPath
    menu_icon = "//span[@class='navbar__tutorial-menu--menu-bars']"  # XPath
    black_box_test = "//li[div/span[contains(text(),'Back-End Testing Automation')]]"  # Family XPath
    hover_of_bbt = './/div[2]/div/ul/li[2]/a'  # Relative XPath
    success = "//h1[@class='article-meta-data__title']"

    def test_check_black_box_hover(self):
        self.open(self.Baseurl)

        # Click on the menu icon to reveal the submenu
        self.click(self.menu_icon)

        # Wait for the black_box_test element to be visible
        self.wait_for_element_visible(self.black_box_test)

        # Find the black_box_test element
        black_box_element = self.wait_for_element_present(self.black_box_test)


        # Create an ActionChains object
        actions = ActionChains(self.driver)


        # Hover over the black_box_test element and then move to hover_of_bbt_element

        actions.move_to_element(black_box_element).perform()
        hover_of_bbt_element = self.wait_for_element_present(self.hover_of_bbt)
        actions.move_to_element(hover_of_bbt_element).click().perform()
        self.wait_for_element_present(self.success)




        txt=self.get_text(self.success)



        self.assert_equal(txt,"Rest Assured Tutorial")
