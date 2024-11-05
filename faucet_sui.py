from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import requests

def load_display():
    try:
        with open('exluminate.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Welcome to Sui Faucet Generator!"

def check_env_file():

    print(load_display())

    env_path = '.env'
    if os.path.exists(env_path):
        print("Found existing wallet configuration")
        load_dotenv()
        wallet_address = os.getenv('WALLET_ADDRESS')
        if wallet_address:
            print(f"Loaded wallet address: {wallet_address}")
            return wallet_address
    
    wallet_address = input("Please enter your sui wallet address : ")
    
    # Write to .env file
    with open(env_path, 'w') as env_file:
        env_file.write(f'WALLET_ADDRESS={wallet_address}')
    
    # Reload environment variables
    load_dotenv()
    return wallet_address

def initialize_chrome():
    service = Service('D:\\Chromedriver\\chromedriver-win64\\chromedriver.exe')
    options = Options()
    
    # Basic settings
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--incognito")
    
    # Remove automation flags
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Set Chrome binary location
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    
    return webdriver.Chrome(service=service, options=options)

def connect_to_croxyproxy(driver, wallet_address):
    while True:
        try:
            print("\nOpening Proxy")
            driver.get("https://croxyproxy.com/")

            wait = WebDriverWait(driver, 10)
            input_field = wait.until(EC.presence_of_element_located((By.ID, "url")))
            input_field.send_keys("faucet.blockbolt.io")
            print("Entered URL: faucet.blockbolt.io")

            go_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Go')]")))
            go_button.click()
            print("Go button clicked")

            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("Waiting 10 seconds for Proxy to fully load...")
            time.sleep(10)
            
            wallet_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='sui_address' and @class='borderBottom']")))
            wallet_input.clear()
            wallet_input.send_keys(wallet_address)
            print(f"Entered wallet address: {wallet_address}")

            give_sui_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Give me sui!')]")))
            give_sui_button.click()
            print("Give me SUI! button clicked")
            print("Your wallet just get 1 sui testnet")
            time.sleep(5)
            
            # Check balance directly in CMD
            check_balance(wallet_address)
            
            time.sleep(5)

        except Exception as e:
            print(f"Operation error: {e}")
            break
            
def check_balance(wallet_address):
    try:
        print("\nChecking wallet balance...")
        # Using official Sui testnet RPC endpoint
        api_url = "https://fullnode.testnet.sui.io:443"
        
        # Prepare the JSON-RPC request
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "suix_getBalance",
            "params": [wallet_address, "0x2::sui::SUI"]
        }
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(api_url, json=payload, headers=headers)
        balance_data = response.json()
        
        if 'result' in balance_data:
            balance = int(balance_data['result']['totalBalance']) / 1000000000  # Convert from MIST to SUI
            print(f"Current balance: {balance} SUI")
            return balance
        else:
            print("Could not fetch balance data")
            return None
            
    except Exception as e:
        print(f"Error checking balance: {e}")
        return None



def main():
    # Check and setup wallet address
    wallet_address = check_env_file()
    print(f"Using wallet address: {wallet_address}")
    
    # Initialize Chrome after wallet setup
    driver = initialize_chrome()
    
    # Connect to proxy and perform faucet operations
    connect_to_croxyproxy(driver, wallet_address)
    
    while True:
        pass

if __name__ == "__main__":
    main()
