import os
from selenium import webdriver
from getpass import getpass

username = input('ingrese mail\n')

current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')
driver.get('https://cses.fi/reset/')

email_textbox = driver.find_element_by_name('email')
email_textbox.send_keys(username)
submit_button = driver.find_element_by_xpath("//input[@type='submit']")
submit_button.submit()
