import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get('https://magento.softwaretestingboard.com/?ref=hackernoon.com')
chrome.maximize_window()
time.sleep(0)

women_btt = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Women')
women_btt.click()
time.sleep(0)

bottom_select = chrome.find_element(By.PARTIAL_LINK_TEXT,'Bottoms')
bottom_select.click()
time.sleep(0)

erika_short = chrome.find_element(By.PARTIAL_LINK_TEXT,"Erika Running Short")
erika_short.click()
time.sleep(0)

reviews_btt = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Reviews')
reviews_btt.click()
time.sleep(1)

details_btt = chrome.find_element(By.ID, 'tab-label-description-title')
details_btt.click()
time.sleep(1)

more_infos_btt = chrome.find_element(By.ID, 'tab-label-additional-title')
more_infos_btt.click()
time.sleep(1)

reviews2_btt = chrome.find_element(By.ID, 'tab-label-reviews-title')
reviews2_btt.click()
time.sleep(1)

nickname_input = chrome.find_element(By.ID, 'nickname_field')
nickname_input.send_keys('Red_Tail_Dog')
time.sleep(1)

summary_input = chrome.find_element(By.ID, 'summary_field')
summary_input.send_keys('BowWow!')
time.sleep(1)

review_input = chrome.find_element(By.ID, 'review_field')
review_input.send_keys('BowWow! Red Flag! BowWow! Red Flag! '
                       'BowWow! Red Flag! BowWow! Red Flag! BowWow! Red Flag!'
                       'BowWow! Red Flag!BowWow! Red Flag!BowWow! Red Flag!')
time.sleep(1)

submit_review_btt = chrome.find_element(By.CSS_SELECTOR, '#review-form > div > div > button > span')
submit_review_btt.click()
time.sleep(1)

qty_field = chrome.find_element(By.ID, 'qty')
qty_field.clear()
qty_field.send_keys('2')
time.sleep(1)

size30_selector = chrome.find_element(By.ID, 'option-label-size-143-item-173')
size30_selector.click()
time.sleep(1)

redcolor_selector = chrome.find_element(By.ID, 'option-label-color-93-item-58')
redcolor_selector.click()
time.sleep(1)

add_to_cart_btt = chrome.find_element(By.ID, 'product-addtocart-button')
add_to_cart_btt.click()
time.sleep(1)

