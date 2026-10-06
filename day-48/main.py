from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas

chrome_driver_path = r'C:\Desktop\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

#driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# time.sleep(5)
#
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
# print(f'price: {symbol.text}{price.text}')
#
# driver.quit()

#####################################################################################

driver.get('https://www.python.org/')

events = []
for x in range (1,6):
    event_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{x}]/a')
    event_date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{x}]/time')
    events.append([event_name.text, event_date.text])

upcoming_events = pandas.DataFrame(events, columns=['name','time']).to_dict('index')
print(upcoming_events)


