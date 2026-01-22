from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

user_name = "xantium0" #input("User:")
password_in = "programmingisace8" #input("Password:")

driver = webdriver.Firefox()
driver.get("https://www.csgoroll.com/en/withdraw/csgo/p2p")

time.sleep(10) # give webpage time to load

# click login

login = driver.find_element("xpath", "/html/body/cw-root/cw-header/nav/div[2]/div/cw-auth-buttons/div/button")
login.click()

time.sleep(10)

# log in steam

name = driver.find_element("xpath", "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input")
name.send_keys(user_name)

password = driver.find_element("xpath", "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input")
password.send_keys(password_in)

sign = driver.find_element("xpath", "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button")
sign.click()


time.sleep(20)

# actually log in

click_signin = driver.find_element("xpath", '//*[@id="imageLogin"]')
click_signin.click()

time.sleep(10)

# now redirect
redirect = driver.find_element("xpath", "/html/body/cw-root/cw-header/nav/div[2]/div/li/a")
redirect.click()

time.sleep(10)

# sort by best value
order_by = driver.find_element("id", "mat-select-0")
order_by.click()
order_by = driver.find_element("id", "mat-option-2")
order_by.click()

# set max price
max_price = 15
set_max = driver.find_element("id", "mat-input-2")
set_max.send_keys(max_price)


get_price = driver.find_element("class", "currency-value ng-star-inserted")
print(get_price)

time.sleep(300)