import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("http://www.seleniumframework.com/practiceform/")
chrome.maximize_window()
time.sleep(1)

email_input = chrome.find_element(By.NAME, "email")
email_input.send_keys("Ceva text")
time.sleep(2)
