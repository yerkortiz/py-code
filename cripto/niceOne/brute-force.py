import os
from selenium import webdriver
from getpass import getpass
#nota: el chromedriver en el directorio es para osx, no usar si se usa windows o linux
username = input('Ingrese email')
password = input('Ingrese una password incorrecta')
#username = 'yerko.ortizm@mail.udp.cl'
#password = 'pass_incorrecta'

current_directory = os.getcwd()
driver = webdriver.Chrome(current_directory + '/chromedriver')
for i in range(100):
    driver.get('https://n1g.cl/Home/iniciar-sesion?back=my-account')

    username_textbox = driver.find_element_by_name('email')
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_name('password')
    password_textbox.send_keys(password)

    login_button = driver.find_element_by_id('submit-login')
    login_button.submit()

#la página no bloquea la cuenta