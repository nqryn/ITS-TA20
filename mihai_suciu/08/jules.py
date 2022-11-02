import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://jules.app/sign-in")
chrome.maximize_window()
time.sleep(1)

email_input = chrome.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
email_input.send_keys('alabala@portocala.ro')
time.sleep(1)

password_input = chrome.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
password_input.send_keys('S4mbur#')
time.sleep(1)

hidden_password_btt = chrome.find_element(By.CSS_SELECTOR,
                                          '#root > div > div.css-1kq6ix3 > form >'
                                          ' div > div:nth-child(2) > div > div >'
                                          ' div > svg > path')
hidden_password_btt.click()
time.sleep(1)

login_button = chrome.find_element(By.XPATH, '//*[text()="Log in"]')
login_button.click()
time.sleep(1)

forgot_password_btt = chrome.find_element(By.XPATH, '//*[text()="Forgot password?"]')
forgot_password_btt.click()
time.sleep(1)

sign_up_btt = chrome.find_element(By.XPATH, '//*[@href="/sign-up"]')
sign_up_btt.click()
time.sleep(1)

personal_radio_btt = chrome.find_element(By.XPATH, '//*[@value="personal"]')
personal_radio_btt.click()
time.sleep(1)

continue_button = chrome.find_element(By.XPATH, '//*[@data-test-id="select-account-continue-btn"]')
continue_button.click()
time.sleep(1)

first_name_input = chrome.find_element(By.XPATH, '//input[@placeholder="Type your answer here..."]')
first_name_input.send_keys('Croco')
first_name_input.send_keys(Keys.ENTER)
time.sleep(1)

last_name_input = chrome.find_element(By.XPATH, '//input[@placeholder="Type your answer here..."]')
last_name_input.send_keys('Tooth')
last_name_input.send_keys(Keys.ENTER)
time.sleep(1)

email_input = chrome.find_element(By.XPATH, '//input[@placeholder="Type your answer here..."]')
email_input.send_keys('Frodo_Tooth@swamp.red')
email_input.send_keys(Keys.ENTER)
time.sleep(1)

password_input = chrome.find_element(By.XPATH, '//input[@placeholder="Type your answer here..."]')
password_input.send_keys('Sw4mpPa22!')
password_input.send_keys(Keys.ENTER)
time.sleep(1)

password_confirmation = chrome.find_element(By.XPATH, '//input[@placeholder="Type your answer here..."]')
password_confirmation.send_keys('Sw4mpPa22!')
password_confirmation.send_keys(Keys.ENTER)
time.sleep(1)

# send_email_again_btt = chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/button/span[1]')
# send_email_again_btt.click()
# time.sleep(3)

chrome.quit()
