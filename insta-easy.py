from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

browser = webdriver.Firefox()

browser.get('http://instagram.com/')

# accept cookies
cookie_accept = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
cookie_accept.click()

# perform login
user = browser.find_element(By.NAME, "username")
passw = browser.find_element(By.NAME, 'password')

# input login credentials via commandline arguments
user.send_keys(sys.argv[1])
passw.send_keys(sys.argv[2])

sleep(2)
login_button = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
login_button.click()

sleep(2)
notification_button = browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
notification_button.click()

sleep(2)
profile = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a')
profile.click()