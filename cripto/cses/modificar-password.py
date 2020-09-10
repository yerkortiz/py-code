import os
from selenium import webdriver
from getpass import getpass

username = input('ingrese nick\n')
password = getpass('ingrese password\n')
new_password = getpass('ingrese nueva password\n')

current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')
driver.get('https://cses.fi/login/')

username_textbox = driver.find_element_by_id('nick')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('pass')
password_textbox.send_keys(password)

submit_button = driver.find_element_by_xpath("//input[@type='submit']")
submit_button.submit()

next_url = driver.find_element_by_xpath("//a[@class='account']")
next_url.click()
current = driver.current_url
driver.get(current + '/password/')

old_textbox = driver.find_element_by_name('old')
old_textbox.send_keys(password)
new1_textbox = driver.find_element_by_name('new1')
new1_textbox.send_keys(new_password)
new2_textbox = driver.find_element_by_name('new2')
new2_textbox.send_keys(new_password)

login_button = driver.find_element_by_xpath("//input[@type='submit']")
login_button.submit()