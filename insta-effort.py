#%%
from argparse import Action
import enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
import sys

# username = sys.argv[1]
username = 't0ffif33'

browser = webdriver.Firefox()

browser.get('http://instagram.com/')

cookies = [{'name': 'mid', 'value': 'Yf2ztwAEAAE1Yhdau2N3RI0ql-N2', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': False, 'expiry': 1707088567, 'sameSite': 'Lax'}, {'name': 'ig_did', 'value': '5894C3EF-CB10-434B-BAFB-778D56185169', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': True, 'expiry': 1707088567, 'sameSite': 'Lax'}, {'name': 'sessionid', 'value': '51140454508%3AaRd0BItYLbVood%3A11', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': True, 'expiry': 1675552572, 'sameSite': 'Lax'}, {'name': 'shbid', 'value': '"12415\\05451140454508\\0541675552572:01f7a5f7a8ca31900b259f54ad1284f655144309eebd704a0138e325f97b0f2a6593fd29"', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': True, 'expiry': 1644621372, 'sameSite': 'Lax'}, {'name': 'shbts', 'value': '"1644016572\\05451140454508\\0541675552572:01f7acbfd817917795245b5849433f360edb8a212c82036976381763de700b33e7bf0e28"', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': True, 'expiry': 1644621372, 'sameSite': 'Lax'}, {'name': 'csrftoken', 'value': 'ZEGz1mhm3drhfprLsk7sjZrHxXx0fpmt', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': False, 'expiry': 1675466370, 'sameSite': 'Lax'}, {'name': 'rur', 'value': '"RVA\\05451140454508\\0541675552771:01f72a15c432d2cf26d6f2a6a5f68953908627733bcff2fba2b8ce47316edaa34fa63327"', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': True, 'sameSite': 'Lax'}, {'name': 'ds_user_id', 'value': '51140454508', 'path': '/', 'domain': '.instagram.com', 'secure': True, 'httpOnly': False, 'expiry': 1651792770, 'sameSite': 'Lax'}]
for c in cookies:
    browser.add_cookie(c)

browser.get(f'http://instagram.com/{username}/')

sleep(1)
followers_button = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
followers_button.click()

#%%
x = browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')

#%%
def is_username(uname):
    predicate = ' ' not in uname and uname.isascii() and uname.islower()
    return predicate

l = x.text.split('\n')
illegal_words = ['Remove', 'Follow', '·']
l = [f for f in l if f not in illegal_words]
l = [f for f in l if is_username(f)]
followers = l


#%%

following_button = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
following_button.click()

x = browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]')
# %%

l = x.text.split('\n')
illegal_words = ['Following', 'Verified']
l = [f for f in l if f not in illegal_words]
l = [f for f in l if is_username(f)]
following = l

# %%

for person in following:
    if person not in followers:
        print(person)