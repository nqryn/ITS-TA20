"""
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri

- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

firstname = chrome.find_element(By.ID,"first-name")
firstname.send_keys("Florin")
time.sleep(1)

lastname = chrome.find_element(By.ID,"last-name")
lastname.send_keys("Chetves")
time.sleep(1)

job_title = chrome.find_element(By.ID,"job-title")
job_title.send_keys("Inginer")
time.sleep(1)


form_link = chrome.find_element(By.LINK_TEXT,"Form")
form_link.click()
assert chrome.current_url== "https://formy-project.herokuapp.com/form"
time.sleep(1)

components_link = chrome.find_element(By.ID,"navbarDropdownMenuLink")
components_link.click()
time.sleep(1)

radio_partial_link= chrome.find_element(By.PARTIAL_LINK_TEXT,"Radio")
radio_partial_link.click()
time.sleep(1)

navbar_class= chrome.find_element(By.CLASS_NAME,"navbar-brand")
navbar_class.click()
time.sleep(1)




chrome.get("http://www.seleniumframework.com/about-2/")
time.sleep(2)
name_input = chrome.find_element(By.NAME,"name")
name_input.send_keys("Ionel")
time.sleep(2)


