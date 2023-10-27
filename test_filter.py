import time
from Data.conftest import driver_setup
from Data.conftest import login
from Locators.Locators import Locators


class TestFilter():
    locator = Locators()

    def test_filter_A_to_Z(self, driver_setup, login):
        driver = driver_setup

        option = driver.find_element(*self.locator.AZ_OPTION)
        option.click()
        time.sleep(2)

        items = driver.find_elements(*self.locator.ITEMS)
        original_item_names = [item.text for item in items]

        sorted_list_of_items = sorted(original_item_names, reverse=False)

        assert sorted_list_of_items == original_item_names, "Items are not sorted from A to Z"

        driver.quit()


    def test_filter_Z_to_A(self, driver_setup, login):
        driver = driver_setup

        option = driver.find_element(*self.locator.ZA_OPTION)
        option.click()
        time.sleep(2)

        items = driver.find_elements(*self.locator.ITEMS)
        original_item_names = [item.text for item in items]

        sorted_list_of_items = sorted(original_item_names, reverse=True)

        assert sorted_list_of_items == original_item_names, "Items are not sorted from Z to A"

        driver.quit()


    def test_filter_Low_to_High(self, driver_setup, login):
        driver = driver_setup

        option = driver.find_element(*self.locator.LOHI_OPTION)
        option.click()
        time.sleep(2)

        item_prices = driver.find_elements(*self.locator.ITEM_PRICES)
        original_item_prices = [item.text for item in item_prices]

        numerical_prices = [float(price.replace('$', '')) for price in original_item_prices]

        sorted_item_prices = sorted(numerical_prices)

        assert sorted_item_prices == numerical_prices, "Prices are not sorted from low to high"

        driver.quit()


    def test_filter_High_to_Low(self, driver_setup, login):
        driver = driver_setup

        option = driver.find_element(*self.locator.HILO_OPTION)
        option.click()
        time.sleep(2)

        item_prices = driver.find_elements(*self.locator.ITEM_PRICES)
        original_item_prices = [item.text for item in item_prices]

        numerical_prices = [float(price.replace('$', '')) for price in original_item_prices]

        sorted_item_prices = sorted(numerical_prices, reverse=True)

        assert sorted_item_prices == numerical_prices, "Prices are not sorted from high to low"

        driver.quit()