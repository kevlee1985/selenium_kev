from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_scrape_bitcoin_price():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.set_window_size(1024, 600)
    driver.maximize_window()

    try:
        # Open the website with Bitcoin price
        driver.get("https://www.coindesk.com/price/bitcoin/")

        # Find the element containing the Bitcoin price (adjust this based on the actual structure of the website)
        bitcoin_price_element = driver.find_element(By.XPATH,
                                                    "//body/div[@id='fusion-app']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[2]")

        # Get the Bitcoin price
        bitcoin_price = bitcoin_price_element.text

        # Print the Bitcoin price (you may want to save it to a file or database)
        print("Bitcoin Price:", bitcoin_price)

        # Save the data to a CSV file (append mode)
        with open('c:/git/selenium_kev/bitcoin_prices.csv', mode='a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.strftime("%m-%d %H:%M"), bitcoin_price])

    finally:
        # Close the browser window
        driver.quit()


def test_scrape_ethereum_price():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.set_window_size(1024, 600)
    driver.maximize_window()

    try:
        # Open the website with Bitcoin price
        driver.get("https://www.coindesk.com/price/ethereum/")

        # Find the element containing the Bitcoin price (adjust this based on the actual structure of the website)
        ethereum_price_element = driver.find_element(By.XPATH,
                                                    "//body/div[@id='fusion-app']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[2]")

        # Get the Bitcoin price
        ethereum_price = ethereum_price_element.text

        # Print the Bitcoin price (you may want to save it to a file or database)
        print("Ethereum Price:", ethereum_price)

        # Save the data to a CSV file (append mode)
        with open('c:/git/selenium_kev/ethereum_prices.csv', mode='a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.strftime("%m-%d %H:%M"), ethereum_price])

    finally:
        # Close the browser window
        driver.quit()
