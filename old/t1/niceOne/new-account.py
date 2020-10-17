import os
from selenium import webdriver
from getpass import getpass
#nota: el chromedriver en el directorio es para osx, no usar si se prueba desde windows o linux

gender = int(input('ingrese 0 si se identifica como sr, 1 si se identifica como sra\n'))
nombre = input('ingrese nombre\n')
apellido = input('ingrese apellido\n')
username = input('ingrese mail\n')
password = getpass('ingrese password\n')


current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')

driver.get('https://n1g.cl/Home/iniciar-sesion?create_account=1')

#radio para señalar si es sr. o sra.
sr_radio =  driver.find_element_by_xpath("//input[@name='id_gender' and @value='1']")
sra_radio =  driver.find_element_by_xpath("//input[@name='id_gender' and @value='2']")
sr_radio.click() if gender == 0 else sra_radio.click()

#textbox nombre
nombre_textbox = driver.find_element_by_name('firstname')
nombre_textbox.send_keys(nombre)

#textbox apellido
apellido_textbox = driver.find_element_by_name('lastname')
apellido_textbox.send_keys(apellido)

#textbox mail
username_textbox = driver.find_element_by_name('email')
username_textbox.send_keys(username)

#textbox password
password_textbox = driver.find_element_by_name('password')
password_textbox.send_keys(password)

#checkbox acepto politicas de privacidad de la página
agree_checkbox = driver.find_element_by_name('psgdpr')
agree_checkbox.click()

#boton de submit para guardar
submit_button = driver.find_element_by_xpath("//button[@data-link-action='save-customer']")
submit_button.submit()



