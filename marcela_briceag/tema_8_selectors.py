import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

# chrome.get("http://automationpractice.com/index.php")
# time.sleep(2)
# # ID selector 1
# search_input = chrome.find_element(by=By.ID, value="search_query_top")
# search_input.send_keys("dresses")
# time.sleep(2)
#
# # ID selector 2
# email_input = chrome.find_element(By.ID, "newsletter-input")
# email_input.send_keys("marcela@gmail.com")
# time.sleep(2)
#
# # Link text 1
# chrome.get("https://the-internet.herokuapp.com/")
# dynamic_content_link = chrome.find_element(By.LINK_TEXT, "Dynamic Content")
# dynamic_content_link.click()
# time.sleep(2)

# # Partial link text 1
# chrome.get("https://the-internet.herokuapp.com/")
# multiple_windows_link = chrome.find_element(By.PARTIAL_LINK_TEXT, "Multiple")
# multiple_windows_link.click()
# time.sleep(2)
#
# # Link text 2
# chrome.get("https://formy-project.herokuapp.com/")
# file_upload_link = chrome.find_element(By.LINK_TEXT, "File Upload")
# file_upload_link.click()
# time.sleep(2)
#
# # Partial link text 2
# chrome.get("https://formy-project.herokuapp.com/")
# enabled_and_disabled_elements_link = chrome.find_element(By.PARTIAL_LINK_TEXT, "Enabled")
# enabled_and_disabled_elements_link.click()
# time.sleep(2)

# # Tag_name 1
# chrome.get("https://phptravels.net/")
# time.sleep(2)
# book_next_trip_title = chrome.find_element(By.TAG_NAME, "h2")
# print(book_next_trip_title.text)
# # tag_name2
# chrome.get("https://phptravels.net/")
# time.sleep(2)
# choose_best_deals = chrome.find_element(By.TAG_NAME, "p")
# print(choose_best_deals.text)

# class-name 1
chrome.get("http://automationpractice.com/index.php")
time.sleep(2)
flights_link = chrome.find_element(By.CLASS_NAME, "shopping_cart")
flights_link.click()
time.sleep(2)


