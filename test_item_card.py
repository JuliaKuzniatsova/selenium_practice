from Data.conftest import driver_setup
from Data.conftest import login
from Locators.Locators import Locators
import time



class TestItemCard():
    locator = Locators()

    def test_click_on_item_image(self, driver_setup, login):
        driver = driver_setup

        item_image = driver.find_element(*self.locator.ITEM_IMAGE)
        item_image.click()

        assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
        time.sleep(2)

        driver.quit()


    def test_click_on_item_name(self, driver_setup, login):
        driver = driver_setup

        item_label = driver.find_element(*self.locator.ITEM_LABEL)
        item_label.click()

        assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=0"
        time.sleep(2)

        driver.quit()

