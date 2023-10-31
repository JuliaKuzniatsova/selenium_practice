import pytest
from selenium import webdriver
from Data.Links import Links
from Locators.Locators import Locators
from Data.Entered_data_values import EnteredData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture(scope="function")
def driver_setup():
    driver = webdriver.Chrome()
    links = Links()
    driver.get(links.LOGIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    links = Links()
    driver.get(links.WAITS)
    yield driver
    driver.quit()


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--window-size=500,500')
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


@pytest.fixture(scope="function")
def login(driver_setup):
    enteredData = EnteredData()
    locators = Locators()

    username_field = driver_setup.find_element(*locators.USERNAME)
    username_field.send_keys(enteredData.USERNAME)

    password_field = driver_setup.find_element(*locators.PASSWORD)
    password_field.send_keys(enteredData.PASSWORD)

    login_button = driver_setup.find_element(*locators.LOGIN_BTN)
    login_button.click()

    yield


@pytest.fixture(scope="function")
def add_to_cart(driver_setup):
    locators = Locators()

    item = driver_setup.find_element(*locators.ITEM).text

    button_add_to_cart = driver_setup.find_element(*locators.ADD_TO_CART)
    button_add_to_cart.click()

    cart = driver_setup.find_element(*locators.CART)
    cart.click()

    item_in_cart = driver_setup.find_element(*locators.ITEM_IN_CART).text

    return item, item_in_cart


@pytest.fixture(scope="function")
def item_card(driver_setup):
    locators = Locators()

    item_in_catalogue = driver_setup.find_element(*locators.ITEM_IN_CATALOGUE).text

    item = driver_setup.find_element(*locators.ITEM).text

    button_add_to_cart = driver_setup.find_element(*locators.ADD_TO_CART)
    button_add_to_cart.click()

    cart = driver_setup.find_element(*locators.CART)
    cart.click()

    item_in_cart = driver_setup.find_element(*locators.ITEM_IN_CART).text

    return item_in_catalogue, item_in_cart


@pytest.fixture(scope="function")
def checkout(driver_setup):
    locator = Locators()
    enteredData = EnteredData()

    checkout_button = driver_setup.find_element(*locator.CHECKOUT_BTN)
    checkout_button.click()

    first_name_field = driver_setup.find_element(*locator.FIRST_NAME)
    first_name_field.send_keys(enteredData.FIRST_NAME)

    last_name_field = driver_setup.find_element(*locator.LAST_NAME)
    last_name_field.send_keys(enteredData.LAST_NAME)

    postal_code_field = driver_setup.find_element(*locator.POSTAL_CODE)
    postal_code_field.send_keys(enteredData.POSTAL_CODE)

    continue_button = driver_setup.find_element(*locator.CONTINUE_BTN)
    continue_button.click()

    yield


@pytest.fixture(scope="function")
def test_header(driver):
    locator = Locators()
    h1_element = driver.find_element(*locator.H1_ELEMENT)
    h1_text = h1_element.text

    expected_text = "Практика с ожиданиями в Selenium"

    if h1_text == expected_text:
        print("Текст в <h1> соответствует ожидаемому.")
    else:
        print("Текст в <h1> не соответствует ожидаемому.")

        driver.quit()


