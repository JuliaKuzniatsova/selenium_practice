import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_item_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name ']").text
    time.sleep(3)

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
    button_add_to_cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    item_in_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']").text
    assert item == item_in_cart

    driver.quit()


def test_delete_item_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name ']").text

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
    button_add_to_cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    item_in_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']").text
    assert item == item_in_cart

    remove = driver.find_element(By.CSS_SELECTOR, "button[data-test='remove-test.allthethings()-t-shirt-(red)']")
    remove.click()
    time.sleep(2)

    assert driver.find_element(By.CSS_SELECTOR, "div[class='removed_cart_item']")

    driver.quit()


def test_add_item_to_cart_through_item_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_in_catalogue = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name ']").text

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name ']")
    item.click()
    time.sleep(2)

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    button_add_to_cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    item_in_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name']").text
    assert item_in_catalogue == item_in_cart

    driver.quit()


def test_delete_item_from_cart_through_item_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_in_catalogue = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name ']").text

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name ']")
    item.click()

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    button_add_to_cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    item_in_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name']").text
    assert item_in_catalogue == item_in_cart

    back_to_item_card = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name']")
    back_to_item_card.click()

    remove_from_cart = driver.find_element(By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-bolt-t-shirt']")
    remove_from_cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    try:
        empty_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name']")
        assert False
    except selenium.common.exceptions.NoSuchElementException:
        pass

    driver.quit()