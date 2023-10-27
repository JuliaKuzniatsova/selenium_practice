import time
from Data.conftest import driver_setup
from Data.conftest import login
from Locators.Locators import Locators


class TestAuthorization:
    locator = Locators()

    def test_login_form_with_correct_data(self, driver_setup, login):
        driver = driver_setup
        time.sleep(2)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        driver.quit()



    def test_login_form_with_incorrect_data(self, driver_setup):
       driver = driver_setup

       username_field = driver.find_element(*self.locator.USERNAME)
       username_field.send_keys("user")

       password_field = driver.find_element(*self.locator.PASSWORD)
       password_field.send_keys("user")

       login_button = driver.find_element(*self.locator.LOGIN_BTN)
       login_button.click()

       time.sleep(2)
       assert driver.find_element(*self.locator.LOGIN_ERROR)

       driver.quit()
