from selenium.webdriver.common.by import By
from utils.platform import Platform
import time
from pages.base_page import BasePage


EXPLORE_BUTTON = {
    "android": (By.XPATH, "//android.view.View[@content-desc='Explore']"),
    "ios": (By.XPATH, " ")
}

SERACH_ICON = {
    "android": (By.XPATH, "//*[contains(@resource-id,'phosphor-react-native-magnifying-glass-bold')]"),
    "ios": (By.XPATH, " ")
}

SERACH_ICON_TEXTFIELD = {
    "android": (By.XPATH, "//android.widget.EditText[@text='Search Mumzworld']"),
    "ios": (By.XPATH, " ")
}

FIRST_SERACH_RESULT = {
    "android": (By.XPATH, "//*[contains(@content-desc,'diapers')][1]"),
    "ios": (By.XPATH, " ")
}

FIRST_PRODUCT_IN_MPP = {
    "android": (By.XPATH, "//*[contains(@content-desc,'Diapers')]/android.view.ViewGroup[1]"),
    "ios": (By.XPATH, " ")
}

ADD_TO_CART_BUTTON = {
    "android": (By.XPATH, "//android.widget.TextView[@text='Add to Cart']"),
    "ios": (By.XPATH, " ")
}

VIEW_CART_BUTTON = {
    "android": (By.XPATH, "//android.widget.Button[@content-desc='View cart']"),
    "ios": (By.XPATH, " ")
}

PRODUCT_IN_CART = {
    "android": (By.XPATH, "//*[contains(@text,'Diapers')]"),
    "ios": (By.XPATH, " ")
}


def click_on_explore_tab(driver, platform):
    locator = EXPLORE_BUTTON[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)

def click_on_search(driver, platform):
    locator = SERACH_ICON[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)
    locator = SERACH_ICON_TEXTFIELD[platform]
    driver.find_element(*locator).send_keys("DIAPER")
    time.sleep(3.5)
    locator = FIRST_SERACH_RESULT[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)


def go_to_pdp_page(driver, platform):
    locator = FIRST_PRODUCT_IN_MPP[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)

def add_to_cart(driver, platform):
    locator = ADD_TO_CART_BUTTON[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)
    locator = VIEW_CART_BUTTON[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)

def verify_product_in_cart(driver, platform):
    base = BasePage(driver)
    verify_locator = PRODUCT_IN_CART[platform]
    if base.is_element_displayed(verify_locator):
        print("product is displayed.")
        return True
    else:
        print("cart is empty")
        return False
