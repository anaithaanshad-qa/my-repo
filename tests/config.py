import os

SERVER_URL = "http://127.0.0.1:4723"
DEFAULT_DRIVER_WAIT_TIME = 10

APPS_FOLDER = "apps"
APK_PATH = os.path.join(os.getcwd(), APPS_FOLDER, "mumzworld.apk")
IPA_PATH = os.path.join(os.getcwd(), APPS_FOLDER, "mumzworld.ipa")

android_config = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "RZ8M123456X",  # <-- replace with your adb device name
    "appPackage": "com.mumzworld.android",
    "appActivity": "com.mumzworld.android.MainActivity",
     "noReset": False,
     "fullReset": False,
    "newCommandTimeout": 240
}

ios_config = {
    "platformName": "iOS",
    "automationName": "XCUITest",
    "deviceName": "iPhone 14",
    "platformVersion": "16.0",
    "bundleId": "com.mumzworld.ios",
    "noReset": True,
    "newCommandTimeout": 240
}
