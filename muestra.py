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


# Ingresar variables a registrar
url = 'https://coub.com/i4udmpj787'
name_field = 'pefufyke'
username_field = ''
password_field = 'pepe3677'
email_field = ''
# Website personal
website = 'versaria.es'
# Biografia
bio = 'Mercadotecnia'



def api_2captcha(google_key):
    # Introducir el Apikey 2 veces.
    api_key = os.getenv('', '')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey= google_key,
            url='https://coub.com/i4udmpj787')
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
        
        # Boton de Registro(Sign Up)
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "sign-up"))).click()
        driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[2]/div/button[2]").click() 


        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))

        # Ingreso de los campos requeridos para registrar.
        print('**********\nIngresando Datos.')
        try:
            # Ubicar campo.
            name_field = driver.find_element_by_name('name')
            # Limpiar campo.
            name_field.clear()
            # Ingresar datos en el campo.
            name_field.send_keys(name)

            
            # username_field = driver.find_element_by_id('signupEmailUsername')       
            # username_field.clear()       
            # username_field.send_keys(username)

            email_field = driver.find_element_by_name('email') 
            email_field.clear()
            email_field.send_keys(email)        
            
            # password_field = driver.find_element_by_id('user_password') 
            # password_field.clear()
            # password_field.send_keys(password)

            password_field = driver.find_element_by_name('password') 
            password_field.clear()
            password_field.send_keys(password)
                                            
            # driver.find_element_by_xpath("/html/body/div[1]/article[6]/section/form/div/fieldset/div[1]/div[2]/select/option[3]").click()      

            # Random Birthday.(fecha de nacimiento)
            # month = randint(1,12)
            # day = randint(1,28)
            # year = randint(1980,2001)

            # birthday_field = driver.find_element_by_name('birthMonth') 
            # birthday_field.clear()
            # birthday_field.send_keys(month)
            
            # birthday_field = driver.find_element_by_name('birthDay') 
            # birthday_field.clear()
            # birthday_field.send_keys(day)

            # birthday_field = driver.find_element_by_name('birthYear') 
            # birthday_field.clear()
            # birthday_field.send_keys(year)
        except:
            print('Error al ingresar los Datos. Revise.')
            exit()


        # 2Captcha bot.
        sleep(1.8) 
        # print('**********\nObteniendo sitekey para reCAPTCHA.')       
        # try:
        #     captcha = driver.find_element_by_class_name("g-recaptcha")
        #     google = captcha.get_attribute("data-sitekey")
        # except:
        #     print('Error al obtener sitekey. Intentelo manualmente.')
        #     exit()
        google = ''
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print('Resolviendo reCAPTCHA.')		
        try:
            token = api_2captcha(google)
            sleep(2)
            print('reCaptcha Exitoso.')
        
        except:	
            print("Timeout1. Error resolviendo reCaptcha")
            exit()
            #driver.close()
        try:
            input_captcha = driver.find_element_by_id("g-recaptcha-response")
            driver.execute_script("arguments[0].style.display = 'block';", input_captcha)
            input_captcha.send_keys(token)
            print('Token ingresado con exito.')
        except:
            print('Error al introducir el token de 2cpatcha.')     
            exit()          
                    

        driver.find_element_by_name("agreeTOS").click()
        
        # # Boton de registro.
        print('**********\nRegistrando....')
        try:
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/button").click()
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/button"))).click()
        except:
            print('Error al registrar. Revisar Datos.')
            exit()           

        

        # usuario
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div[2]/div[2]/div/div[3]/a/img"))).click()

        # Perfil
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[3]/div[2]/div[3]/div/a/svg/path"))).click()

        # Ingreso de bio y website
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "channel[description]")))

        bio_field = driver.find_element_by_name('channel[description]') 
        bio_field.clear()
        bio_field.send_keys(bio)

        website_field = driver.find_element_by_name('channel[homepage]') 
        website_field.clear()
        website_field.send_keys(website)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/div[3]/div/div[2]/button"))).click()

    # De vuelta al usuario
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div[2]/div[2]/div/div[3]/a/img"))).click()


        print('Registro exitoso')

        # # Cerrar el navegador.
        # # driver.close()

    except:
        print('Registro fallido. Revisar.')
        # Cerrar el navegador.
        # driver.close()


registro(url,name_field,username_field,password_field,email_field,website,bio)



        # try:
        #     sleep(10)
        #     menu = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/section/div[1]/div/nav/ul/li[1]")))
        #     sub_menu = driver.find_element_by_xpath('/html/body/header/section/div[1]/div/nav/ul/li[1]/ul/li[12]/a')
        #     ActionChains(driver).move_to_element(menu).click(sub_menu).perform()
        # except:
        #     print('Error al ingresar a usuario')
        #     exit()



            # months = ['/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[2]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[3]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[4]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[5]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[6]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[7]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[8]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[9]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[10]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[11]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[12]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[2]/option[13]'
            #         ]


            # days = ['/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[2]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[3]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[4]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[5]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[6]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[7]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[8]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[9]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[10]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[11]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[12]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[13]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[15]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[16]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[17]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[18]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[19]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[20]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[21]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[22]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[23]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[24]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[25]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[26]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[27]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[28]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[1]/option[29]']

            # years = ['/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[42]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[41]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[40]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[39]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[38]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[37]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[36]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[35]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[34]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[33]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[32]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[31]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[29]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[28]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[27]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[26]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[25]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[24]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[23]',
            #         '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/form/fieldset[4]/select[3]/option[22]',
            #         ]
                   
            # # Random Birthday.(fecha de nacimiento)
            # month = choice(months)
            # day = choice(days)
            # year = choice(years)                                          
           
            # driver.find_element_by_xpath(month).click()      
            # driver.find_element_by_xpath(day).click()      
            # driver.find_element_by_xpath(year).click()

# Redes sociales
        # try:
        #     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/nav/ul/li[4]/a"))).click()

        #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "id_website")))

        #     website_field = driver.find_element_by_name('website') 
        #     website_field.clear()
        #     website_field.send_keys(website)

        #     twitter_field = driver.find_element_by_name('twitter') 
        #     twitter_field.clear()
        #     twitter_field.send_keys(twitter)

        #     instagram_field = driver.find_element_by_name('instagram') 
        #     instagram_field.clear()
        #     instagram_field.send_keys(instagram)

        #     tumblr_field = driver.find_element_by_name('tumblr') 
        #     tumblr_field.clear()
        #     tumblr_field.send_keys(tumblr)

        #     flickr_field = driver.find_element_by_name('flickr') 
        #     flickr_field.clear()
        #     flickr_field.send_keys(flickr)

        #     behance_field = driver.find_element_by_name('behance') 
        #     behance_field.clear()
        #     behance_field.send_keys(behance)

        #     linkedin_field = driver.find_element_by_name('linkedin') 
        #     linkedin_field.clear()
        #     linkedin_field.send_keys(linkedin)

        #     youtube_field = driver.find_element_by_name('youtube') 
        #     youtube_field.clear()
        #     youtube_field.send_keys(youtube)

        #     vimeo_field = driver.find_element_by_name('vimeo') 
        #     vimeo_field.clear()
        #     vimeo_field.send_keys(vimeo)
            
        #     dribble_field = driver.find_element_by_name('dribble') 
        #     dribble_field.clear()
        #     dribble_field.send_keys(dribble)

        #     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/form/input[2]"))).click()
        # except:
        #     print('Error al ingresar Redes Sociales. Revisar.')
        #     exit()



# Acelerar la carga de la pagina. Eager(wait until the initial HTML document has been completely loaded and parsed, and discards loading of stylesheets, images and subframes.)
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "normal"  #  complete
#caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"
driver = webdriver.Firefox(desired_capabilities=caps, executable_path=r'C:\path\to\geckodriver.exe')
driver.get("http://google.com")


