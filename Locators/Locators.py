from selenium.webdriver.common.by import By


class Locators:
    USERNAME = (By.XPATH, '//input[@data-test="username"]')
    PASSWORD = (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BTN = (By.XPATH, '//input[@data-test="login-button"]')
    LOGIN_ERROR = (By.XPATH, '//div[@class="error-message-container error"]')
    ITEM = (By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name ']")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
    CART = (By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    ITEM_IN_CART = (By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']")
    REMOVE_ITEM = (By.CSS_SELECTOR, "button[data-test='remove-test.allthethings()-t-shirt-(red)']")
    REMOVED_ITEM = (By.CSS_SELECTOR, "div[class='removed_cart_item']")
    ITEM_IN_CATALOGUE = (By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name ']")
    BACK_TO_ITEM_CARD = (By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']")
    ITEM_IMAGE = (By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']")
    ITEM_LABEL = (By.CSS_SELECTOR, "div[class='inventory_item_label'] a[id='item_0_title_link']")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "button[data-test='checkout']")
    FIRST_NAME = (By.XPATH, '//input[@data-test="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@data-test="lastName"]')
    POSTAL_CODE = (By.XPATH, '//input[@data-test="postalCode"]')
    CONTINUE_BTN = (By.XPATH, '//input[@data-test="continue"]')
    FINISH_BTN = (By.XPATH, '//button[@name="finish"]')
    COMPLETE = (By.XPATH, '//h2[@class="complete-header"]')
    BURGER_MENU = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BTN = (By.CSS_SELECTOR, '#logout_sidebar_link')
    ABOUT_BTN = (By.ID, 'about_sidebar_link')
    AZ_OPTION = (By.XPATH, '//option[@value="az"]')
    ZA_OPTION = (By.XPATH, '//option[@value="za"]')
    LOHI_OPTION = (By.XPATH, '//option[@value="lohi"]')
    HILO_OPTION = (By.XPATH, '//option[@value="hilo"]')
    ITEMS = (By.XPATH, '//div[@class="inventory_item_label"]')
    ITEM_PRICES = (By.XPATH, '//div[@class="inventory_item_price"]')
    H1_ELEMENT = (By.XPATH, '//h1')
    START_TEST = (By.XPATH, "//button[text()='Начать тестирование']")
    LOGIN = (By.ID, 'login')
    PASS = (By.ID, 'password')
    CHECKBOX = (By.ID, 'agree')
    REGISTRATION = (By.ID, 'register')
    LOADER = (By.ID, 'loader')
    SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Вы успешно зарегистрированы!']")