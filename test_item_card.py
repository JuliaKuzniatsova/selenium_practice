import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_click_on_item_image():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_image = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']")
    item_image.click()

    assert driver.find_element(By.CSS_SELECTOR, "div[id='inventory_item_container']")
    time.sleep(2)

    driver.quit()


def test_click_on_item_name():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_label = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_item_label'] a[id='item_0_title_link']")
    item_label.click()

    assert driver.find_element(By.CSS_SELECTOR, "div[id='inventory_item_container']")
    time.sleep(2)

    driver.quit()

