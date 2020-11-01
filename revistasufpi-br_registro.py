from selenium import webdriver
from time import sleep
# Se importa WebDriverWait y las otras librerias para hace esperas explicitas.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
from twocaptcha import TwoCaptcha
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


# Ingresar variables a registrar
url = 'https://revistas.ufpi.br/index.php/gecont/index'
# Usuario o User
user_field = 'pefm71e'
# Nombre 
firstname_field = 'pepto'
# Apellido
lastname_field = 'pepo'
# contraseña >=8
password_field = 'Pepe7890'
# Correo para Registrar.
email_field = 'pepe194@gmail.com'
# Website personal.Ejemplo: https://www.google.com
website = 'https://versaria.es'
# Biografia
bio = 'Mercadotecnia'


# Variable de entorno de la api_key de 2captcha.
key_2captcha = os.environ.get('2CAPTCHA_APIKEY')

def api_2captcha(google_key):
    # Introducir el Apikey 2 veces.
    api_key = os.getenv(key_2captcha, key_2captcha)

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey= google_key,
            # Pagina donde esta el recapcha
            url='https://revistas.ufpi.br/index.php/gecont/user/register')
        token = result['code']        
        return token

    except Exception as e:
        sys.exit(e)

    else:
        sys.exit('solved: ' + str(result))

def registro(url,name,firstname,lastname,password,email,bio,website):
    # Especificar el PATH de geckodriver en Windows.
    driver = webdriver.Firefox(executable_path=r"c:\se\geckodriver.exe")
    # import pdb; pdb.set_trace()
    
     # Abrir la pagina especificada.
    print('Abriendo Navegador y cargando la pagina:\n ',url )
    driver.get(url)  
    
    try:
        
        # Boton de Registro(Sign Up)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/ul/li[4]/a").click()     
                                                                                                       
        # Registro.
       
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))

        # Ingreso de los campos requeridos para registrar.
        print('**********\nIngresando Datos.')
        try:  
            sleep(1.8)
            # Ubicar campo.
            name_field = driver.find_element_by_id('username')
            # Limpiar campo.
            name_field.clear()
            # Ingresar datos en el campo.
            name_field.send_keys(name) 

            password_field = driver.find_element_by_id('password') 
            password_field.clear()
            password_field.send_keys(password) 

            password_field = driver.find_element_by_id('password2') 
            password_field.clear()
            password_field.send_keys(password)
      
            firstname_field = driver.find_element_by_name('firstName')
            firstname_field.clear()
            firstname_field.send_keys(firstname) 
         
            lastname_field = driver.find_element_by_name('lastName')
            lastname_field.clear()
            lastname_field.send_keys(lastname)              
         
            email_field = driver.find_element_by_name('email') 
            email_field.clear()
            email_field.send_keys(email) 

            email_field = driver.find_element_by_name('confirmEmail') 
            email_field.clear()
            email_field.send_keys(email) 
            
            website_field = driver.find_element_by_name('userUrl') 
            website_field.clear()
            website_field.send_keys(website)         
     
            driver.find_element_by_xpath('//*[@id="sendPassword"]').click()     

        except:
            print('Error al Ingresar datos.')
            sys.exit()

        # 2Captcha bot.
        sleep(1.8) 
        print('**********\nObteniendo sitekey para reCAPTCHA.')       
        try:
            captcha = driver.find_element_by_class_name("g-recaptcha")
            google = captcha.get_attribute("data-sitekey")
        except:
            print('Error al obtener sitekey. Intentelo manualmente.')
            sys.exit()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print('Resolviendo reCAPTCHA.')		
        try:
            token = api_2captcha(google)
            sleep(2)
            print('reCaptcha Exitoso.')
        
        except:	
            print("Timeout1. Error resolviendo reCaptcha")
            sys.exit()
            #driver.close()
        try:
            input_captcha = driver.find_element_by_id("g-recaptcha-response")
            driver.execute_script("arguments[0].style.display = 'block';", input_captcha)
            input_captcha.send_keys(token)
            print('Token ingresado con exito.')
        except:
            print('Error al introducir el token de 2cpatcha.')     
            sys.exit()        
             
             
        # Boton Registro
        print('**********\nRegistrando....')
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/form/p[3]/input[1]'))).click()
        except:
            print('Error al registrar. Revisar Datos.(linea 80)')
            exit()         
     
        print('********\nRegistro Completo exitoso')

        # # Cerrar el navegador.
        # # driver.close()

    except:
        print('********\nRegistro fallido.')
        # Cerrar el navegador.
        # driver.close()


registro(url,user_field,firstname_field,lastname_field,password_field,email_field,bio,website)