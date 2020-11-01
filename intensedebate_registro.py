from selenium import webdriver
from time import sleep
# Se importa WebDriverWait y las otras librerias para hace esperas explicitas.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import exit

# Ingresar variables a registrar
url = 'https://www.intensedebate.com/'
# Datos.
user_field = 'pefl09e'
# Password >= 6 caracteres
password_field = 'pepe78'
# Correo para Registrar.
email_field = 'pepo463@gmail.com'


def registro(url,name,password,email):
    # Especificar el PATH de geckodriver en Windows.
    driver = webdriver.Firefox(executable_path=r"c:\se\geckodriver.exe")
    # import pdb; pdb.set_trace()
    
     # Abrir la pagina especificada.
    print('Abriendo Navegador y cargando la pagina:\n ',url )
    driver.get(url)  
    
    try:
        
        # Boton de Registro(Sign Up)
        driver.find_element_by_xpath("/html/body/div[1]/div/p[1]/a").click()     
                                                                                                                                                                                                                                         
        # Registro.
     
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/p[3]/a/span[2]")))

        # Ingreso de los campos requeridos para registrar.
        print('**********\nIngresando Datos.')
        try:                     
        
             # Ubicar campo.
            name_field = driver.find_element_by_name('txtName')
            # Limpiar campo.
            name_field.clear()
            # Ingresar datos en el campo.
            name_field.send_keys(name)
            
            email_field = driver.find_element_by_name('txtEmail') 
            email_field.clear()
            email_field.send_keys(email)  

            password_field = driver.find_element_by_name('txtPassword') 
            password_field.clear()
            password_field.send_keys(password)

            password_field = driver.find_element_by_name('txtPassword2') 
            password_field.clear()
            password_field.send_keys(password)                       
                
        except:
            print('Error al ingresar los Datos. Revise.')
            exit()          
      
        sleep(1.8) 
        
        # # Boton de registro.
        print('**********\nRegistrando....')
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/p[3]/a/span[2]"))).click()
        except:
            print('Error al registar. Revisar')
            exit() 

        try:
            # Confirmar que el registro fue exitoso y paso a la siguiente pagina.
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/h4/a")))
        except:
            print('Error al terminar registro de cuenta. Revisar.')
            exit()
      
        print('Registro exitoso')

        # # Cerrar el navegador.
        # # driver.close()

    except:
        print('Registro fallido. Revisar.')
        # Cerrar el navegador.
        # driver.close()


registro(url,user_field,password_field,email_field)