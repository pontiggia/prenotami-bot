# dev by ponti github.com/pontiggia
# python 3.9

from urllib.parse import ParseResultBytes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from locators import mainPageLocators as mpl
from locators import consolare_moron as cm
import time, json
from os import system

PATH = "/home/ponti/Escritorio/dev/Trabajos/prenotami-BOT/chromedriver"  # Ruta del archivo chromedriver

operacion = 4

while operacion > 3:
    x_cliente = int(input("Introduci el numero del cliente: "))
    print("Estado Civil = 1 \nCiudadania por descendencia = 2 \nPasaporte = 3")
    operacion = int(input("Que tipo de operacion queres realizar?: "))
    if operacion > 3:
        print("Operacion invalida \nVolviendo atras...")
        time.sleep(2)
        system('clear')

with open ('users_info.json') as file:
    json_dict = json.load(file)
    lista_clientes = json_dict["listaClientes"]
    cliente = lista_clientes[x_cliente-1] # Le restamos uno debido a que la listas empiezan desde 0
    
    email = cliente["email"]
    password = cliente["password"]
    #tipo_reserva = cliente["tipoReserva"]
    address = cliente["address"]
    hijos_Menores = cliente["hijosMenores"]
    estado_Civil = cliente["estadoCivil"]
    pasaporte_Italiano = cliente["pasaporteItaliano"]
    hijos_Numero = cliente["hijosNumero"]
    mensaje_json = cliente["mensaje"]
    nombre_completo_conyuge = cliente["nombre_completo_conyuge"]
    estatura = cliente["estatura"]
    color_ojos = cliente["color_de_ojos"]
    nombre_completo_hijo = cliente["nombre_completo_hijo"]

print("Abriendo navegador")
webdriver0 = webdriver.Chrome(PATH) # Crea el objeto del navegador
#webdriver0.maximize_window()
webdriver0.get("https://prenotami.esteri.it/")

def login(): # funcion de inicio de sesion

    # Coloca los datos de inicio de sesion en los input correctos
    login_email = webdriver0.find_element_by_id(mpl.LOGIN_EMAIL_LOCATORS) 
    login_email.send_keys(email)
        
    login_password = webdriver0.find_element_by_id(mpl.LOGIN_PASSWORD_LOCATORS) 
    login_password.send_keys(password)
    login_password.send_keys(Keys.RETURN)
    print("Sesion Iniciada")

def civil_state(): # funcion para el condicional estado civil
    idioma = webdriver0.find_element_by_xpath(mpl.LENGUAJE_BUTTON)
    idioma.click()
    time.sleep(1)
    reserva = webdriver0.find_element_by_id(mpl.RESERVA_NAV)
    reserva.click()
    time.sleep(1)
    prenota = webdriver0.find_element_by_xpath(cm.RESERVA_BUTTON_CIVIL_STATE)
    prenota.click()
    time.sleep(1)
    mensaje = webdriver0.find_element_by_id(mpl.MESSAGE_LOCATORS)
    mensaje.send_keys(mensaje_json)
        
    terminos_y_condiciones = webdriver0.find_element_by_id(mpl.PRIVACY_CHECK)
    terminos_y_condiciones.click()

    enviar_y_terminar = webdriver0.find_element_by_id(mpl.SUBMIT_LOCATORS)
    enviar_y_terminar.click()
    time.sleep(1)


def citizenship(): # funcion para el condicional ciudadania
    idioma = webdriver0.find_element_by_xpath(mpl.LENGUAJE_BUTTON)
    idioma.click()
    time.sleep(1)
    reserva = webdriver0.find_element_by_id(mpl.RESERVA_NAV)
    reserva.click()
    time.sleep(1)
    prenota = webdriver0.find_element_by_xpath(cm.RESERVA_BUTTON_CITIZENSHIP2)
    prenota.click()
    time.sleep(1)
    mensaje = webdriver0.find_element_by_id(mpl.MESSAGE_LOCATORS)
    mensaje.send_keys(mensaje_json)
        
    terminos_y_condiciones = webdriver0.find_element_by_id(mpl.PRIVACY_CHECK)
    terminos_y_condiciones.click()

    enviar_y_terminar = webdriver0.find_element_by_id(mpl.SUBMIT_LOCATORS)
    enviar_y_terminar.click()
    time.sleep(1)


def passport(): # funcion para el condicional pasaporte
    idioma = webdriver0.find_element_by_xpath(mpl.LENGUAJE_BUTTON)
    idioma.click()
    time.sleep(1)
    reserva = webdriver0.find_element_by_id(mpl.RESERVA_NAV)
    reserva.click()
    time.sleep(1)
    prenota = webdriver0.find_element_by_xpath(cm.RESERVA_BUTTON_PASSPORT2)
    prenota.click()
    time.sleep(1)
    italian_passport = webdriver0.find_element_by_id(cm.ITALIAN_PASSPORT_OWNER)
    Select(italian_passport).select_by_value(pasaporte_Italiano)
    
    direccion_completa = webdriver0.find_element_by_id(cm.COMPLETE_ADDRESS_PASSPORT2)
    direccion_completa.send_keys(address)
    
    estado_civil = webdriver0.find_element_by_id(cm.CIVIL_STATE_PASSPORT2)
    Select(estado_civil).select_by_value(estado_Civil)
    
    nombre_Completo_Conyuge = webdriver0.find_element_by_id(cm.FULL_NAME_CONYUGE)
    nombre_Completo_Conyuge.send_keys(nombre_completo_conyuge)

    estatura_cm = webdriver0.find_element_by_id(cm.TALL_IN_CM)
    estatura_cm.send_keys(estatura)

    color_Ojos = webdriver0.find_element_by_id(cm.EYES_COLOR)
    Select(color_Ojos).select_by_value(color_ojos)

    hijos_menores = webdriver0.find_element_by_id(cm.MINOR_CHILDREN_PASSPORT2)
    Select(hijos_menores).select_by_value(hijos_Menores)

    hijos_numero = webdriver0.find_element_by_id(cm.MINOR_CHILDREN_NUMBER2)
    hijos_numero.send_keys(hijos_Numero)

    nombre_Completo_Hijo = webdriver0.find_element_by_id(cm.FULL_NAME_MINOR_CHILDREN)
    nombre_Completo_Hijo.send_keys(nombre_completo_hijo)
    mensaje = webdriver0.find_element_by_id(mpl.MESSAGE_LOCATORS)
    mensaje.send_keys(mensaje_json)
        
    terminos_y_condiciones = webdriver0.find_element_by_id(mpl.PRIVACY_CHECK)
    terminos_y_condiciones.click()

    enviar_y_terminar = webdriver0.find_element_by_id(mpl.SUBMIT_LOCATORS)
    enviar_y_terminar.click()
    time.sleep(1)


if __name__ == '__main__':
		if operacion == 1:
            login()
            civil_state()
        elif operacion == 2:
            login()
            citizenship()
        elif operacion == 3:
            login()
            passport()


