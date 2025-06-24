from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
INSTA_USERNAME = os.getenv("user")
INSTA_PASSWORD = os.getenv("pass")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/")

time.sleep(5)

try:
    user_input_username = driver.find_element(By.NAME, value="username")
except NoSuchElementException:
    user_input_email = driver.find_element(By.NAME, value="email")
    user_input_email.send_keys(INSTA_USERNAME)
else:
    user_input_username.send_keys(INSTA_USERNAME)

user_input_pass = driver.find_element(By.NAME, value="password")
user_input_pass.send_keys(INSTA_PASSWORD)
user_input_pass.send_keys(Keys.ENTER)
time.sleep(30)
driver.get(f"https://www.instagram.com/{INSTA_USERNAME}/")
time.sleep(10)
following = driver.find_element(By.CSS_SELECTOR, value='header section:nth-child(3) ul li:nth-child(3) div')
following.click()
time.sleep(5)
modal = driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
for i in range(8):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    time.sleep(1)

button_list = driver.find_elements(By.CSS_SELECTOR, value="._acan._acap._acat._aj1-._ap30")
for button in button_list:
    button.click()
    time.sleep(1)
    unfollow = driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]')
    unfollow.click()
