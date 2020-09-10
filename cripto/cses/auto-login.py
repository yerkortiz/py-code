import os
from selenium import webdriver
from getpass import getpass
#nota: el chromedriver en el directorio es para osx, no usar si se usa windows o linux
username = input('ingrese nick\n')
password = getpass('ingrese password\n')

current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')
driver.get('https://cses.fi/login/')

username_textbox = driver.find_element_by_id('nick')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('pass')
password_textbox.send_keys(password)

submit_button = driver.find_element_by_xpath("//input[@type='submit']")
submit_button.submit()