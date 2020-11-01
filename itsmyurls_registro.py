from selenium import webdriver
# Se importa WebDriverWait y las otras librerias para hace esperas explicitas.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import exit

# Ingresar variables a registrar
url = 'https://itsmyurls.com/'
# Usuario o User
user_field = 'pefm71e'
# Nombre Completo
firstname_field = 'pepto'
# contraseña >=8
password_field = 'Pepe7890'
# Correo para Registrar.
email_field = 'pepe194@gmail.com'


def registro(url,name,firstname,password,email):
    # Especificar el PATH de geckodriver en Windows.
    driver = webdriver.Firefox(executable_path=r"c:\se\geckodriver.exe")
    # import pdb; pdb.set_trace()
    
     # Abrir la pagina especificada.
    print('Abriendo Navegador y cargando la pagina:\n ',url )
    driver.get(url)  
    
    try:
        
        # Boton de Registro(Sign Up)
        driver.find_element_by_xpath("/html/body/section[2]/nav/div/div/div[2]/ul/li[2]/a").click()     
                                                                                                                                                                                                                                         
        # Registro.
       
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[3]/div/form/div[6]/button")))

        
        # Ingreso de los campos requeridos para registrar.
        print('**********\nIngresando Datos.')
        try:                    
             
            firstname_field = driver.find_element_by_name('name')
            firstname_field.clear()
            firstname_field.send_keys(firstname)

             # Ubicar campo.
            name_field = driver.find_element_by_name('username')
            # Limpiar campo.
            name_field.clear()
            # Ingresar datos en el campo.
            name_field.send_keys(name)        
         
            email_field = driver.find_element_by_name('email') 
            email_field.clear()
            email_field.send_keys(email) 

            email_field = driver.find_element_by_name('confirm_email') 
            email_field.clear()
            email_field.send_keys(email) 
            
            password_field = driver.find_element_by_name('password') 
            password_field.clear()
            password_field.send_keys(password)   
                
        except:
            print('Error al ingresar los Datos. Revise.(linea 47)')
            exit()          
            
              
        # Boton Siguiente
        print('**********\nRegistrando....')
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/form/div[6]/button'))).click()
        except:
            print('Error al registrar. Revisar Datos.(linea 80)')
            exit()         
                
        # COnfirmar que paso a la pagina de registro exitoso
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/p/a/span")))
            
            print('********\nIngreso de datos y registro terminados.')
        except:
            print('Error al Registrar Cuenta. Revisar. Linea 88')
            exit()      
   
        print('********\nRegistro Completo exitoso')

        # # Cerrar el navegador.
        # # driver.close()

    except:
        print('********\nRegistro fallido.')
        # Cerrar el navegador.
        # driver.close()


registro(url,user_field,firstname_field,password_field,email_field)