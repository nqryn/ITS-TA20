# Implementează o clasă Login care să moștenească unittest.TestCase
# Gasește elementele în partea de sus folosind ce selectors dorești:
# - setUp()
# - Driver
# https://the-internet.herokuapp.com/
# Click pe Form Authentication
# tearDown()
# Quit browser

import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class HerokuappLoginTestCase(unittest.TestCase):

    def setUp(self) -> None:
        service = ChromeService(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=service)
        self.chrome.implicitly_wait(10)
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()
        time.sleep(3)
        form_authentication = self.chrome.find_element(By.XPATH, '//*[text()="Form Authentication"]')
        form_authentication.click()

    def tearDown(self) -> None:
        self.chrome.quit()

# ● Test 1
# - Verifică dacă noul url e corect
    def test_1(self):
        assert self.chrome.current_url == "https://the-internet.herokuapp.com/login"
        time.sleep(3)

# ● Test 2
# - Verifică dacă page title e corect
    def test_2(self):
        page_title = self.chrome.find_element(By.XPATH, '//h2[contains(text(),"Login Page")]')
        assert page_title.text == 'Login Page'

# ● Test 3
# - Verifică textul de pe elementul xpath=//h2 e corect
    def test_3(self):
        self.chrome.get('https://the-internet.herokuapp.com/')
        h2_elem = self.chrome.find_element(By.TAG_NAME, 'h2')
        assert h2_elem.text == "Available Examples"

# ● Test 4
# - Verifică dacă butonul de login este displayed
    def test_4(self):
        login_button = self.chrome.find_element(By.XPATH, '//*[@class="fa fa-2x fa-sign-in"]')
        assert login_button.is_displayed()

# ● Test 5
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_5(self):
        elemental_selenium = self.chrome.find_element(By.XPATH, '//*[text()="Elemental Selenium"]')
        href_attribute = elemental_selenium.get_attribute('href')
        assert href_attribute == "http://elementalselenium.com/"

# ● Test 6
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed
    def test_6(self):
        login_with_blank = self.chrome.find_element(By.XPATH, '//*[@class="fa fa-2x fa-sign-in"]')
        login_with_blank.click()
        login_blank_error = self.chrome.find_element(By.XPATH, '//div[@class="flash error"]')
        assert login_blank_error.is_displayed()

# ● Test 7
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is
# incorrect')
#     def test_7(self):
#         self.chrome.get('https://the-internet.herokuapp.com/login')
#         username_input = self.chrome.find_element(By.ID, "username")
#         username_input.send_keys("jgjhgkb")
#         password_input = self.chrome.find_element(By.ID, "password")
#         password_input.send_keys("jgdydtc")
#         login_invalid = self.chrome.find_element(By.XPATH, "//button[@type=submit']")
#         login_invalid.click()

# ● Test 8
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut

# ● Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi

# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    def test_10(self):
        username_input = self.chrome.find_element(By.ID, "username")
        username_input.send_keys("tomsmith")
        password_input = self.chrome.find_element(By.ID, "password")
        password_input.send_keys("SuperSecretPassword!")
        login_valid = self.chrome.find_element(By.XPATH, "//button[@type=submit']")
        login_valid.click()
        assert '/secure' in self.chrome.current_url

# ● Test 11
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login