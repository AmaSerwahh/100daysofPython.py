from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = r'C:\Desktop\chromedriver-win64\chromedriver.exe'

class InternetSpeedBot:

    def __init__(self, chrome_driver_path):
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]')
        go.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet(self):
        internet_provider = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]').text
        print(f'Hey {internet_provider}, why is my internet speed {self.down}/{self.up} down/upload mbps when I pay for {PROMISED_DOWN}/{PROMISED_UP} down/upload mbps?')

bot = InternetSpeedBot(CHROME_DRIVER_PATH)
bot.get_speed()
bot.tweet()



