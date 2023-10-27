import selenium.common.exceptions
import time
from Data.conftest import driver_setup
from Data.conftest import login
from Data.conftest import add_to_cart
from Locators.Locators import Locators
from Data.conftest import item_card



class TestAddToCart():
    locator = Locators()


    def test_add_item_to_cart(self, driver_setup, login, add_to_cart):
        driver = driver_setup
        item, item_in_cart = add_to_cart

        assert item == item_in_cart

        driver.quit()


    def test_delete_item_from_cart(self, driver_setup, login, add_to_cart):
        driver = driver_setup
        item, item_in_cart = add_to_cart

        assert item == item_in_cart

        remove = driver.find_element(*self.locator.REMOVE_ITEM)
        remove.click()
        time.sleep(2)

        assert driver.find_element(*self.locator.REMOVED_ITEM)

        driver.quit()


    def test_add_item_to_cart_through_item_card(self, driver_setup, login, item_card):
        driver = driver_setup
        item_in_catalogue, item_in_cart = item_card

        assert item_in_catalogue == item_in_cart

        driver.quit()


    def test_delete_item_from_cart_through_item_card(self, driver_setup, login, item_card):
        driver = driver_setup
        item_in_catalogue, item_in_cart = item_card

        assert item_in_catalogue == item_in_cart

        back_to_item_card = driver.find_element(*self.locator.BACK_TO_ITEM_CARD)
        back_to_item_card.click()

        remove_from_cart = driver.find_element(*self.locator.REMOVE_ITEM)
        remove_from_cart.click()

        cart = driver.find_element(*self.locator.CART)
        cart.click()

        try:
            empty_cart = driver.find_element(*self.locator.ITEM)
            assert False
        except selenium.common.exceptions.NoSuchElementException:
            pass

        driver.quit()