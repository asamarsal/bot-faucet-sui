# Bot faucet sui testnet

A Python-based automation tool for claiming SUI testnet tokens using Selenium WebDriver.

## Technology Stack
- Python
- Selenium WebDriver
- Chrome WebDriver
- python-dotenv

## Prerequisites
1. Python installed
2. Google Chrome browser installed
3. ChromeDriver matching your Chrome version
   - Check your version of chrome to download same version.
     `chrome://settings/help` put the link on chrome
   - Download from: https://chromedriver.chromium.org/downloads
   - Place in `D:\Chromedriver\chromedriver-win64\chromedriver.exe`
5. Required Python packages:
   - pip install selenium python-dotenv

## Run code
1. Open CLI/CMD
2. Navigate to folder that you want
3. Download this file, type `git clone https://github.com/asamarsal/bot-faucet-sui.git`
4. Type `python faucet_sui.py`
5. Input your sui wallet address
6. Your chrome will open automatically and get some faucet

## How It Works
- Loads/requests wallet address
- Initializes Chrome with custom settings
- Navigates to CroxyProxy
- Accesses the faucet through proxy
- Automatically fills wallet address
- Claims SUI tokens
- Check balance
- Repeats the process

## Technical Details
- Uses Selenium for browser automation
- Implements explicit waits for reliability
- Handles browser automation detection
- Manages Chrome profiles and sessions
- Includes error handling and recovery

## Notes
- Requires stable internet connection
- Chrome must be installed in default location
- ChromeDriver version must match Chrome browser version
