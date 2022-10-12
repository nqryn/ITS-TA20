"""
Css selector ne permite sa folosim celelalte tipuri de selectori, dupa cum urmeaza:
 - nume tag -> il folosim fix asa cum este
 - id element -> punem # in fata (#first-name)
 - clasa element -> punem . in fata
 - alte atribute pe element -> punem [nume_atribut="valoare"]

Putem inclusiv cauta dupa structura din html, pornind de unde vrem noi,
si mergand doar in jos sau in lateral.

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

# Cautam un tag de tip <div>, care are clasa (.) numita "form-group"
form_group = chrome.find_element(By.CSS_SELECTOR, "div.form-group")
# Cautam in tree-ul format de elementul gasit mai sus (adica nu in tot html-ul, ci doar intr-o parte)
# Cautam un copil div, mai exact primul copil, iar apoi in acest div cautam un copil "input"
first_name1 = form_group.find_element(By.CSS_SELECTOR, "div:nth-child(1) input")
# Aici cautarea se face pornind de la root, si se merge in jos pe copii, pana ajungem la inputul de first name.
first_name2 = form_group.find_element(By.CSS_SELECTOR, "body > div > form > div > div:nth-child(1) > input")
assert first_name2 == first_name1
