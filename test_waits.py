import time
from Data.conftest import chrome_options
from Data.conftest import driver
from Data.conftest import test_header
from Data.conftest import wait
from selenium.webdriver.support import expected_conditions as EC
from Data.conftest import Locators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TestRegistration:
    locator = Locators()


    def test_explicit_waits(self, chrome_options, driver, wait, test_header):
        driver = driver
        start_test_button = wait.until(EC.element_to_be_clickable(self.locator.START_TEST))
        assert start_test_button.text == 'Начать тестирование'
        start_test_button = driver.find_element(*self.locator.START_TEST)
        start_test_button.click()

        login = driver.find_element(*self.locator.LOGIN)
        login.send_keys("Login123")

        password = driver.find_element(*self.locator.PASS)
        password.send_keys("pass123")

        checkbox = driver.find_element(*self.locator.CHECKBOX)
        checkbox.click()

        registration_button = driver.find_element(*self.locator.REGISTRATION)
        registration_button.click()

        loader_invisible = wait.until(EC.invisibility_of_element_located(self.locator.LOADER))
        success = wait.until(EC.presence_of_element_located(self.locator.SUCCESS_MESSAGE))

        assert loader_invisible, "Loader is not invisible"
        assert success.text == 'Вы успешно зарегистрированы!', "Success message is not present"


    def test_implicit_waits(self, chrome_options, driver, test_header):
        driver = driver
        driver.implicitly_wait(5)

        start_test_button = driver.find_element(*self.locator.START_TEST)
        start_test_button.click()

        login = driver.find_element(*self.locator.LOGIN)
        login.send_keys("Login123")

        password = driver.find_element(*self.locator.PASS)
        password.send_keys("pass123")

        checkbox = driver.find_element(*self.locator.CHECKBOX)
        checkbox.click()

        registration_button = driver.find_element(*self.locator.REGISTRATION)
        registration_button.click()

        loader_invisible = driver.find_element(*self.locator.LOADER)
        assert loader_invisible, "Loader is not invisible"

        wait = WebDriverWait(driver, 6)

        success = wait.until(EC.visibility_of_element_located(self.locator.SUCCESS_MESSAGE))
        assert success.text == 'Вы успешно зарегистрированы!', "Success message is not present"


    def test_time_sleep_waits(self, chrome_options, driver, test_header):
        driver = driver
        time.sleep(5)

        start_test_button = driver.find_element(*self.locator.START_TEST)
        assert start_test_button.text == 'Начать тестирование'
        start_test_button.click()

        login = driver.find_element(*self.locator.LOGIN)
        login.send_keys("Login123")

        password = driver.find_element(*self.locator.PASS)
        password.send_keys("pass123")

        checkbox = driver.find_element(*self.locator.CHECKBOX)
        checkbox.click()

        registration_button = driver.find_element(*self.locator.REGISTRATION)
        registration_button.click()

        loader_invisible = driver.find_element(*self.locator.LOADER)
        assert loader_invisible, "Loader is not invisible"

        success = driver.find_element(*self.locator.SUCCESS_MESSAGE)
        time.sleep(5)
        assert success.text == 'Вы успешно зарегистрированы!', "Success message is not present"
