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

6. Recorded video - https://github.com/anaithaanshad-qa/my-repo/commit/e7c5d09d8ddc6c532f14ea851325e6bc196bd075#diff-98bdd78bd38cb2d232cb9f0db6e9904432d98c0a1d11417268d9c2f3d04748a3
