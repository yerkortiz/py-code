import os
from selenium import webdriver
from getpass import getpass

username = input('ingrese mail')

current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')
driver.get('https://n1g.cl/Home/recuperar-contrase%C3%B1a')

username_textbox = driver.find_element_by_name('email')
username_textbox.send_keys(username)

submit_button = driver.find_element_by_xpath("//button[@class='form-control-submit btn btn-primary hidden-xs-down' and @name='submit']")
submit_button.click()
#llega un link al correo que intenta, con ese link es posible reestablecer la password.
