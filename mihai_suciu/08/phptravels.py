import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://phptravels.com/demo/")
chrome.maximize_window()
time.sleep(1)

first_name_input = chrome.find_element(By.XPATH,"/html/body/div[3]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[1]")
first_name_input.send_keys("Green")
time.sleep(1)

last_name_input = chrome.find_element(By.XPATH,"html/body/div[3]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[2]")
last_name_input.send_keys("Forest")
time.sleep(1)

business_name_input = chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Business Name"]')
business_name_input.send_keys("Green Forest INC")
time.sleep(1)

email_input = chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Email"]')
email_input.send_keys("office@greenforest.inc")
time.sleep(1)

result_input = chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Result ?"]')
result_input.send_keys('55')
time.sleep(1)

submit_button = chrome.find_element(By.ID,"demo")
submit_button.click()
time.sleep(3)
