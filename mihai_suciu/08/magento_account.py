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

create_account_btt = chrome.find_element(By.LINK_TEXT, 'Create an Account')
create_account_btt.click()
time.sleep(1)

first_name_input = chrome.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[1]/div/input')
first_name_input.send_keys('Yellow')
time.sleep(1)

last_name_input = chrome.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[2]/div/input')
last_name_input.send_keys('Frog')
time.sleep(1)

sign_up_for_newsletter_ckbox = chrome.find_element(By.ID, 'is_subscribed')
flag = sign_up_for_newsletter_ckbox.is_selected()
print(flag)
if not flag:
    sign_up_for_newsletter_ckbox.click()
time.sleep(1)

email_field = chrome.find_element(By.ID, 'email_address')
email_field.send_keys('dizzy_frog@blackswamp.nfo')
time.sleep(1)

password_field = chrome.find_element(By.ID, 'password')
password_field.send_keys('Fr0gsH34vEn')
time.sleep(1)

password_confirm_field = chrome.find_element(By.ID, 'password-confirmation')
password_confirm_field.send_keys('Fr0gsH34vEn')
time.sleep(1)

create_blue_btt = chrome.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button/span')
create_blue_btt.click()
time.sleep(1)

