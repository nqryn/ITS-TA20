import time
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AlertTests(unittest.TestCase):

    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    BUTTON_SELECTORS = {
        "ALERT": (By.XPATH, "//ul/li[1]/button"),
        "CONFIRM": (By.XPATH, "//ul/li[2]/button"),  # //button[text()="Click for JS Confirm"]
        "PROMPT": (By.XPATH, "//ul/li[3]/button"),  # //button[@onclick="jsPrompt()"]
    }

    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_alert(self):
        self.driver.get(self.URL)
        time.sleep(3)
        alert_button = self.driver.find_element(*self.BUTTON_SELECTORS["ALERT"])
        alert_button.click()
        time.sleep(3)

        # Nu putem interactiona cu fereastra de alert in mod clasic (cu find element)
        # deoarece aceasta nu face parte din DOM (adica din pagina noastra web cu elemente)
        # ci este un element care apartine browserului

        # Folosim switch_to ca sa obtinem o referinta la un obiect de tipul Alert
        my_alert = self.driver.switch_to.alert

        # Acum avem 2 optiuni:
        # accept() - butonul de OK
        # dismiss() - butonul de Cancel
        my_alert.accept()
        time.sleep(3)

        result_p = self.driver.find_element("result")
        assert result_p.text == "You successfully clicked an alert"


    def test_prompt(self):
        self.driver.get(self.URL)
        prompt_button = self.driver.find_element(*self.BUTTON_SELECTORS["PROMPT"])
        prompt_button.click()

        prompt = self.driver.switch_to.alert
        prompt.send_keys("Salut!")
        prompt.accept()

        result = self.driver.find_element(By.ID, "result")

        assert result.text == "You entered: Salut!"


    def test_basic_auth(self):
        # Sintxa pentru a ne loga intr-o pagina cu Basic Authentication
        # (adica o ferestruica mica de la browser care cere user si parola)
        # este https://<username>:<parola>@<restul de url>
        url_no_auth = "https://the-internet.herokuapp.com/basic_auth"
        self.driver.get(url_no_auth)
        time.sleep(3)

        url_with_auth = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url_with_auth)
        time.sleep(3)
