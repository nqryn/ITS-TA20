import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)


chrome.get("http://automationpractice.com/index.php")
chrome.maximize_window()
time.sleep(1)
# ID selector 1
first_name_input = chrome.find_element(By.ID, "search_query_top")
first_name_input.send_keys("dress")
time.sleep(1)
# NAME selector 1
search_button = chrome.find_element(By.NAME, "submit_search")
search_button.click()
time.sleep(1)
# ID selector 2
header_logo_button = chrome.find_element(By.ID, "header_logo")
header_logo_button.click()
time.sleep(1)
# ID selector 3
contact_link_button = chrome.find_element(By.ID, "contact-link")
contact_link_button.click()
time.sleep(1)
# ID selector 4
message_input = chrome.find_element(By.ID, "message")
message_input.send_keys("OK!")
time.sleep(1)


chrome.get("https://formy-project.herokuapp.com/")
chrome.maximize_window()
time.sleep(1)
# CSS_SELECTOR selector 1
autocomplete_button = chrome.find_element(By.CSS_SELECTOR, "body > div > div > li:nth-child(5) > a")
autocomplete_button.click()
time.sleep(2)
# XPATH selector 1
street1_input = chrome.find_element(By.XPATH, "//*[@id='street_number']")
street1_input.send_keys("rue Voltaire")
time.sleep(1)
# XPATH selector 2
street2_input = chrome.find_element(By.XPATH, "//*[@id='route']")
street2_input.send_keys("5")
time.sleep(1)
# XPATH selector 3
city_input = chrome.find_element(By.XPATH, '//*[@id="locality"]')
city_input.send_keys("Paris")
time.sleep(1)
# XPATH selector 4
admin_area_input = chrome.find_element(By.XPATH, '//*[@id="administrative_area_level_1"]')
admin_area_input.send_keys("Ille-de-France")
time.sleep(1)
# XPATH selector 5
zip_input = chrome.find_element(By.XPATH, '//*[@id="postal_code"]')
zip_input.send_keys("401999")
time.sleep(1)
# XPATH selector 6
country_input = chrome.find_element(By.XPATH, '//*[@id="country"]')
country_input.send_keys("France")
time.sleep(1)
# XPATH selector 7
address_input = chrome.find_element(By.XPATH, "//*[@id='autocomplete']")
address_input.send_keys("Paris, 21eme")
time.sleep(2)
# ID Selector 5
formy_logo_button = chrome.find_element(By.ID, "logo")
formy_logo_button.click()
time.sleep(1)
# CSS_SELECTOR 2
chrome.find_element(By.CSS_SELECTOR, "body > div > div > li:nth-child(6) > a").click()
time.sleep(1)
# CSS_SELECTOR 3
chrome.find_element(By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > div > "
                                     "div > button.btn.btn-lg.btn-primary").click()
time.sleep(1)
# CSS_SELECTOR 4
chrome.find_element(By.CSS_SELECTOR, "#btnGroupDrop1").click()
time.sleep(2)
# CSS_SELECTOR 5
chrome.find_element(By.CSS_SELECTOR, "body > div > form > div:nth-child(2) > "
                                     "div > div > div > button:nth-child(3)").click()
time.sleep(2)


chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.maximize_window()
time.sleep(1)

# CSS_SELECTOR 6
chrome.find_element(By.CSS_SELECTOR, "#ez-accept-all").click()
time.sleep(1)
# NAME selector 2
chrome.find_element(By.NAME, "firstname").send_keys("Tommy")
time.sleep(1)
# NAME selector 3
chrome.find_element(By.NAME, "lastname").send_keys("Johnnes")
time.sleep(1)
# ID selector 6
chrome.find_element(By.ID, "datepicker").send_keys("12.05.1975")
time.sleep(1)
# ID selector 7
chrome.find_element(By.ID, "exp-0").click()
time.sleep(1)
# ID selector 8
chrome.find_element(By.ID, "sex-0").click()
time.sleep(1)
# ID selector 9
chrome.find_element(By.ID, "cookieChoiceDismiss").click()
time.sleep(1)
# NAME selector 4
profession_button = chrome.find_elements(By.NAME, "profession")
profession_button[1].click()
time.sleep(1)
# NAME selector 5
tool_button = chrome.find_elements(By.NAME, "tool")
tool_button[2].click()
time.sleep(2)


chrome.get("https://formy-project.herokuapp.com/")
chrome.maximize_window()
time.sleep(1)
# LINK_TEXT selector 1
chrome.find_element(By.LINK_TEXT, "Form").click()
time.sleep(1)
# CLASS_NAME selector 1
firstname_input = chrome.find_elements(By.CLASS_NAME, 'form-control')
firstname_input[0].send_keys('Tiberiu')
time.sleep(1)
# CLASS_NAME selector 2
lastname_input = chrome.find_elements(By.CLASS_NAME, 'form-control')
lastname_input[1].send_keys('Popoviciu')
time.sleep(1)
# CLASS_NAME selector 3
job_input = chrome.find_elements(By.CLASS_NAME, 'form-control')
job_input[2].send_keys('Engineer')
time.sleep(1)
# CSS_NAME attribute-value selector 1
education_button = chrome.find_element(By.CSS_SELECTOR, 'input[value="radio-button-3"]')
education_button.click()
time.sleep(1)
# CSS_NAME attribute-value selector 2
sex_button = chrome.find_element(By.CSS_SELECTOR, 'input[value="checkbox-1"]')
sex_button.click()
time.sleep(1)
# CLASS_NAME selector 4
experience_input = chrome.find_elements(By.CLASS_NAME, 'form-control')
experience_input[3].click()
time.sleep(1)
# CSS_NAME attribute-value selector 3
sex_button = chrome.find_element(By.CSS_SELECTOR, 'option[value="1"]')
sex_button.click()
time.sleep(1)
# CSS_NAME attribute-value selector 4
date_input = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="mm/dd/yyyy"]')
date_input.click()
date_input.send_keys('12/12/2000')
time.sleep(2)
# LINK_TEXT selector 2
submit_button = chrome.find_element(By.LINK_TEXT, 'Submit')
submit_button.click()
time.sleep(1)
# CSS_SELECTOR - ID selector 1
home_return_by_formy = chrome.find_element(By.CSS_SELECTOR, '#logo')
home_return_by_formy.click()
time.sleep(1)
# PARTIAL_LINK_TEXT selector 1
key_mouse_button = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Key and Mouse')
key_mouse_button.click()
time.sleep(1)
# CSS_SELECTOR attribute-value selector 5
full_name_input = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter full name"]')
full_name_input.send_keys('Tiberiu Popoviciu')
time.sleep(1)
# CSS_SELECTOR ID selector 2
button_input = chrome.find_element(By.CSS_SELECTOR, '#button')
button_input.click()
time.sleep(1)
# CSS_SELECTOR ID selector 3
components_dropdown = chrome.find_element(By.CSS_SELECTOR, '#navbarDropdownMenuLink')
components_dropdown.click()
time.sleep(2)
# CLASS_NAME selector 5
modal_link = chrome.find_elements(By.CLASS_NAME, 'dropdown-item')
modal_link[9].click()
time.sleep(1)
# CSS_SELECTOR ID selector 4
open_modal_button = chrome.find_element(By.CSS_SELECTOR, '#modal-button')
open_modal_button.click()
time.sleep(1)
# CSS_SELECTOR ID selector 5
open_modal_button = chrome.find_element(By.CSS_SELECTOR, '#close-button')
open_modal_button.click()
time.sleep(2)


chrome.get("https://the-internet.herokuapp.com/")
chrome.maximize_window()
time.sleep(1)
# PARTIAL_LINK_TEXT selector 2
form_auth_link = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Form Auth')
form_auth_link.click()
time.sleep(1)
# CSS_SELECTOR attribute-value selector 6
username_input = chrome.find_element(By.CSS_SELECTOR, 'input[name="username"]')
username_input.send_keys('alabala.portocala')
time.sleep(1)
# CSS_SELECTOR attribute-value selector 7
password_input = chrome.find_element(By.CSS_SELECTOR, 'input[type="password"]')
password_input.send_keys('111111')
time.sleep(1)
# CLASS_NAME selector 6
submit_button = chrome.find_element(By.CLASS_NAME, 'radius')
submit_button.click()
time.sleep(1)
# CSS_SELECTOR attribute-value selector 8
username_input = chrome.find_element(By.CSS_SELECTOR, 'input[name="username"]')
username_input.send_keys('tomsmith')
time.sleep(1)
# CSS_SELECTOR attribute-value selector 9
password_input = chrome.find_element(By.CSS_SELECTOR, 'input[type="password"]')
password_input.send_keys('SuperSecretPassword!')
time.sleep(1)
# CLASS_NAME selector 7
submit_button = chrome.find_element(By.CLASS_NAME, 'radius')
submit_button.click()
time.sleep(1)
# CSS_SELECTOR attribute-value selector 10
logout_button = chrome.find_element(By.CSS_SELECTOR, 'i[class="icon-2x icon-signout"]')
logout_button.click()
time.sleep(1)


chrome.get("https://the-internet.herokuapp.com/")
chrome.maximize_window()
time.sleep(1)
# PARTIAL_LINK_TEXT selector 3
forgot_pass_link = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Forgot')
forgot_pass_link.click()
time.sleep(1)
# CSS_SELECTOR attribute-value selector 11
email_input = chrome.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_input.send_keys('alabala@gnail.bom')
time.sleep(1)
# CSS_NAME class selector 1
retrieve_button = chrome.find_element(By.CSS_SELECTOR, 'button.radius')
retrieve_button.click()
time.sleep(2)
chrome.back()
chrome.back()
time.sleep(5)

# CSS_NAME class selector 1
chrome.get("https://formy-project.herokuapp.com/")
chrome.maximize_window()
time.sleep(1)

autocomplete_button = chrome.find_element(By.CSS_SELECTOR, "body > div > div > li:nth-child(5) > a")
autocomplete_button.click()
time.sleep(2)

address_input = chrome.find_elements(By.TAG_NAME, "input")
address_input[0].send_keys("Cluj-Napoca, str. Tache Petrescu, nr.5")
time.sleep(1)
dismiss_button = chrome.find_element(By.CLASS_NAME, "dismissButton")
dismiss_button.click()
address_input[1].send_keys("str. Tache Petrescu")
time.sleep(1)
address_input[2].send_keys("nr.5")
time.sleep(1)
address_input[3].send_keys("Cluj-Napoca")
time.sleep(1)
address_input[4].send_keys("Cluj")
time.sleep(1)
address_input[5].send_keys("400669")
time.sleep(1)
address_input[6].send_keys("Romania")
time.sleep(3)
chrome.back()



