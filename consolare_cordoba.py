# dev by ponti github.com/pontiggia
# python 3.9

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from locators import mainPageLocators as mpl
import time, json
from os import system

PATH = "/home/ponti/Escritorio/dev/Trabajos/prenotami-BOT/chromedriver"  # Ruta del archivo chromedriver

operacion = 5

while operacion > 4:
    x_cliente = int(input("Introduci el numero del cliente: "))
    print("Pasaporte = 1 \nLegalizacion = 2 \nServicios Consulares = 3 \nCiudadania = 4")
    operacion = int(input("Que tipo de operacion queres realizar?: "))
    if operacion > 4:
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
        

def passport(): # Funcion para el condicional pasaporte 
    idioma = webdriver0.find_element_by_xpath(mpl.LENGUAJE_BUTTON)
    idioma.click()
    time.sleep(1)
    reserva = webdriver0.find_element_by_id(mpl.RESERVA_NAV)
    reserva.click()
    time.sleep(1)
    prenota = webdriver0.find_element_by_xpath(mpl.RESERVA_BUTTON_PASSPORT)
    prenota.click()
    time.sleep(1)
    direccion_completa = webdriver0.find_element_by_id(mpl.COMPLETE_ADDRES_PASSPORT)
    direccion_completa.send_keys(address)
    
    hijos_menores = webdriver0.find_element_by_id(mpl.MINOR_CHILDREN_PASSPORT)
    Select(hijos_menores).select_by_value(hijos_Menores)
        
    estado_civil = webdriver0.find_element_by_id(mpl.CIVIL_STATE_PASSPORT)
    Select(estado_civil).select_by_value(estado_Civil)
        
    pasaporte_italiano = webdriver0.find_element_by_id(mpl.ITALIAN_PASSPORT)
    Select(pasaporte_italiano).select_by_value(pasaporte_Italiano)
        
    hijos_numero = webdriver0.find_element_by_id(mpl.NUMBER_CHILD_PASSPORT)
    hijos_numero.send_keys(hijos_Numero)
        
    mensaje = webdriver0.find_element_by_id(mpl.MESSAGE_LOCATORS)
    mensaje.send_keys(mensaje_json)
        
    terminos_y_condiciones = webdriver0.find_element_by_id(mpl.PRIVACY_CHECK)
    terminos_y_condiciones.click()

    enviar_y_terminar = webdriver0.find_element_by_id(mpl.SUBMIT_LOCATORS)
    enviar_y_terminar.click()
    time.sleep(1)

    
def legalization(): # Funcion para el condicional legalizacion
    idioma = webdriver0.find_element_by_xpath(mpl.LENGUAJE_BUTTON)
    idioma.click()
    time.sleep(1)
    reserva = webdriver0.find_element_by_id(mpl.RESERVA_NAV)
    reserva.click()
    time.sleep(1)
    prenota = webdriver0.find_element_by_xpath(mpl.RESERVA_BUTTON_LEGALIZATION)
    prenota.click()
    time.sleep(1)
    mensaje = webdriver0.find_element_by_id(mpl.MESSAGE_LOCATORS)
    mensaje.send_keys(mensaje_json)
        
    terminos_y_condiciones = webdriver0.find_element_by_id(mpl.PRIVACY_CHECK)
    terminos_y_condiciones.click()

    enviar_y_terminar = webdriver0.find_element_by_id(mpl.SUBMIT_LOCATORS)
    enviar_y_terminar.click()
    time.sleep(1)
        
   
def consularServices(): # Funcion para el condicional Servicios consulares
    idioma = webdriver0.find_element_by_xpath(mpl.LENGUAJE_BUTTON)
    idioma.click()
    time.sleep(1)
    reserva = webdriver0.find_element_by_id(mpl.RESERVA_NAV)
    reserva.click()
    time.sleep(1)
    prenota = webdriver0.find_element_by_xpath(mpl.RESERVA_BUTTON_CONSULAR_SERVICE)
    prenota.click()
    mensaje = webdriver0.find_element_by_id(mpl.MESSAGE_LOCATORS)
    mensaje.send_keys(mensaje_json)
    
    terminos_y_condiciones = webdriver0.find_element_by_id(mpl.PRIVACY_CHECK)
    terminos_y_condiciones.click()
    time.sleep(1)
    enviar_y_terminar = webdriver0.find_element_by_id(mpl.SUBMIT_LOCATORS)
    enviar_y_terminar.click()
    time.sleep(1)


def citizenship(): # Funcion para el condicional Ciudadania
    idioma = webdriver0.find_element_by_xpath(mpl.LENGUAJE_BUTTON)
    idioma.click()
    time.sleep(1)
    reserva = webdriver0.find_element_by_id(mpl.RESERVA_NAV)
    reserva.click()
    time.sleep(1)
    prenota = webdriver0.find_element_by_xpath(mpl.RESERVA_BUTTON_CITIZENSHIP)
    prenota.click()
    time.sleep(1)
    estado_civil = webdriver0.find_element_by_id(mpl.CIVIL_STATE_CITIZENSHIP)
    Select(estado_civil).select_by_value(estado_Civil)
        
    direccion_completa = webdriver0.find_element_by_id(mpl.COMPLETE_ADDRES_CITIZENSHIP)
    direccion_completa.send_keys(address)
        
    hijos_numero = webdriver0.find_element_by_id(mpl.NUMBER_CHILD_CITIZENSHIP)
    hijos_numero.send_keys(hijos_Numero)
        
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
            passport()
        elif operacion == 2:
            login()
            legalization()
        elif operacion == 3:
            login()
            consularServices()
        elif operacion == 4:
            login()
            citizenship()






    
