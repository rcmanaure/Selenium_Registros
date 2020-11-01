from selenium import webdriver
from time import sleep
from random import choice
# Se importa WebDriverWait y las otras librerias para hace esperas explicitas.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import exit

# Ingresar variables a registrar
url = 'https://www.aeriagames.com/'
# Datos.
user_field = 'pefm571e'
# Nombre
firstname_field = 'pepto'
# Requisitos de la contraseña: 1 mayúscula, 1 minúscula, 1 número, 8 - 15 caracteres
password_field = 'Pepe7890'
# Correo para Registrar.
email_field = 'pepe1794@gmail.com'
# Website personal
website = 'versaria.es'
# Biografia
bio = 'Mercadotecnia'




def registro(url,name,firstname,password,email,bio,website):
    # Especificar el PATH de geckodriver en Windows.
    driver = webdriver.Firefox(executable_path=r"c:\se\geckodriver.exe")
    # import pdb; pdb.set_trace()
    
     # Abrir la pagina especificada.
    print('Abriendo Navegador y cargando la pagina:\n ',url )
    driver.get(url)  
    
    try:
        
        # Boton de Registro(Sign Up)
        driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div/div/span[1]/a/span").click()     
                                                                                                                                                                                                                                         
        # Registro.
       
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "account_signup_submit")))

        
        # Ingreso de los campos requeridos para registrar.
        print('**********\nIngresando Datos.')
        try:                    
                     
         
            email_field = driver.find_element_by_name('edit[mail]') 
            email_field.clear()
            email_field.send_keys(email)  

            
            months = ['/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[1]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[2]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[3]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[4]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[5]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[6]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[7]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[8]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[9]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[10]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[11]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[1]/select/option[12]'
                    ]


            days = ['/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[1]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[2]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[3]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[4]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[5]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[6]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[7]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[8]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[9]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[11]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[12]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[13]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[15]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[16]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[17]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[18]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[19]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[20]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[21]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[22]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[23]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[24]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[25]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[26]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[27]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[28]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[2]/select/option[29]'
                    ]

            years = ['/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[41]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[42]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[43]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[44]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[45]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[46]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[47]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[48]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[49]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[50]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[51]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[52]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[53]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[54]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[55]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[56]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[57]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[58]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[59]',
                    '/html/body/div[4]/div[2]/div/div[1]/form/div/div[2]/div[2]/div/div/div[3]/select/option[60]',
                    ]
                   
            # Random Birthday.(fecha de nacimiento)
            month = choice(months)
            day = choice(days)
            year = choice(years)                                          
           
            driver.find_element_by_xpath(month).click()      
            driver.find_element_by_xpath(day).click()      
            driver.find_element_by_xpath(year).click()

                
        except:
            print('Error al ingresar los Datos. Revise.(linea 169)')
            exit()          
            
              
        # Boton Siguiente
        print('**********\nRegistrando....')
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_signup_submit"]'))).click()
        except:
            print('Error al registrar. Revisar Datos.(linea 141)')
            exit() 
        
        # Nombre de Usuario
        try:    
            # Ubicar campo.
            name_field = driver.find_element_by_name('edit[name]')
            # Limpiar campo.
            name_field.clear()
            # Ingresar datos en el campo.
            name_field.send_keys(name)

            # Disponibiliad de Nombre de Usuario.
            # try:
            #     driver.find_element_by_class_name('signupVerifier_errorIcon signupVerifier_check_error')
            #     print('Error en Disponibilidad de Nombre de Usuario. Usuando Aleatorio.(linea 226)')
            #     driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[1]/form/div/div[3]/div[1]/div[2]/ul/li[2]/div/ul/li[2]').click()

            # except:
            #     pass                
            
            sleep(3)
            password_field = driver.find_element_by_name('edit[pass]') 
            password_field.clear()
            password_field.send_keys(password)

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "account_signup2_submit"))).click()

        except:
            print('Error al ingresar Nombre de Usuario. Linea 148') 
            exit()
        
        # COnfirmar que paso a la pagina de registro exitoso
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/a")))
            print('********\nIngreso de datos y registro terminados. Configurando Perfil.')
        except:
            print('Error al Registrar Cuenta. Revisar. Linea 147')
            exit()

        # Entrar a configuracion de perfil
        try:
            sleep(1.8)
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/div/ul/li[2]/a[2]').click()      

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[1]/div[1]/div[4]/div[1]/div/div[1]/ul/li[1]/a"))).click()
            
        except:
            print('Error al ingresar a COnfiguracion de Perfil.(linea 188)')
            exit()

        # Ingresar Nombre
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/form/div/input[3]")))

            firstname_field = driver.find_element_by_name('edit[fname]')
            firstname_field.clear()
            firstname_field.send_keys(firstname)

            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/form/div/input[3]').click()

            print('********\nIngreso de nombre en perfil exitoso...')
        except:
            print('Error al ingresar Nombre. (linea 197)')
            exit()
        
        # Entrar a configuracion de perfil
        try:
           sleep(2) 
           WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[1]/div[1]/div[5]/div[1]/div/div[1]/ul/li[1]/a"))).click()
            
        except:
            print('Error al ingresar a COnfiguracion de Perfil.(linea 211)')
            exit()

        # Ingresar Biografia
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div/ul/li[2]/a"))).click()

            bio_field = driver.find_element_by_name('edit[blurb]') 
            bio_field.clear()
            bio_field.send_keys(bio)
            
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/form/div/input[3]').click()
            print('Ingreso de Biografia  en perfil exitoso...')
        except:
            print('Error al ingresar biografia. (linea 220)')
            exit()

        
        # Entrar a configuracion de perfil
        try:
            sleep(2)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[1]/div[1]/div[5]/div[1]/div/div[1]/ul/li[1]/a"))).click()
            
        except:
            print('Error al ingresar a COnfiguracion de Perfil.(linea 235)')
            exit()

        # Ingresar website
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div/ul/li[3]/a"))).click()
            
            website_field = driver.find_element_by_name('edit[website]') 
            website_field.clear()
            website_field.send_keys(website)
            
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/form/div/input[3]').click()
            print('Ingreso de Website en perfil exitoso...')
        except:
            print('Error al ingresar website. (linea 244)')
            exit()
        
         # Entrar a configuracion de perfil
        try:
            sleep(2)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div[1]/div[1]/div[5]/div[1]/div/div[1]/ul/li[1]/a"))).click()
            
        except:
            print('Error al ingresar a COnfiguracion de Perfil.(linea 258)')
            exit()

        # Ingresar preferencias
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div/ul/li[5]/a"))).click()            
                      
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/form/div/fieldset/div[2]/div[2]/select/option[2]').click()

            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/form/div/input[3]').click()
            print('Seleccion de preferencias exitoso...')
        except:
            print('Error al ingresar preferencias. (linea 267)')
            exit()
        
      
        print('********\nRegistro Completo exitoso')

        # # Cerrar el navegador.
        # # driver.close()

    except:
        print('********\nRegistro fallido.')
        # Cerrar el navegador.
        # driver.close()


registro(url,user_field,firstname_field,password_field,email_field,bio,website)