import os
from selenium import webdriver
from getpass import getpass

username = input('Ingrese nick\n')
password = input('Ingrese password\n')
email = input('Ingrese email\n')
current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')
driver.get('https://cses.fi/register/')

username_textbox = driver.find_element_by_id('nick')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('pass1')
password_textbox.send_keys(password)

password2_textbox = driver.find_element_by_name('pass2')
password2_textbox.send_keys(password)

email_textbox = driver.find_element_by_id('email')
email_textbox.send_keys(email)

login_button = driver.find_element_by_xpath("//input[@type='submit']")
login_button.submit()