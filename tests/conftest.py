import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import tests.config as config


def create_driver(platform: str):
    if platform.lower() == "android":
        options = UiAutomator2Options().load_capabilities(config.android_config)
    else:
        options = XCUITestOptions().load_capabilities(config.ios_config)

    return webdriver.Remote(config.SERVER_URL, options=options)


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android")


@pytest.fixture(scope="function")
def driver(request):
    platform = request.config.getoption("--platform")
    driver = create_driver(platform)
    yield driver
    driver.quit()
