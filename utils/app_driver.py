from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import tests.config as config


def launch_installed_app(platform: str = "android"):
    """
    Launch an already installed app on Android or iOS.

    Args:
        platform (str): "android" or "ios"

    Returns:
        WebDriver instance
    """
    platform = platform.lower()

    if platform == "android":
        options = UiAutomator2Options().load_capabilities(config.android_config)
    elif platform == "ios":
        options = XCUITestOptions().load_capabilities(config.ios_config)
    else:
        raise ValueError(f"Unsupported platform: {platform}")

    driver = webdriver.Remote(config.SERVER_URL, options=options)
    return driver

# from appium import webdriver
# from appium.options.android import UiAutomator2Options
#
# def launch_installed_app_android():
#     options = UiAutomator2Options().load_capabilities({
#         "platformName": "Android",
#         "deviceName": "Android Device",   # replace with your actual device name
#         "appPackage": "com.example.yourapp",  # replace with your app's package
#         "appActivity": "com.example.yourapp.MainActivity",  # replace with main activity
#         "noReset": True,
#         "automationName": "UiAutomator2"
#     })
#
#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#     return driver
