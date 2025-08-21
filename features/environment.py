from utils.app_driver import launch_installed_app

def before_all(context):
    platform = context.config.userdata.get("platform", "android").lower()
    context.driver = launch_installed_app(platform)
    context.driver.implicitly_wait(10)

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()



# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.options.ios import XCUITestOptions
# import tests.config as config
#
#
# def before_all(context):
#     platform = context.config.userdata.get("platform", "android").lower()
#
#     if platform == "android":
#         options = UiAutomator2Options().load_capabilities(config.android_config)
#     else:
#         options = XCUITestOptions().load_capabilities(config.ios_config)
#
#     context.driver = webdriver.Remote(config.SERVER_URL, options=options)
#
#
# def after_all(context):
#     if hasattr(context, "driver"):
#         context.driver.quit()
