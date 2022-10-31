import unittest
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class HerokuAuthenticationTestCase(unittest.TestCase):

    def setUp(self) -> None:
        service = ChromeService(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=service)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.maximize_window()

    """
    Test 1
    - Verifică dacă noul url e corect
    """

    def test_form_authentication_button(self):
        self.form_authentication_btt = self.chrome.find_element(By.XPATH, '//*[text()="Form Authentication"]')
        self.form_authentication_btt.click()
        assert self.chrome.current_url == "https://the-internet.herokuapp.com/login", "form_authentication_button error"
        time.sleep(3)

    def tearDown(self) -> None:
        self.chrome.quit()


class HerokuFormAuthenticationPageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        service = ChromeService(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=service)
        self.chrome.get("https://the-internet.herokuapp.com/login")

    """
    Test 2
    - Verifică dacă page title e corect
    """

    def test_login_page_title_1(self):
        title1 = self.chrome.find_element(By.TAG_NAME, 'h2')
        self.assertEqual(title1.text, "Login Page")

    """
    Test 3
    - Verifică textul de pe elementul xpath=//h2 e corect
    """

    def test_login_page_title_2(self):
        title2 = self.chrome.find_element(By.XPATH, '//h2')
        self.assertEqual(title2.text, "Login Page")

    """
    Test 4
    - Verifică dacă butonul de login este displayed
    """

    def test_login_button_displayed(self):
        login_button = self.chrome.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
        assert login_button.is_displayed(), "login button not displayed error"

    """
    Test 5
    - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    """

    def test_elemental_selenium_href(self):
        elemental_selenium_button = self.chrome.find_element(By.XPATH, '//a[@href="http://elementalselenium.com/"]')
        href_attribute = elemental_selenium_button.get_attribute('href')
        assert href_attribute == "http://elementalselenium.com/", "elemental selenium href error"

    """
    Test 6
    - Lasă goale user și pass
    - Click login
    - Verifică dacă eroarea e displayed
    """

    def test_login_error(self):
        login_button = self.chrome.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
        login_button.click()
        login_error_msg = self.chrome.find_element(By.XPATH, '//div[@id="flash"]')
        assert login_error_msg.is_displayed(), "login error message error"

    """
    Test 7
    - Completează cu user și pass invalide
    - Click login
    - Verifică dacă mesajul de pe eroare e corect
    - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    expected = 'Your username is invalid!'
    self.assertTrue(expected in actual, 'Error message text is
    incorrect')
    """

    def test_invalid_user_and_pass_message_on(self):
        user_input = self.chrome.find_element(By.XPATH, '//input[@name="username"]')
        user_input.send_keys('red_cat')
        pass_input = self.chrome.find_element(By.XPATH, '//input[@name="password"]')
        pass_input.send_keys('G4arden!ng')
        login_button = self.chrome.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
        login_button.click()
        login_error_msg = self.chrome.find_element(By.XPATH, '//div[@id="flash"]').text
        # self.assertEqual(login_error_msg.text, "Your username is invalid!\n×")
        expected = 'Your username is invalid!'
        self.assertTrue(expected in login_error_msg, 'Error message text is incorrect')

    """
    Test 8
    - Lasă goale user și pass
    - Click login
    - Apasă x la eroare
    - Verifică dacă eroarea a dispărut
    """

    def test_invalid_user_and_pass_message_off(self):
        self.chrome.maximize_window()
        login_button = self.chrome.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
        login_button.click()
        error_x_button = self.chrome.find_element(By.XPATH, '//a[@class="close"]')
        error_x_button.click()
        try:
            login_error_msg = self.chrome.find_element(By.XPATH, '//div[@id="flash"]')
        except:
            NoSuchElementException
        finally:
            print('Test8: element not displayed')


    """
    Test 9
    - Ia ca o listă toate //label
    - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
    Password)
    - Aici e ok să avem 2 asserturi
    """

    def test_labels(self):
        labels = self.chrome.find_elements(By.TAG_NAME, 'label')
        self.assertEqual(labels[0].text, "Username")
        self.assertEqual(labels[1].text, "Password")

    """
    Test 10
    - Completează cu user și pass valide
    - Click login
    - Verifică ca noul url CONTINE /secure
    - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    """

    def test_good_user_pass_login(self):
        user_input = self.chrome.find_element(By.XPATH, '//input[@name="username"]')
        user_input.send_keys('tomsmith')
        pass_input = self.chrome.find_element(By.XPATH, '//input[@name="password"]')
        pass_input.send_keys('SuperSecretPassword!')
        login_button = self.chrome.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
        login_button.click()
        new_url = self.chrome.current_url
        assert '/secure' in new_url, '"/secure" is not contained in the new url! Error!'
        flash_success_element = WebDriverWait(self.chrome, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="flash success"]'))
        )
        assert flash_success_element.is_displayed(), '"flash success" element display error'
        self.assertIn("secure area!", flash_success_element.text)

    """
    Test 11
    - Completează cu user și pass valide
    - Click login
    - Click logout
    - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    """

    def test_login_logout(self):
        user_input = self.chrome.find_element(By.XPATH, '//input[@name="username"]')
        user_input.send_keys('tomsmith')
        pass_input = self.chrome.find_element(By.XPATH, '//input[@name="password"]')
        pass_input.send_keys('SuperSecretPassword!')
        login_button = self.chrome.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
        login_button.click()
        logout_button = self.chrome.find_element(By.XPATH, '//*[text()=" Logout"]')
        logout_button.click()
        assert self.chrome.current_url == "https://the-internet.herokuapp.com/login"

    """
    Test 12 - brute force password hacking
    - Completează user tomsmith
    - Găsește elementul //h4
    - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
    potențială parolă.
    - Folosește o structură iterativă prin care să introduci rând pe rând
    parolele și să apeși pe login.
    - La final testul trebuie să îmi printeze fie
    ‘Nu am reușit să găsesc parola’
    ‘Parola secretă este [parola]’
    """
    def test_brute_force_pass_hack(self):
        h4_text_elements_list = self.chrome.find_elements(By.XPATH, '//h4/*')
        possible_password_list = []
        for element in h4_text_elements_list:
            possible_password_list.append(element.text)
        for item in possible_password_list:
            user_input = self.chrome.find_element(By.XPATH, '//input[@name="username"]')
            user_input.send_keys('tomsmith')
            pass_input = self.chrome.find_element(By.XPATH, '//input[@name="password"]')
            pass_input.clear()
            pass_input.send_keys(item)
            login_button = self.chrome.find_element(By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]')
            login_button.click()
            if self.chrome.current_url == 'https://the-internet.herokuapp.com/secure':
                secret_password = item
        if self.chrome.current_url == 'https://the-internet.herokuapp.com/secure':
            print(f'I found the secret password: {secret_password}')
        else:
            print("I didn't find the secret password")

    def tearDown(self) -> None:
        self.chrome.quit()