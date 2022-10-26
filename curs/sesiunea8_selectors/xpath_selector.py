"""
XPath este foarte util atunci cand elementul cautat nu are id sau clasa/tag unic,
si trebuie sa il luam raportandu-ne la alte elemente.
Dupa ce gasim un alt element apropiat in mod unicat, putem face parcurgere catre
elementul care ne intereseaza.

// - descendenti
/ - copii
parent - cautare in sus
siblings - in lateral
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

# // - porneste de la radacina (html) si cauta peste tot
# * - orice tip de tag
# [@ceva="valoare"] - selecteaza doar tagurile care au atributul "ceva" egal cu "valoare"
xpath_first_name = '//*[@id="first-name"]'

# / - doar copiii directi (spre deosebire de //, unde se cauta in toti descendentii)
# daca punem 0 ca si index atunci cand avem mai multi copii de acelasi tip, va da eroare
full_xpath_first_name = '/html/body/div/form/div/div[1]/input'

full_xpath_last_name = '/html/body/div/form/div/div[2]/input'

first_name_possible_xpaths = [
    '//input[@placeholder="Enter first name"]',
    '//*[@id="first-name"]',
    '/html/body/div/form/div/div[1]/input',
    '//div[@class="form-group"]/div[1]/input'
]

# Putem avea si functia text() in loc de numele atribului dupa care cautam
# /*[text()="text cautat"]
submit_button_xpath = '//a[text()="Submit"]'
# Putem folosi si functia contains pentru text partial (dar elementul cautat
# trebuie sa contina doar text)
title_xpath = '//h1[contains(text(),"Complete")]'

# cu | putem face OR (sau) intre mai multi selectori
# Primul gasit de sus in jos in DOM
any_text_input_selector = '//*[@id="last-name"] | //*[@id="first-name"] | //*[@id="job-title"]'
elem = chrome.find_element(By.XPATH, any_text_input_selector)
elem.send_keys("Testam XPAth")
time.sleep(2)
