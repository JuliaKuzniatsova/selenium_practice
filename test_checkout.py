import time
from Data.conftest import driver_setup
from Data.conftest import login
from Data.conftest import add_to_cart
from Locators.Locators import Locators
from Data.conftest import checkout


class TestCheckout():
    locator = Locators()


    def test_checkout(self, driver_setup, login, add_to_cart, checkout):
        driver = driver_setup

        item, item_in_cart = add_to_cart
        assert item == item_in_cart

        assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
        time.sleep(2)

        finish_button = driver.find_element(*self.locator.FINISH_BTN)
        finish_button.click()
        time.sleep(2)

        assert driver.find_element(*self.locator.COMPLETE)

        driver.quit()
