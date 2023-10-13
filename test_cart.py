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

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']").text
    print(item)

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
    button_add_to_cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    item_in_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']").text
    assert item == item_in_cart
