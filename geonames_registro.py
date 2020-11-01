from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep
from random import randint
# Se importa WebDriverWait y las otras librerias para hace esperas explicitas.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 2captcha API
# pip install 2captcha-python
import sys
import os
from twocaptcha import TwoCaptcha
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from PIL import Image


# Ingresar variables a registrar
url = 'http://forum.geonames.org/gforum/user/insert.page'
name_field = 'pefufyke'
username_field = ''
password_field = 'pepe3677'
email_field = 'pepetoo1567@gmail.com'
# Website personal
website = 'versaria.es'
# Biografia
bio = 'Mercadotecnia'

def get_captcha(driver, element, path):
    # Asignando las medidas
    location = element.location
    size = element.size
    # salvar un screenshot de toda la pagina
    driver.save_screenshot(path)

    # Usar PIL para abrir la imagen.
    image = Image.open(path)

    left = location['x']
    top = location['y'] 
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = image.crop((left, top, right, bottom))  # definiendo los puntos para hacer el corte.
    image.save(path, 'png')  # Salvando la imagen en el path asignado.
    

def api_2captcha():
    # Introducir el Apikey 2 veces.
    api_key = os.getenv('cb72b72b7810a84d5ec3891e1dbeca54', 'cb72b72b7810a84d5ec3891e1dbeca54')

    solver = TwoCaptcha(api_key)

    try:
        # Ingresar el path de la imagen.
        result = solver.normal(r"C:\Users\Xenofungus\Desktop\selenium\captcha.png")
        token = result['code']        
        return token

    except Exception as e:
        sys.exit(e)

    else:
        sys.exit('solved: ' + str(result))

def registro(url,name,username,password,email,website,bio):
    # Especificar el PATH de geckodriver en Windows.
    driver = webdriver.Firefox(executable_path=r"c:\se\geckodriver.exe")
    # import pdb; pdb.set_trace()
    
     # Abrir la pagina especificada o deseada.
    print('Abriendo Navegador y cargando la pagina:\n ',url )
    driver.get(url)  
    
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td/form/table[2]/tbody/tr[3]/td[2]/input")))

        # Ingreso de los campos requeridos para registrar.
        print('**********\nIngresando Datos.')
        try:
            # Ubicar campo.
            name_field = driver.find_element_by_name('username')
            # Limpiar campo.
            name_field.clear()
            # Ingresar datos en el campo.
            name_field.send_keys(name)            
           
            email_field = driver.find_element_by_name('email') 
            email_field.clear()
            email_field.send_keys(email)        
           
            password_field = driver.find_element_by_name('password') 
            password_field.clear()
            password_field.send_keys(password)

            password_field = driver.find_element_by_name('password_confirm') 
            password_field.clear()
            password_field.send_keys(password)
        
        except:
            print('Error al ingresar los Datos. Revise.')
            exit()

        try:
            print("Obteniendo Imagen Captcha.")
            # Obteniendo la imagen/captcha
            img = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td/form/table[2]/tbody/tr[7]/td[2]/img")
            # Se tiene que dar el path donde se va a guardar la imagen que luego sera asignada al api de 2captcha.
            get_captcha(driver, img, r"C:\Users\Xenofungus\Desktop\selenium\captcha.png")
        except:
            print('Error al obtener imagen')
            exit()
	
        try:
            token = api_2captcha()
            sleep(2)
            print('reCaptcha Exitoso.')
        
        except:	
            print("Timeout1. Error resolviendo reCaptcha")
            exit()
            #driver.close()

        try:            
            captcha_field = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/form/table[2]/tbody/tr[7]/td[2]/input') 
            captcha_field.clear()
            captcha_field.send_keys(token)
            print('Token ingresado con exito.\nTexto:  ', token)
        except:
            print('Error al introducir el texto de 2cpatcha.')     
            exit()         
        
        # # Boton de registro.
        print('**********\nRegistrando....')
        try:
            sleep(1.8)
            driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td/form/table[2]/tbody/tr[8]/td/input[1]").click()
            
        except:
            print('Error al registrar. Revisar Datos.')
            exit()          
      

        # usuario
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/span/a[1]"))).click()
        
        # Ingreso de bio y website
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr/td/table/tbody/tr[16]/td[2]/input")))       

        website_field = driver.find_element_by_name('website') 
        website_field.clear()
        website_field.send_keys(website)

        bio_field = driver.find_element_by_name('biography') 
        bio_field.clear()
        bio_field.send_keys(bio)
        
        driver.find_element_by_name("viewemail").click()
        
        driver.find_element_by_name("submit").click()    

        print('Registro exitoso')

        # # Cerrar el navegador.
        # # driver.close()

    except:
        print('Registro fallido. Revisar.')
        # Cerrar el navegador.
        # driver.close()


registro(url,name_field,username_field,password_field,email_field,website,bio)


