import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

page_title = chrome.find_element(By.TAG_NAME, "h1")
print(page_title.text)

"""
Deoarece pot uneori exista mai multe elemente cu acelasi tag, 
metoda find_element il va gasi mereu DOAR pe primul.
"""
# input_elem = chrome.find_element(By.TAG_NAME, "input")
# input_elem.send_keys("Acesta este primul input gasit")
# time.sleep(2)

"""
Daca dorim sa luam toate inputurile, trebuie folosita metoda de plural (find_elements)
"""
input_elements = chrome.find_elements(By.TAG_NAME, "input")
input_elements[0].send_keys("First name here")
input_elements[1].send_keys("Last name here")
time.sleep(3)
