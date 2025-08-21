Mumzworld App Automation
Setup Instructions
1. Install dependencies
pip install -r requirements.txt

2. Start Appium Server
appium -relaxed security

3. Run Tests
Run Behave:
Android
behave features/login.feature -D platform=android

4. Notes
Use real devices, Update the tests/config.py file with android and iOS capabilities. 

5. Install the mumzworld app from playstore
