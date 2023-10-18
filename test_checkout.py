import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_checkout():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name ']").text
    time.sleep(2)

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
    button_add_to_cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    item_in_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']").text
    assert item == item_in_cart

    checkout_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='checkout']")
    checkout_button.click()

    first_name_field = driver.find_element(By.XPATH, '//input[@data-test="firstName"]')
    first_name_field.send_keys("Liza")

    last_name_field = driver.find_element(By.XPATH, '//input[@data-test="lastName"]')
    last_name_field.send_keys("Simpson")

    postal_code_field = driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    postal_code_field.send_keys("N2E 4L3")

    continue_button = driver.find_element(By.XPATH, '//input[@data-test="continue"]')
    continue_button.click()

    assert driver.find_element(By.XPATH, '//span[@class="title"]')
    time.sleep(2)

    finish_button = driver.find_element(By.XPATH, '//button[@name="finish"]')
    finish_button.click()
    time.sleep(2)

    assert driver.find_element(By.XPATH, '//h2[@class="complete-header"]')

    driver.quit()
