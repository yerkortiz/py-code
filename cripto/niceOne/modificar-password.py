import os
from selenium import webdriver
from getpass import getpass

username = input('ingrese mail\n')
password = getpass('ingrese password\n')
new_password = getpass('ingrese nueva password\n')

current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')
driver.get('https://n1g.cl/Home/iniciar-sesion?back=my-account')

username_textbox = driver.find_element_by_name('email')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('password')
password_textbox.send_keys(password)

login_button = driver.find_element_by_id('submit-login')
login_button.submit()

driver.get('https://n1g.cl/Home/datos-personales')

#textbox password
password_textbox = driver.find_element_by_name('password')
password_textbox.send_keys(password)

new_password_textbox = driver.find_element_by_name('new_password')
new_password_textbox.send_keys(new_password)

#checkbox acepto politicas de privacidad de la página
agree_checkbox = driver.find_element_by_name('psgdpr')
agree_checkbox.click()

#boton de submit para guardar
submit_button = driver.find_element_by_xpath("//button[@data-link-action='save-customer']")
submit_button.submit()

print('contraseña cambiada correctamente')
