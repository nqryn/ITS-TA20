import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert


class SeleniumEasyTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://demo.seleniumeasy.com/")

    def test_basic_form(self):
        click_input_forms = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/ul/li/ul/li[1]/a")
        click_input_forms.click()
        click_simple_form = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/ul/li/ul/li[1]/ul/li[1]/a")
        click_simple_form.click()
        select_enter_message = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[2]/form/div/input")
        select_enter_message.send_keys("Hello World!")
        click_show_message = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button")
        click_show_message.click()
        message_box = self.driver.find_element(By.ID, "display")
        assert message_box.text == "Hello World!"

    def test_form_two_input_fields(self):
        click_input_forms_2 = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/ul/li/ul/li[1]/a")
        click_input_forms_2.click()
        click_simple_form_2 = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/ul/li/ul/li[1]/ul/li[1]/a")
        click_simple_form_2.click()
        click_input_field_1 = self.driver.find_element(By.ID, "sum1")
        click_input_field_1.send_keys("5")
        click_input_field_2 = self.driver.find_element(By.ID, "sum2")
        click_input_field_2.send_keys("3")
        click_get_total_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button")
        click_get_total_button.click()
        sum_total = self.driver.find_element(By.ID, "displayvalue")
        assert sum_total.text == "8"

    def test_basic_checkbox(self):
        click_input_forms_3 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/a")
        click_input_forms_3.click()
        click_checkbox_demo = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/ul/li[2]/a")
        click_checkbox_demo.click()
        click_on_checkbox = self.driver.find_element(By.ID, "isAgeSelected")
        click_on_checkbox.click()
        success_message = self.driver.find_element(By.ID, "txtAge")
        assert success_message.text == "Success - Check box is checked"

    def test_radio_button(self):
        click_input_forms_4 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/a")
        click_input_forms_4.click()
        click_radio_buttons = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/ul/li[3]/a")
        click_radio_buttons.click()
        click_male_radiobutton = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[2]/label[1]/input")
        click_male_radiobutton.click()
        click_get_value = self.driver.find_element(By.ID, "buttoncheck")
        click_get_value.click()
        check_message = self.driver.find_element(By.CLASS_NAME, "radiobutton")
        assert check_message.text == "Radio button 'Male' is checked"

    def test_ajax_form_submit(self):
        click_input_forms_4 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/a")
        click_input_forms_4.click()
        click_ajax_form_submit = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[1]/li[1]/ul/li[6]/a")
        click_ajax_form_submit.click()
        insert_name = self.driver.find_element(By.ID, "title")
        insert_name.send_keys("James Bond")
        insert_comment = self.driver.find_element(By.ID, "description")
        insert_comment.send_keys("Hello World!")
        click_submit_button = self.driver.find_element(By.ID, "btn-submit")
        click_submit_button.click()
        time.sleep(2)
        check_submit = self.driver.find_element(By.ID, "submit-control")
        assert check_submit.text == "Form submited Successfully!"

    def test_alert_box(self):
        click_alerts_modals = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li[2]/a")
        click_alerts_modals.click()
        click_javascript_alerts = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li[2]/ul/li[5]/a")
        click_javascript_alerts.click()
        conform_box_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/button")
        conform_box_button.click()
        Alert(self.driver).accept()
        check_popup_message = self.driver.find_element(By.ID, "confirm-demo")
        assert check_popup_message.text == "You pressed OK!"

    @classmethod
    def tearDown(self):
        self.driver.quit()