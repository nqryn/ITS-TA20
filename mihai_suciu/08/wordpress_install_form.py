import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://s1.demo.opensourcecms.com/wordpress/wp-admin/install.php")
chrome.maximize_window()
time.sleep(1)

site_title_input = chrome.find_element(By.TAG_NAME,"input")
site_title_input.send_keys("orangesky")
time.sleep(1)

username_input = chrome.find_element(By.NAME,"user_name")
username_input.send_keys("bluemonkey")
time.sleep(1)

password_input = chrome.find_element(By.ID,"pass1")
password_input.clear()
password_input.send_keys("R3deyes_M0nkey!")
time.sleep(1)

show_button = chrome.find_elements(By.TAG_NAME,"span")
show_button[1].click()
time.sleep(1)

your_email_input = chrome.find_element(By.ID,"admin_email")
your_email_input.send_keys("blue_monkey@jungle.moon")
time.sleep(1)

search_engine_button = chrome.find_element(By.ID,"blog_public")
search_engine_button.click()
time.sleep(1)

install_wordpress_button = chrome.find_elements(By.TAG_NAME,"input")
install_wordpress_button[7].click()
time.sleep(3)
