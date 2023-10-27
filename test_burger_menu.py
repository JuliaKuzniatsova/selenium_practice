import time
from Data.conftest import driver_setup
from Data.conftest import login
from Locators.Locators import Locators
from Data.Entered_data_values import EnteredData


class TestBurgerMenu():
    locator = Locators()
    enteredData = EnteredData()


    def test_logout(self, driver_setup):
        driver = driver_setup

        url_before = driver.current_url

        username_field = driver_setup.find_element(*self.locator.USERNAME)
        username_field.send_keys(*self.enteredData.USERNAME)

        password_field = driver_setup.find_element(*self.locator.PASSWORD)
        password_field.send_keys(*self.enteredData.PASSWORD)

        login_button = driver_setup.find_element(*self.locator.LOGIN_BTN)
        login_button.click()

        burger_menu = driver.find_element(*self.locator.BURGER_MENU)
        burger_menu.click()
        time.sleep(2)

        logout_button = driver.find_element(*self.locator.LOGOUT_BTN)
        logout_button.click()
        time.sleep(1)

        url_after = driver.current_url
        assert url_before == url_after

        driver.quit()


    def test_about(self, driver_setup, login):
        driver = driver_setup

        burger_menu = driver.find_element(*self.locator.BURGER_MENU)
        burger_menu.click()
        time.sleep(2)

        about_button = driver.find_element(*self.locator.ABOUT_BTN)
        about_button.click()
        time.sleep(2)

        about_page_url = driver.current_url
        expected_url = "https://saucelabs.com/"
        assert about_page_url == expected_url

        driver.quit()