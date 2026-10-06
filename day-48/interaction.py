from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r'C:\Desktop\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# num = driver.find_element(By.CSS_SELECTOR, '#mw-content-text li a')
# print(num.text)

driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
first_name.click()
first_name.send_keys('Eugenia')

last_name = driver.find_element(By.NAME, 'lName')
last_name.click()
last_name.send_keys('Frimpong')

email_address = driver.find_element(By.NAME, 'email')
email_address.click()
email_address.send_keys('eugeniafrimpong27@gmail.com')

signup_btn = driver.find_element(By.TAG_NAME, 'button')
signup_btn.click()
#signup_btn.send_keys(Keys.ENTER)

time.sleep(5)