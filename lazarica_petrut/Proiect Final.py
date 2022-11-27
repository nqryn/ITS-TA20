# import driver as driver

#print si assert !!! si conect la github

# Import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time


options = Options()
options.add_argument("start-maximized")

# Chrome Web Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Accesare Site
driver.get("https://www.saucedemo.com/")
print(driver.title)
time.sleep(0.5)
driver.implicitly_wait(5)

# Cautate si Introducere Element Username
username = driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")

time.sleep(0.5)

# Cautate si Introducere Element Password
driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")

time.sleep(0.5)

# Cautare si Click Button Login
driver.find_element(by=By.ID, value="login-button").click()

time.sleep(1)

# Sort Items
def sort_items():
    sort_dropdown = driver.find_element(by=By.CLASS_NAME, value="product_sort_container")
    select_dropdown = Select(sort_dropdown)
    # Sort by Index (Low to High)
    select_dropdown.select_by_index(2)
sort_items()

time.sleep(0.5)

# Add Items to Cart
def add_item_to_cart():
    item_backpack = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-backpack")
    item_backpack.click()
    time.sleep(0.5)
    item_tshirt_b = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-bolt-t-shirt")
    item_tshirt_b.click()
    time.sleep(0.5)
    item_onesie = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-onesie")
    item_onesie.click()
    time.sleep(0.5)
    item_bike_lights = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-bike-light")
    item_bike_lights.click()
    time.sleep(0.5)
    item_jacket = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-fleece-jacket")
    item_jacket.click()
    time.sleep(0.5)
    item_tshirt_r = driver.find_element(by=By.ID, value="add-to-cart-test.allthethings()-t-shirt-(red)")
    item_tshirt_r.click()
add_item_to_cart()

time.sleep(0.5)

# Click Shopping Cart Button
driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link").click()

# Remove Items From Cart
def remove_items_from_cart():
    # Remove Bike Light
    time.sleep(0.5)
    driver.find_element(by=By.ID, value="remove-sauce-labs-bike-light").click()
    # Remove Onesie
    time.sleep(0.5)
    driver.find_element(by=By.ID, value="remove-sauce-labs-onesie").click()
    # Remove TShirt Red
    time.sleep(0.5)
    driver.find_element(by=By.ID, value="remove-test.allthethings()-t-shirt-(red)").click()
remove_items_from_cart()

time.sleep(0.5)

# Checkout
driver.find_element(by=By.ID, value="checkout").click()

time.sleep(0.5)

# Checkout Info
def check_out_info():
    time.sleep(0.5)
    driver.find_element(by=By.ID, value="first-name").send_keys("Mos")
    time.sleep(0.5)
    driver.find_element(by=By.ID, value="last-name").send_keys("Craciun")
    time.sleep(0.5)
    driver.find_element(by=By.ID, value="postal-code").send_keys("21512")
check_out_info()

time.sleep(1)

# Continua Checkout
driver.find_element(by=By.ID, value="continue").click()

time.sleep(0.5)

# Finish Checkout
#print(driver.find_element(by=By.CLASS_NAME, value="cart_list").text)
driver.find_element(by=By.ID, value="finish").click()
print(driver.find_element(by=By.CLASS_NAME, value="complete-header").text)





# Verificare Pret
#pret_backpack = driver.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
#print(pret_backpack)
time.sleep(3)
