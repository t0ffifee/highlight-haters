from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Firefox()
browser.get('http://instagram.com/')

# accept cookies
cookie_accept = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
cookie_accept.click()

# perform login
user = browser.find_element(By.NAME, "username")
passw = browser.find_element(By.NAME, 'password')

user.send_keys("your_username")
passw.send_keys("your_password")

sleep(5)
login_button = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
login_button.click()