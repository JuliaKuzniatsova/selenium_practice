import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_filter_A_to_Z():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    option = driver.find_element(By.XPATH, '//option[@value="az"]')
    option.click()
    time.sleep(2)

    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_label"]')
    original_item_names = [item.text for item in items]

    sorted_list_of_items = sorted(original_item_names, reverse=False)

    assert sorted_list_of_items == original_item_names, "Items are not sorted from A to Z"

    driver.quit()


def test_filter_Z_to_A():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    option = driver.find_element(By.XPATH, '//option[@value="za"]')
    option.click()
    time.sleep(2)

    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item_label"]')
    original_item_names = [item.text for item in items]

    sorted_list_of_items = sorted(original_item_names, reverse=True)

    assert sorted_list_of_items == original_item_names, "Items are not sorted from Z to A"

    driver.quit()


def test_filter_Low_to_High():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    option = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    option.click()
    time.sleep(2)

    item_prices = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    original_item_prices = [item.text for item in item_prices]

    numerical_prices = [float(price.replace('$', '')) for price in original_item_prices]

    sorted_item_prices = sorted(numerical_prices)

    assert sorted_item_prices == numerical_prices, "Prices are not sorted from low to high"

    driver.quit()


def test_filter_High_to_Low():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    option = driver.find_element(By.XPATH, '//option[@value="hilo"]')
    option.click()
    time.sleep(2)

    item_prices = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    original_item_prices = [item.text for item in item_prices]

    numerical_prices = [float(price.replace('$', '')) for price in original_item_prices]

    sorted_item_prices = sorted(numerical_prices, reverse=True)

    assert sorted_item_prices == numerical_prices, "Prices are not sorted from high to low"

    driver.quit()