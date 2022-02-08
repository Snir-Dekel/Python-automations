import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.system("taskkill /F /IM chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://play.typeracer.com")
xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/div[1]/div/a'
enter_race = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(xpath)).click()
print('joined race')
time.sleep(3)
xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div'
my_text = str(WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(xpath)).text)
print(my_text)
xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input'
input_box = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, xpath)))
print("starts typing")
for x in my_text:
    input_box.send_keys(x)
    time.sleep(0.003)
