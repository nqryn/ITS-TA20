import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.maximize_window()
time.sleep(1)

accept_cookies_window = chrome.find_element(By.XPATH, '//button[@id="ez-accept-all"]')
accept_cookies_window.click()

first_name_input = chrome.find_element(By.XPATH, '//input[@name="firstname"]')
first_name_input.send_keys('Goldy')
time.sleep(1)

last_name_input = chrome.find_element(By.XPATH, '//input[@name="lastname"]')
last_name_input.send_keys('Locks')
time.sleep(1)

gender_male_button = chrome.find_element(By.XPATH, '//input[@value="Male"]')
gender_male_button.click()
time.sleep(1)

gender_female_button = chrome.find_element(By.XPATH, '//input[@value="Female"]')
gender_female_button.click()
time.sleep(1)

years_of_experience_btt = chrome.find_element(By.XPATH, '//input[@value="1"] |'
                                                        ' //input[@value="2"] |'
                                                        ' //input[@value="3"] |'
                                                        ' //input[@value="4"] |'
                                                        ' //input[@value="5"] |'
                                                        ' //input[@value="6"] |'
                                                        ' //input[@value="7"]')
years_of_experience_btt.click()
time.sleep(1)

cookies_banner = chrome.find_element(By.ID, 'cookieChoiceDismiss')
cookies_banner.click()

date_field = chrome.find_element(By.XPATH, '//*[@id="datepicker"]')
date_field.send_keys('31.10.2022')
time.sleep(1)

manual_tester_button = chrome.find_element(By.XPATH, '//*[@id="profession-0"]')
manual_tester_button.click()
time.sleep(1)
manual_tester_button.click()
automation_tester_button = chrome.find_element(By.XPATH, '//*[@id="profession-1"]')
automation_tester_button.click()
time.sleep(1)

automation_tools_selenium = chrome.find_element(By.XPATH, '//input[@name="tool"][3]')
automation_tools_selenium.click()
time.sleep(1)

continent_selection = chrome.find_element(By.XPATH, '//select[@name="continents"]/option[. = "Europe"]')
continent_selection.click()
time.sleep(1)

dropdown = chrome.find_element(By.XPATH, '//select[@id="selenium_commands"]')
dropdown.find_element(By.XPATH,'//option[. = "WebElement Commands"]').click()
time.sleep(5)

chrome.quit()