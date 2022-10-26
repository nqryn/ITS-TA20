import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get('https://magento.softwaretestingboard.com/?ref=hackernoon.com')
chrome.maximize_window()
time.sleep(1)

sign_in_btt = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Sign In')
sign_in_btt.click()
time.sleep(1)

input_field = chrome.find_elements(By.CLASS_NAME, 'input-text')
input_field[1].send_keys('roni_cost@example.com')
input_field[2].send_keys('roni_cost3@example.com')
time.sleep(1)

sign_in_blue_btt = chrome.find_element(By.ID, 'send2')
sign_in_blue_btt.click()
time.sleep(3)
