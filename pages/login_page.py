
from selenium.webdriver.common.by import By
from utils.platform import Platform
import time
from pages.base_page import BasePage

COUNTRY_SELECTION_PAGE_CONTINUE_BUTTON = {
    "android": (By.XPATH, "//*[contains(@content-desc,'Continue')]"),
    "ios": (By.XPATH, "//*[contains(@label,'Terms & conditions')] | //XCUIElementTypeButton[@name='tv_about_terms']")
}

ACCOUNT_TAB = {
    "android": (By.XPATH, "//*[contains(@text,'Account')]"),
    "ios": (By.XPATH, "//*[contains(@label,'Terms & conditions')] | //XCUIElementTypeButton[@name='tv_about_terms']")
}

SIGN_IN_BUTTON = {
    "android": (By.XPATH, "(//android.widget.TextView[@text='Sign In'])[2]"),
    "ios": (By.XPATH, "//*[contains(@label,'Terms & conditions')] | //XCUIElementTypeButton[@name='tv_about_terms']")
}

EMAIL_TEXTFIELD = {
    "android": (By.XPATH, "//android.widget.EditText[@text='Email']"),
    "ios": (By.XPATH, "//*[contains(@label,'Terms & conditions')] | //XCUIElementTypeButton[@name='tv_about_terms']")
}

PASSWORD_TEXTFIELD = {
    "android": (By.XPATH, "//android.widget.EditText[@text='Password']"),
    "ios": (By.XPATH, "//*[contains(@label,'Terms & conditions')] | //XCUIElementTypeButton[@name='tv_about_terms']")
}

SIGN_IN_WITH_VALID_CREDENTIALS = {
    "android": (By.XPATH, "//android.view.ViewGroup[@content-desc='auth-primary-action']"),
    "ios": (By.XPATH, "//*[contains(@label,'Terms & conditions')] | //XCUIElementTypeButton[@name='tv_about_terms']")
}

VERIFY_ACCOUNT_DETAILS = {
    "android": (By.XPATH, "//android.view.ViewGroup[@content-desc='TA, Test']"),
    "ios": (By.XPATH, "//*[contains(@label,'Terms & conditions')] | //XCUIElementTypeButton[@name='tv_about_terms']")
}

SIGN_OUT_BUTTON = {
    "android": (By.XPATH, "//android.widget.Button[@content-desc='Sign out']"),
    "ios": (By.XPATH, " ")
}

def click_on_continue_button_in_launch_screen(driver, platform):
    base = BasePage(driver)
    locator = COUNTRY_SELECTION_PAGE_CONTINUE_BUTTON[platform]

    if base.is_element_displayed(locator):
        driver.find_element(*locator).click()
        print("Continue button clicked")
        time.sleep(3.5)
    else:
        print("Continue button not found, moving to next step")


def click_on_Account_tab(driver, platform):
    locator = ACCOUNT_TAB[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)

def click_on_signin_button(driver, platform):
    locator = SIGN_IN_BUTTON[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)

def login_in_with_valid_credentials(driver, platform):
    base = BasePage(driver)
    locator = EMAIL_TEXTFIELD[platform]
    driver.find_element(*locator).send_keys("testanaithaanshad@yopmail.com")
    time.sleep(3.5)
    locator = PASSWORD_TEXTFIELD[platform]
    driver.find_element(*locator).send_keys("Test@123")
    time.sleep(3.5)
    locator = SIGN_IN_WITH_VALID_CREDENTIALS[platform]
    driver.find_element(*locator).click()
    time.sleep(3.5)
    verify_locator = VERIFY_ACCOUNT_DETAILS[platform]
    if base.is_element_displayed(verify_locator):
        print("Account details screen is displayed.")
        return True
    else:
        print("Account details screen NOT displayed.")
        return False

