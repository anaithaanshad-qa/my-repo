Mumzworld App Automation
Setup Instructions
1. Install dependencies
pip install -r requirements.txt
2. Start Appium Server
appium
3. Run Tests
Android
pytest --platform=android
iOS
pytest --platform=ios
Or run Behave:

python runner.py
4. Notes
Replace login credentials in login_steps.py before running tests.
Use adb / Xcode simulators for devices.
Record test execution using screen recorder or adb screenrecord.